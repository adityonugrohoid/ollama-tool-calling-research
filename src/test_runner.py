"""Test orchestrator that runs test functions against models and outputs results.

Manages test execution, captures results, and prints summary tables using rich.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from rich.console import Console
from rich.table import Table

from src.ollama_client import is_model_available

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
    notes: str = ""
    error: str | None = None
    details: dict[str, Any] = field(default_factory=dict)


# Type alias for test functions
# A test function takes a model name and returns a TestResult
TestFunction = Callable[[str], TestResult]


def run_test_for_model(
    test_fn: TestFunction,
    model: str,
    test_name: str,
) -> TestResult:
    """Run a single test function against a single model with error handling.

    Catches all exceptions so a model crash doesn't crash the suite.
    """
    # Check model availability first
    if not is_model_available(model):
        return TestResult(
            model=model,
            test_name=test_name,
            passed=False,
            native_or_text="error",
            parse_success=False,
            notes="Model not available",
            error="Model not available on this Ollama instance",
        )

    try:
        result = test_fn(model)
        return result
    except Exception as e:
        return TestResult(
            model=model,
            test_name=test_name,
            passed=False,
            native_or_text="error",
            parse_success=False,
            notes=f"Exception: {type(e).__name__}",
            error=str(e),
        )


def run_tests(
    test_fns: dict[str, TestFunction],
    models: list[str],
) -> list[TestResult]:
    """Run all test functions against all models.

    Args:
        test_fns: Dict mapping test name to test function.
        models: List of model names to test.

    Returns:
        List of all TestResults.
    """
    results: list[TestResult] = []
    total = len(test_fns) * len(models)
    current = 0

    for model in models:
        console.rule(f"[bold blue]{model}[/bold blue]")

        for test_name, test_fn in test_fns.items():
            current += 1
            console.print(
                f"  [{current}/{total}] Running [cyan]{test_name}[/cyan]...",
                end=" ",
            )

            result = run_test_for_model(test_fn, model, test_name)
            results.append(result)

            # Print inline status
            if result.passed:
                console.print("[green]PASS[/green]", end="")
            elif result.error and "not available" in (result.error or ""):
                console.print("[yellow]SKIP[/yellow]", end="")
            else:
                console.print("[red]FAIL[/red]", end="")

            if result.notes:
                console.print(f"  ({result.notes})", end="")
            console.print()

    return results


def print_summary_table(
    results: list[TestResult],
    models: list[str],
    test_names: list[str],
) -> None:
    """Print a rich summary matrix (models x tests)."""
    console.print()
    console.rule("[bold]Summary Matrix[/bold]")

    table = Table(title="Test Results", show_lines=True)
    table.add_column("Model", style="bold cyan", min_width=15)

    for test_name in test_names:
        table.add_column(test_name, min_width=8, justify="center")

    # Build lookup
    lookup: dict[tuple[str, str], TestResult] = {}
    for r in results:
        lookup[(r.model, r.test_name)] = r

    for model in models:
        row: list[str] = [model]
        for test_name in test_names:
            result = lookup.get((model, test_name))
            if result is None:
                row.append("[dim]---[/dim]")
            elif result.passed:
                fmt = result.native_or_text[0].upper() if result.native_or_text != "error" else "?"
                row.append(f"[green]PASS ({fmt})[/green]")
            elif result.error and "not available" in (result.error or ""):
                row.append("[yellow]SKIP[/yellow]")
            else:
                fmt = result.native_or_text[0].upper() if result.native_or_text != "error" else "?"
                row.append(f"[red]FAIL ({fmt})[/red]")

        table.add_row(*row)

    console.print(table)

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
) -> Path:
    """Save results summary to observations/summaries/ as markdown."""
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    filepath = SUMMARIES_DIR / f"{ts}_results.md"

    lines: list[str] = []
    lines.append(f"# Test Results — {ts}")
    lines.append("")
    lines.append(f"**Models:** {', '.join(models)}")
    lines.append(f"**Tests:** {', '.join(test_names)}")
    lines.append("")

    # Summary table
    header = "| Model | " + " | ".join(test_names) + " |"
    sep = "|-------|" + "|".join(["------" for _ in test_names]) + "|"
    lines.append(header)
    lines.append(sep)

    lookup: dict[tuple[str, str], TestResult] = {}
    for r in results:
        lookup[(r.model, r.test_name)] = r

    for model in models:
        row_parts = [model]
        for test_name in test_names:
            result = lookup.get((model, test_name))
            if result is None:
                row_parts.append("---")
            elif result.passed:
                row_parts.append(f"PASS ({result.native_or_text})")
            elif result.error and "not available" in (result.error or ""):
                row_parts.append("SKIP")
            else:
                row_parts.append(f"FAIL ({result.native_or_text})")
        lines.append("| " + " | ".join(row_parts) + " |")

    lines.append("")

    # Detailed results
    lines.append("## Detailed Results")
    lines.append("")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        if r.error and "not available" in (r.error or ""):
            status = "SKIP"
        lines.append(f"### {r.model} / {r.test_name} — {status}")
        lines.append(f"- Format: {r.native_or_text}")
        lines.append(f"- Parse success: {r.parse_success}")
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
