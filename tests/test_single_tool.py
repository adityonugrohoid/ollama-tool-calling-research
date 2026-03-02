"""Test 1: Single tool, single call.

Provides one tool (get_weather) and asks a question that requires it.
Verifies:
- tool_calls are present in the response
- Correct tool name is returned
- Arguments are valid against the schema
- No hallucinated parameters
"""

from src.ollama_client import chat
from src.tool_parser_native import parse_native, validate_arguments
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, TOOL_GET_WEATHER


TEST_NAME = "test_single_tool"

PROMPT = "What is the current weather in Tokyo?"


def run(model: str) -> TestResult:
    """Run single tool test against a model."""
    messages = [{"role": "user", "content": PROMPT}]
    tools = [TOOL_GET_WEATHER]

    response = chat(
        model=model,
        messages=messages,
        test_name=TEST_NAME,
        tools=tools,
        stream=False,
        options=DEFAULT_OPTIONS,
    )

    # Try native parsing first
    result = parse_native(response)

    # Fall back to text parsing
    if not result.success:
        result = parse_text(response)

    if not result.success:
        return TestResult(
            model=model,
            test_name=TEST_NAME,
            passed=False,
            native_or_text=result.format_type,
            parse_success=False,
            notes=result.error or "No tool calls found",
        )

    # Validate the tool call
    tc = result.tool_calls[0]
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
        native_or_text=result.format_type,
        parse_success=True,
        notes="; ".join(notes_parts) if notes_parts else f"Tool: {tc.name}, City: {city}",
        details={
            "tool_name": tc.name,
            "arguments": tc.arguments,
            "source": tc.source,
            "schema_valid": is_valid,
            "schema_issues": issues,
        },
    )
