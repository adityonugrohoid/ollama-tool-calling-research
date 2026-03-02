"""Test 7: Thinking mode (think=true) with tool calling.

Enable think=true while providing tools.
Verifies:
- Thinking tokens don't corrupt tool call JSON
- Tool calls are still properly structured
- Thinking content is separate from tool calls
"""

from src.ollama_client import chat
from src.tool_parser_native import parse_native, validate_arguments
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, TOOL_GET_WEATHER


TEST_NAME = "test_thinking_with_tools"

PROMPT = "What is the current weather in Tokyo?"


def run(model: str) -> TestResult:
    """Run thinking + tools test against a model."""
    messages = [{"role": "user", "content": PROMPT}]
    tools = [TOOL_GET_WEATHER]

    response = chat(
        model=model,
        messages=messages,
        test_name=TEST_NAME,
        tools=tools,
        stream=False,
        options=DEFAULT_OPTIONS,
        think=True,
    )

    notes_parts: list[str] = []

    # Check for thinking content
    has_thinking = False
    thinking_content = ""
    if hasattr(response, "message"):
        msg = response.message
        if hasattr(msg, "thinking") and msg.thinking:
            has_thinking = True
            thinking_content = msg.thinking
            notes_parts.append(f"Thinking: {len(thinking_content)} chars")

    # Try native parsing
    native_result = parse_native(response)
    text_result = parse_text(response)

    if native_result.success:
        result = native_result
    elif text_result.success:
        result = text_result
    else:
        # Check if thinking content contains tool-call-like JSON (corruption)
        if has_thinking and ("get_weather" in thinking_content or '"name"' in thinking_content):
            notes_parts.append("POSSIBLE CORRUPTION: tool call JSON found in thinking content")

        return TestResult(
            model=model,
            test_name=TEST_NAME,
            passed=False,
            native_or_text="none",
            parse_success=False,
            notes="; ".join(notes_parts) + "; " + (native_result.error or "No tool calls"),
            details={
                "has_thinking": has_thinking,
                "thinking_length": len(thinking_content),
            },
        )

    tc = result.tool_calls[0]

    # Validate tool call
    is_valid, issues = validate_arguments(tc, TOOL_GET_WEATHER["function"])
    if issues:
        notes_parts.append(f"Schema issues: {issues}")

    # Check for corruption — thinking tokens inside tool call arguments
    args_str = str(tc.arguments)
    corruption_markers = ["<think>", "</think>", "<|think|>", "**thinking**"]
    has_corruption = any(marker in args_str for marker in corruption_markers)
    if has_corruption:
        notes_parts.append("CORRUPTION: thinking markers found in tool call arguments")

    name_correct = tc.name == "get_weather"
    if not name_correct:
        notes_parts.append(f"Wrong tool: {tc.name}")

    if not notes_parts:
        notes_parts.append(f"Tool: {tc.name}, Thinking: {'yes' if has_thinking else 'no'}")

    passed = name_correct and is_valid and not has_corruption

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=result.format_type,
        parse_success=True,
        notes="; ".join(notes_parts),
        details={
            "has_thinking": has_thinking,
            "thinking_length": len(thinking_content),
            "tool_name": tc.name,
            "arguments": tc.arguments,
            "corruption_detected": has_corruption,
            "source": tc.source,
        },
    )
