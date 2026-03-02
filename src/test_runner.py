"""Test orchestrator that runs test functions against models and outputs results.

Manages test execution across the flag matrix (stream × think), captures results,
and prints summary tables using rich.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from rich.console import Console
from rich.table import Table

from src.ollama_client import is_model_available
from tests.config import FlagCombo, ALL_FLAG_COMBOS

console = Console()

SUMMARIES_DIR = Path(__file__).parent.parent / "observations" / "summaries"
SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class TestResult:
    """Structured result from a single test run."""
    model: str
    test_name: str
    passed: bool
    native_or_text: str  # "native", "text", "none", "mixed", "error"
    parse_success: bool
    stream: bool = False
    think: bool = False
    classification: str = ""  # "native", "text", "misrouted", "none"
    notes: str = ""
    error: str | None = None
    details: dict[str, Any] = field(default_factory=dict)


# Type alias for test functions — now takes model name AND flag combo
TestFunction = Callable[[str, FlagCombo], TestResult]


def run_test_for_model(
    test_fn: TestFunction,
    model: str,
    test_name: str,
    flags: FlagCombo,
) -> TestResult:
    """Run a single test function against a single model with error handling.

    Catches all exceptions so a model crash doesn't crash the suite.
    """
    if not is_model_available(model):
        return TestResult(
            model=model,
            test_name=test_name,
            passed=False,
            native_or_text="error",
            parse_success=False,
            stream=flags.stream,
            think=flags.think,
            notes="Model not available",
            error="Model not available on this Ollama instance",
        )

    try:
        result = test_fn(model, flags)
        return result
    except Exception as e:
        return TestResult(
            model=model,
            test_name=test_name,
            passed=False,
            native_or_text="error",
            parse_success=False,
            stream=flags.stream,
            think=flags.think,
            notes=f"Exception: {type(e).__name__}",
            error=str(e),
        )


def run_tests(
    test_fns: dict[str, TestFunction],
    models: list[str],
    flag_combos: list[FlagCombo] | None = None,
) -> list[TestResult]:
    """Run all test functions against all models across all flag combos.

    Triple loop: models × tests × flag_combos.

    Args:
        test_fns: Dict mapping test name to test function.
        models: List of model names to test.
        flag_combos: List of FlagCombo to test. Defaults to ALL_FLAG_COMBOS.

    Returns:
        List of all TestResults.
    """
    if flag_combos is None:
        flag_combos = ALL_FLAG_COMBOS

    results: list[TestResult] = []
    total = len(models) * len(test_fns) * len(flag_combos)
    current = 0

    for model in models:
        console.rule(f"[bold blue]{model}[/bold blue]")

        for test_name, test_fn in test_fns.items():
            for flags in flag_combos:
                current += 1
                console.print(
                    f"  [{current}/{total}] Running [cyan]{test_name}[/cyan] "
                    f"[dim][{flags.label}][/dim]...",
                    end=" ",
                )

                result = run_test_for_model(test_fn, model, test_name, flags)
                results.append(result)

                # Print inline status
                if result.passed:
                    console.print("[green]PASS[/green]", end="")
                elif result.error and "not available" in (result.error or ""):
                    console.print("[yellow]SKIP[/yellow]", end="")
                else:
                    console.print("[red]FAIL[/red]", end="")

                if result.classification:
                    console.print(f" [{result.classification}]", end="")

                if result.notes:
                    console.print(f"  ({result.notes})", end="")
                console.print()

    return results


def print_summary_table(
    results: list[TestResult],
    models: list[str],
    test_names: list[str],
    flag_combos: list[FlagCombo] | None = None,
) -> None:
    """Print rich summary tables — one per flag combo plus a comparison table."""
    if flag_combos is None:
        flag_combos = ALL_FLAG_COMBOS

    # Build lookup: (model, test_name, flag_label) -> TestResult
    lookup: dict[tuple[str, str, str], TestResult] = {}
    for r in results:
        label = "S0T0"
        for fc in flag_combos:
            if r.stream == fc.stream and r.think == fc.think:
                label = fc.label
                break
        lookup[(r.model, r.test_name, label)] = r

    # One table per flag combo
    for flags in flag_combos:
        console.print()
        console.rule(f"[bold]Summary — {flags.label} (stream={flags.stream}, think={flags.think})[/bold]")

        table = Table(title=f"Results [{flags.label}]", show_lines=True)
        table.add_column("Model", style="bold cyan", min_width=15)

        for test_name in test_names:
            table.add_column(test_name, min_width=8, justify="center")

        for model in models:
            row: list[str] = [model]
            for test_name in test_names:
                result = lookup.get((model, test_name, flags.label))
                if result is None:
                    row.append("[dim]---[/dim]")
                elif result.passed:
                    cls = result.classification[0].upper() if result.classification else "?"
                    row.append(f"[green]PASS ({cls})[/green]")
                elif result.error and "not available" in (result.error or ""):
                    row.append("[yellow]SKIP[/yellow]")
                else:
                    cls = result.classification[0].upper() if result.classification else "?"
                    row.append(f"[red]FAIL ({cls})[/red]")

            table.add_row(*row)

        console.print(table)

    # Condensed comparison table (all combos side by side)
    if len(flag_combos) > 1:
        console.print()
        console.rule("[bold]Flag Comparison[/bold]")

        cmp_table = Table(title="Pass/Fail Across Flag Combos", show_lines=True)
        cmp_table.add_column("Model", style="bold cyan", min_width=15)

        for test_name in test_names:
            cmp_table.add_column(test_name, min_width=len(flag_combos) * 2, justify="center")

        for model in models:
            row = [model]
            for test_name in test_names:
                codes: list[str] = []
                for flags in flag_combos:
                    result = lookup.get((model, test_name, flags.label))
                    if result is None:
                        codes.append("-")
                    elif result.passed:
                        codes.append("P")
                    elif result.error and "not available" in (result.error or ""):
                        codes.append("S")
                    else:
                        codes.append("F")
                code_str = "".join(codes)
                if all(c == "P" for c in codes):
                    row.append(f"[green]{code_str}[/green]")
                elif all(c in ("F", "S") for c in codes):
                    row.append(f"[red]{code_str}[/red]")
                else:
                    row.append(f"[yellow]{code_str}[/yellow]")
            cmp_table.add_row(*row)

        console.print(cmp_table)
        combo_legend = " ".join(f"{i}={fc.label}" for i, fc in enumerate(flag_combos))
        console.print(f"[dim]Positions: {combo_legend} | P=pass F=fail S=skip[/dim]")

    # Print stats
    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed and not (r.error and "not available" in (r.error or "")))
    skipped = sum(1 for r in results if r.error and "not available" in (r.error or ""))
    console.print(
        f"\n[green]{passed} passed[/green]  "
        f"[red]{failed} failed[/red]  "
        f"[yellow]{skipped} skipped[/yellow]  "
        f"({len(results)} total)"
    )


def save_summary(
    results: list[TestResult],
    models: list[str],
    test_names: list[str],
    flag_combos: list[FlagCombo] | None = None,
) -> Path:
    """Save results summary to observations/summaries/ as markdown."""
    if flag_combos is None:
        flag_combos = ALL_FLAG_COMBOS

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    filepath = SUMMARIES_DIR / f"{ts}_results.md"

    lines: list[str] = []
    lines.append(f"# Test Results — {ts}")
    lines.append("")
    lines.append(f"**Models:** {', '.join(models)}")
    lines.append(f"**Tests:** {', '.join(test_names)}")
    combo_labels = ", ".join(fc.label for fc in flag_combos)
    lines.append(f"**Flag combos:** {combo_labels}")
    lines.append("")

    # Build lookup
    lookup: dict[tuple[str, str, str], TestResult] = {}
    for r in results:
        label = "S0T0"
        for fc in flag_combos:
            if r.stream == fc.stream and r.think == fc.think:
                label = fc.label
                break
        lookup[(r.model, r.test_name, label)] = r

    # One table per flag combo
    for flags in flag_combos:
        lines.append(f"## {flags.label} (stream={flags.stream}, think={flags.think})")
        lines.append("")

        header = "| Model | " + " | ".join(test_names) + " |"
        sep = "|-------|" + "|".join(["------" for _ in test_names]) + "|"
        lines.append(header)
        lines.append(sep)

        for model in models:
            row_parts = [model]
            for test_name in test_names:
                result = lookup.get((model, test_name, flags.label))
                if result is None:
                    row_parts.append("---")
                elif result.passed:
                    row_parts.append(f"PASS ({result.classification})")
                elif result.error and "not available" in (result.error or ""):
                    row_parts.append("SKIP")
                else:
                    row_parts.append(f"FAIL ({result.classification})")
            lines.append("| " + " | ".join(row_parts) + " |")

        lines.append("")

    # Comparison table
    if len(flag_combos) > 1:
        lines.append("## Flag Comparison")
        lines.append("")
        combo_legend = " ".join(f"{i}={fc.label}" for i, fc in enumerate(flag_combos))
        lines.append(f"Positions: {combo_legend} | P=pass F=fail S=skip")
        lines.append("")

        header = "| Model | " + " | ".join(test_names) + " |"
        sep = "|-------|" + "|".join(["------" for _ in test_names]) + "|"
        lines.append(header)
        lines.append(sep)

        for model in models:
            row_parts = [model]
            for test_name in test_names:
                codes: list[str] = []
                for flags in flag_combos:
                    result = lookup.get((model, test_name, flags.label))
                    if result is None:
                        codes.append("-")
                    elif result.passed:
                        codes.append("P")
                    elif result.error and "not available" in (result.error or ""):
                        codes.append("S")
                    else:
                        codes.append("F")
                row_parts.append("".join(codes))
            lines.append("| " + " | ".join(row_parts) + " |")

        lines.append("")

    # Detailed results
    lines.append("## Detailed Results")
    lines.append("")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        if r.error and "not available" in (r.error or ""):
            status = "SKIP"
        flag_label = "S0T0"
        for fc in flag_combos:
            if r.stream == fc.stream and r.think == fc.think:
                flag_label = fc.label
                break
        lines.append(f"### {r.model} / {r.test_name} [{flag_label}] — {status}")
        lines.append(f"- Classification: {r.classification}")
        lines.append(f"- Parse success: {r.parse_success}")
        lines.append(f"- Stream: {r.stream}, Think: {r.think}")
        if r.notes:
            lines.append(f"- Notes: {r.notes}")
        if r.error:
            lines.append(f"- Error: {r.error}")
        if r.details:
            lines.append(f"- Details: {r.details}")
        lines.append("")

    filepath.write_text("\n".join(lines))
    console.print(f"\n[dim]Summary saved to {filepath}[/dim]")
    return filepath
