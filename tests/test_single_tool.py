"""Test 1: Single tool, single call.

Provides one tool (get_weather) and asks a question that requires it.
Verifies:
- tool_calls are present in the response
- Correct tool name is returned
- Arguments are valid against the schema
- No hallucinated parameters
"""

from src.ollama_client import chat
from src.tool_parser_native import validate_arguments
from src.response_layers import extract_layers
from src.stream_collector import collect_streaming_response
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, TOOL_GET_WEATHER, FlagCombo


TEST_NAME = "single_tool"

PROMPT = "What is the current weather in Tokyo?"


def run(model: str, flags: FlagCombo) -> TestResult:
    """Run single tool test against a model."""
    messages = [{"role": "user", "content": PROMPT}]
    tools = [TOOL_GET_WEATHER]

    response_raw = chat(
        model=model,
        messages=messages,
        test_name=TEST_NAME,
        tools=tools,
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

    # Validate the tool call
    tc = layers.best_tool_calls[0]
    notes_parts: list[str] = []

    # Check correct tool name
    name_correct = tc.name == "get_weather"
    if not name_correct:
        notes_parts.append(f"Wrong tool: {tc.name}")

    # Validate arguments against schema
    is_valid, issues = validate_arguments(tc, TOOL_GET_WEATHER["function"])
    if issues:
        notes_parts.append(f"Schema issues: {issues}")

    # Check city argument contains something reasonable
    city = tc.arguments.get("city", "")
    has_city = bool(city)
    if not has_city:
        notes_parts.append("Missing city argument")

    passed = name_correct and is_valid and has_city

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=layers.classification,
        parse_success=True,
        stream=flags.stream,
        think=flags.think,
        classification=layers.classification,
        notes="; ".join(notes_parts) if notes_parts else f"Tool: {tc.name}, City: {city}",
        details={
            "tool_name": tc.name,
            "arguments": tc.arguments,
            "source": tc.source,
            "schema_valid": is_valid,
            "schema_issues": issues,
            "classification": layers.classification,
        },
    )
