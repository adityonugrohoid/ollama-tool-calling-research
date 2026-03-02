"""Test 3: Parallel tool calls.

Question requiring 2+ simultaneous tool calls.
Provides get_weather, get_temperature, get_population — asks about
weather AND population of a city to force parallel calls.
Verifies:
- Multiple tool calls returned in a single response
- All expected tools are called
- Arguments are valid for each
"""

from src.ollama_client import chat
from src.tool_parser_native import validate_arguments
from src.response_layers import extract_layers
from src.stream_collector import collect_streaming_response
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, PARALLEL_TOOLS, FlagCombo


TEST_NAME = "parallel_calls"

PROMPT = "What is the weather in London and also what is the population of London?"


def run(model: str, flags: FlagCombo) -> TestResult:
    """Run parallel tool call test against a model."""
    messages = [{"role": "user", "content": PROMPT}]

    response_raw = chat(
        model=model,
        messages=messages,
        test_name=TEST_NAME,
        tools=PARALLEL_TOOLS,
        stream=flags.stream,
        options=DEFAULT_OPTIONS,
        think=True if flags.think else None,
    )

    if flags.stream:
        response = collect_streaming_response(response_raw)
    else:
        response = response_raw

    layers = extract_layers(response)

    if not layers.has_tool_calls:
        return TestResult(
            model=model,
            test_name=TEST_NAME,
            passed=False,
            native_or_text=layers.classification,
            parse_success=False,
            stream=flags.stream,
            think=flags.think,
            classification=layers.classification,
            notes="No tool calls found",
        )

    tool_calls = layers.best_tool_calls
    notes_parts: list[str] = []
    tool_names = [tc.name for tc in tool_calls]

    # Should have at least 2 tool calls
    has_multiple = len(tool_calls) >= 2
    if not has_multiple:
        notes_parts.append(f"Expected 2+ tool calls, got {len(tool_calls)}")

    # Check that we got calls to different tools
    unique_tools = set(tool_names)
    has_diversity = len(unique_tools) >= 2
    if not has_diversity:
        notes_parts.append(f"All calls to same tool: {unique_tools}")

    # Validate each tool call
    tool_lookup = {t["function"]["name"]: t["function"] for t in PARALLEL_TOOLS}
    all_valid = True
    for tc in tool_calls:
        if tc.name in tool_lookup:
            is_valid, issues = validate_arguments(tc, tool_lookup[tc.name])
            if not is_valid:
                all_valid = False
                notes_parts.append(f"{tc.name} schema issues: {issues}")

    passed = has_multiple and all_valid

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=layers.classification,
        parse_success=True,
        stream=flags.stream,
        think=flags.think,
        classification=layers.classification,
        notes="; ".join(notes_parts) if notes_parts else f"Tools called: {tool_names}",
        details={
            "num_tool_calls": len(tool_calls),
            "tool_names": tool_names,
            "source": tool_calls[0].source if tool_calls else "none",
            "classification": layers.classification,
        },
    )
