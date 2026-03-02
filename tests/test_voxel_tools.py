"""Test 9: Real-world voxel arena tools.

Provides 4 tools with real-world complexity: integer constraints (min/max),
enum types (12 block types), zero-parameter tools, and mixed signatures.
Answers whether tool calling mechanics hold up beyond simple string-param tools.

Sub-checks:
1. tool_selection — correct tool from 4, all 4 params valid
2. enum_adherence — block type is a valid enum value
3. integer_constraints — coords are ints within 0-15
4. zero_param_tool — calls getWorldState with empty args
5. tool_discrimination — calls removeBlock not placeBlock
"""

from src.ollama_client import chat
from src.tool_parser_native import parse_native, validate_arguments
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import (
    DEFAULT_OPTIONS,
    VOXEL_TOOLS,
    TOOL_PLACE_BLOCK,
    TOOL_REMOVE_BLOCK,
    TOOL_GET_WORLD_STATE,
)


TEST_NAME = "test_voxel_tools"

SUB_CHECKS: list[dict] = [
    {
        "name": "tool_selection",
        "prompt": "Place a stone block at position x=3, y=0, z=5.",
        "expected_tool": "placeBlock",
        "schema": TOOL_PLACE_BLOCK["function"],
        "extra_validate": lambda tc: (
            tc.arguments.get("x") == 3
            and tc.arguments.get("y") == 0
            and tc.arguments.get("z") == 5
            and tc.arguments.get("type") == "stone"
        ),
        "extra_desc": "x=3, y=0, z=5, type=stone",
    },
    {
        "name": "enum_adherence",
        "prompt": "Place a gold block at x=7, y=1, z=7.",
        "expected_tool": "placeBlock",
        "schema": TOOL_PLACE_BLOCK["function"],
        "extra_validate": lambda tc: tc.arguments.get("type") == "gold",
        "extra_desc": "type=gold (valid enum)",
    },
    {
        "name": "integer_constraints",
        "prompt": "Place a stone block at the highest point: x=15, y=15, z=15.",
        "expected_tool": "placeBlock",
        "schema": TOOL_PLACE_BLOCK["function"],
        "extra_validate": lambda tc: (
            tc.arguments.get("x") == 15
            and tc.arguments.get("y") == 15
            and tc.arguments.get("z") == 15
        ),
        "extra_desc": "x=15, y=15, z=15 (boundary values)",
    },
    {
        "name": "zero_param_tool",
        "prompt": "Check the current state of the world.",
        "expected_tool": "getWorldState",
        "schema": TOOL_GET_WORLD_STATE["function"],
        "extra_validate": lambda tc: len(tc.arguments) == 0,
        "extra_desc": "empty args",
    },
    {
        "name": "tool_discrimination",
        "prompt": "Remove the block at position x=3, y=0, z=5.",
        "expected_tool": "removeBlock",
        "schema": TOOL_REMOVE_BLOCK["function"],
        "extra_validate": lambda tc: (
            tc.arguments.get("x") == 3
            and tc.arguments.get("y") == 0
            and tc.arguments.get("z") == 5
        ),
        "extra_desc": "x=3, y=0, z=5",
    },
]


def _run_sub_check(model: str, check: dict) -> tuple[bool, str]:
    """Run a single sub-check. Returns (passed, notes)."""
    messages = [{"role": "user", "content": check["prompt"]}]

    response = chat(
        model=model,
        messages=messages,
        test_name=f"{TEST_NAME}_{check['name']}",
        tools=VOXEL_TOOLS,
        stream=False,
        options=DEFAULT_OPTIONS,
    )

    # Try native parsing first, fall back to text
    result = parse_native(response)
    if not result.success:
        result = parse_text(response)

    if not result.success:
        return False, f"no tool calls ({result.error})"

    tc = result.tool_calls[0]

    # Check correct tool name
    if tc.name != check["expected_tool"]:
        return False, f"wrong tool: {tc.name} (expected {check['expected_tool']})"

    # Validate arguments against schema
    is_valid, issues = validate_arguments(tc, check["schema"])
    if not is_valid:
        return False, f"schema issues: {issues}"

    # Extra validation specific to this sub-check
    if not check["extra_validate"](tc):
        return False, f"expected {check['extra_desc']}, got {tc.arguments}"

    return True, f"{tc.name}({tc.arguments}) via {result.format_type}"


def run(model: str) -> TestResult:
    """Run voxel tools test against a model. Pass = all 5 sub-checks pass."""
    sub_results: dict[str, tuple[bool, str]] = {}

    for check in SUB_CHECKS:
        passed, notes = _run_sub_check(model, check)
        sub_results[check["name"]] = (passed, notes)

    all_passed = all(p for p, _ in sub_results.values())
    failed_checks = [name for name, (p, _) in sub_results.items() if not p]

    if all_passed:
        notes = "All 5 sub-checks passed"
    else:
        notes = f"Failed: {', '.join(failed_checks)}"

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=all_passed,
        native_or_text="native",  # Will reflect first sub-check; details has per-check info
        parse_success=True,
        notes=notes,
        details={
            name: {"passed": p, "notes": n}
            for name, (p, n) in sub_results.items()
        },
    )
