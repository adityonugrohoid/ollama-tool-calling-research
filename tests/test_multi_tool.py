"""Test 2: Multiple tools available, question requiring one.

Provides 3 tools (get_weather, search_restaurants, book_flight).
Asks a question that should only trigger get_weather.
Verifies:
- Correct tool is selected from multiple options
- Other tools are NOT called
- Arguments are valid
"""

from src.ollama_client import chat
from src.tool_parser_native import validate_arguments
from src.response_layers import extract_layers
from src.stream_collector import collect_streaming_response
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, MULTI_TOOLS, TOOL_GET_WEATHER, FlagCombo


TEST_NAME = "multi_tool"

PROMPT = "What's the weather like in Paris right now?"


def run(model: str, flags: FlagCombo) -> TestResult:
    """Run multi-tool selection test against a model."""
    messages = [{"role": "user", "content": PROMPT}]

    response_raw = chat(
        model=model,
        messages=messages,
        test_name=TEST_NAME,
        tools=MULTI_TOOLS,
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

    notes_parts: list[str] = []
    tool_calls = layers.best_tool_calls

    # Should have exactly one tool call
    if len(tool_calls) != 1:
        notes_parts.append(f"Expected 1 tool call, got {len(tool_calls)}")

    tc = tool_calls[0]

    # Should be get_weather
    correct_tool = tc.name == "get_weather"
    if not correct_tool:
        notes_parts.append(f"Wrong tool selected: {tc.name} (expected get_weather)")

    # Validate arguments
    is_valid, issues = validate_arguments(tc, TOOL_GET_WEATHER["function"])
    if issues:
        notes_parts.append(f"Schema issues: {issues}")

    passed = correct_tool and is_valid and len(tool_calls) == 1

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=layers.classification,
        parse_success=True,
        stream=flags.stream,
        think=flags.think,
        classification=layers.classification,
        notes="; ".join(notes_parts) if notes_parts else f"Correctly selected {tc.name}",
        details={
            "num_tool_calls": len(tool_calls),
            "tool_name": tc.name,
            "arguments": tc.arguments,
            "source": tc.source,
            "available_tools": [t["function"]["name"] for t in MULTI_TOOLS],
            "classification": layers.classification,
        },
    )
