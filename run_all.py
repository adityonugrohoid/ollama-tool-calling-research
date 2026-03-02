#!/usr/bin/env python3
"""Entry point for running the Ollama tool calling research test suite.

Usage:
    # Run all tests against P0 models (default)
    python run_all.py

    # Run specific tests against specific models
    python run_all.py --models qwen3:8b,llama3.1:8b --tests test_single_tool,test_multi_tool

    # Run all tests against a single model
    python run_all.py --models qwen3:8b

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
from tests.config import P0_MODELS, ALL_MODELS

# Import all test modules
from tests import (
    test_single_tool,
    test_multi_tool,
    test_parallel_calls,
    test_multi_step,
    test_streaming_tools,
    test_tool_count_scaling,
    test_thinking_with_tools,
    test_text_fallback,
    test_voxel_tools,
    test_voxel_tools_text,
)

console = Console()

# Registry of all available tests
ALL_TESTS: dict[str, TestFunction] = {
    "test_single_tool": test_single_tool.run,
    "test_multi_tool": test_multi_tool.run,
    "test_parallel_calls": test_parallel_calls.run,
    "test_multi_step": test_multi_step.run,
    "test_streaming_tools": test_streaming_tools.run,
    "test_tool_count_scaling": test_tool_count_scaling.run,
    "test_thinking_with_tools": test_thinking_with_tools.run,
    "test_text_fallback": test_text_fallback.run,
    "test_voxel_tools": test_voxel_tools.run,
    "test_voxel_tools_text": test_voxel_tools_text.run,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ollama Tool Calling Research — Test Runner",
    )
    parser.add_argument(
        "--models",
        type=str,
        default=None,
        help="Comma-separated list of model names (default: P0 models). Use 'all' for all models.",
    )
    parser.add_argument(
        "--tests",
        type=str,
        default=None,
        help="Comma-separated list of test names (default: all tests).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    # Resolve models
    if args.models is None:
        models = P0_MODELS
    elif args.models.strip().lower() == "all":
        models = ALL_MODELS
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

    # Print header
    console.rule("[bold green]Ollama Tool Calling Research[/bold green]")
    console.print(f"[bold]Models:[/bold] {', '.join(models)}")
    console.print(f"[bold]Tests:[/bold] {', '.join(selected_tests.keys())}")
    console.print()

    # Run tests
    results = run_tests(selected_tests, models)

    # Print summary
    test_names_list = list(selected_tests.keys())
    print_summary_table(results, models, test_names_list)

    # Save summary
    save_summary(results, models, test_names_list)

    # Return exit code based on results
    failed = sum(
        1 for r in results
        if not r.passed and not (r.error and "not available" in (r.error or ""))
    )
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
