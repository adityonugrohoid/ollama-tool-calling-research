#!/usr/bin/env python3
"""Entry point for running the Ollama tool calling research test suite.

Usage:
    # Run all tests against P0 models (default, all 4 flag combos)
    python run_all.py

    # Run specific tests against specific models
    python run_all.py --models gpt-oss:20b,ministral-3:8b --tests single_tool,multi_tool

    # Run only baseline flag combo
    python run_all.py --flags S0T0

    # Run specific flag combos
    python run_all.py --flags S0T0,S0T1

    # Run all tests against all models
    python run_all.py --models all
"""

import argparse
import sys

from rich.console import Console

from src.test_runner import (
    TestFunction,
    run_tests,
    print_summary_table,
    save_summary,
)
from tests.config import (
    GA_MODELS, GB_MODELS, GC_MODELS, GD_MODELS,
    ALL_MODELS, FlagCombo, ALL_FLAG_COMBOS,
)

# Import all test modules
from tests import (
    test_single_tool,
    test_multi_tool,
    test_parallel_calls,
    test_multi_step,
    test_tool_count_scaling,
    test_voxel_tools,
    test_voxel_tools_text,
)

console = Console()

# Registry of all available tests (7 core tests)
ALL_TESTS: dict[str, TestFunction] = {
    "single_tool": test_single_tool.run,
    "multi_tool": test_multi_tool.run,
    "parallel_calls": test_parallel_calls.run,
    "multi_step": test_multi_step.run,
    "tool_count_scaling": test_tool_count_scaling.run,
    "voxel_tools": test_voxel_tools.run,
    "voxel_tools_text": test_voxel_tools_text.run,
}

# Lookup for flag combos by label
FLAG_COMBO_LOOKUP: dict[str, FlagCombo] = {fc.label: fc for fc in ALL_FLAG_COMBOS}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ollama Tool Calling Research — Test Runner",
    )
    parser.add_argument(
        "--models",
        type=str,
        default=None,
        help="Comma-separated list of model names, or group shorthand: ga/gb/gc/gd/all (default: ga).",
    )
    parser.add_argument(
        "--tests",
        type=str,
        default=None,
        help="Comma-separated list of test names (default: all tests).",
    )
    parser.add_argument(
        "--flags",
        type=str,
        default=None,
        help="Comma-separated list of flag combos: S0T0,S0T1,S1T0,S1T1 (default: all 4).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    # Resolve models
    GROUP_LOOKUP: dict[str, list[str]] = {
        "ga": GA_MODELS, "gb": GB_MODELS, "gc": GC_MODELS, "gd": GD_MODELS,
        "all": ALL_MODELS,
    }
    if args.models is None:
        models = GA_MODELS
    elif args.models.strip().lower() in GROUP_LOOKUP:
        models = GROUP_LOOKUP[args.models.strip().lower()]
    else:
        models = [m.strip() for m in args.models.split(",") if m.strip()]

    # Resolve tests
    if args.tests is None:
        selected_tests = ALL_TESTS
    else:
        test_names = [t.strip() for t in args.tests.split(",") if t.strip()]
        selected_tests = {}
        for name in test_names:
            if name in ALL_TESTS:
                selected_tests[name] = ALL_TESTS[name]
            else:
                console.print(f"[yellow]Warning: Unknown test '{name}', skipping[/yellow]")
        if not selected_tests:
            console.print("[red]No valid tests selected.[/red]")
            return 1

    # Resolve flag combos
    if args.flags is None:
        flag_combos = ALL_FLAG_COMBOS
    else:
        flag_labels = [f.strip().upper() for f in args.flags.split(",") if f.strip()]
        flag_combos = []
        for label in flag_labels:
            if label in FLAG_COMBO_LOOKUP:
                flag_combos.append(FLAG_COMBO_LOOKUP[label])
            else:
                console.print(f"[yellow]Warning: Unknown flag combo '{label}', skipping[/yellow]")
        if not flag_combos:
            console.print("[red]No valid flag combos selected.[/red]")
            return 1

    # Print header
    console.rule("[bold green]Ollama Tool Calling Research[/bold green]")
    console.print(f"[bold]Models:[/bold] {', '.join(models)}")
    console.print(f"[bold]Tests:[/bold] {', '.join(selected_tests.keys())}")
    combo_labels = ", ".join(fc.label for fc in flag_combos)
    console.print(f"[bold]Flags:[/bold] {combo_labels}")
    total = len(models) * len(selected_tests) * len(flag_combos)
    console.print(f"[bold]Total runs:[/bold] {total}")
    console.print()

    # Run tests
    results = run_tests(selected_tests, models, flag_combos)

    # Print summary
    test_names_list = list(selected_tests.keys())
    print_summary_table(results, models, test_names_list, flag_combos)

    # Save summary
    save_summary(results, models, test_names_list, flag_combos)

    # Return exit code based on results
    failed = sum(
        1 for r in results
        if not r.passed and not (r.error and "not available" in (r.error or ""))
    )
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
