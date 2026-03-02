"""Test 4: Multi-step tool calling loop (5 turns).

Runs a 5-turn tool calling conversation. Each turn:
1. Send user message (or tool result)
2. Get model response
3. Log whether the response used native or text format
4. Feed simulated tool result back

THIS IS KEY — detects mid-conversation format switching.
"""

from src.ollama_client import chat
from src.tool_parser_native import parse_native
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, TOOL_GET_WEATHER


TEST_NAME = "test_multi_step"

# 5 cities to query across turns
CITIES = ["Tokyo", "Paris", "New York", "London", "Sydney"]

# Simulated weather responses
FAKE_WEATHER = {
    "Tokyo": "Sunny, 24°C",
    "Paris": "Cloudy, 18°C",
    "New York": "Rainy, 15°C",
    "London": "Foggy, 12°C",
    "Sydney": "Clear, 28°C",
}


def run(model: str) -> TestResult:
    """Run 5-turn multi-step tool calling test."""
    tools = [TOOL_GET_WEATHER]
    messages: list[dict] = []
    turn_formats: list[str] = []  # Track format per turn
    turn_details: list[dict] = []

    for turn_idx, city in enumerate(CITIES):
        # User asks about weather in this city
        if turn_idx == 0:
            messages.append({
                "role": "user",
                "content": f"What is the weather in {city}?",
            })
        else:
            messages.append({
                "role": "user",
                "content": f"Now tell me the weather in {city}.",
            })

        # Get model response
        response = chat(
            model=model,
            messages=messages,
            test_name=f"{TEST_NAME}_turn{turn_idx + 1}",
            tools=tools,
            stream=False,
            options=DEFAULT_OPTIONS,
        )

        # Try native parsing
        native_result = parse_native(response)
        text_result = parse_text(response)

        if native_result.success:
            fmt = "native"
            tool_calls = native_result.tool_calls
        elif text_result.success:
            fmt = "text"
            tool_calls = text_result.tool_calls
        else:
            fmt = "none"
            tool_calls = []

        turn_formats.append(fmt)
        turn_details.append({
            "turn": turn_idx + 1,
            "city": city,
            "format": fmt,
            "num_tool_calls": len(tool_calls),
            "tool_names": [tc.name for tc in tool_calls],
            "raw_content_preview": (native_result.raw_content or text_result.raw_content or "")[:200],
        })

        # Add assistant message to conversation
        if hasattr(response, "message"):
            msg = response.message
            assistant_msg: dict = {"role": "assistant"}
            if hasattr(msg, "content") and msg.content:
                assistant_msg["content"] = msg.content
            else:
                assistant_msg["content"] = ""
            if native_result.success and hasattr(msg, "tool_calls") and msg.tool_calls:
                assistant_msg["tool_calls"] = [
                    {"function": {"name": tc.name, "arguments": tc.arguments}}
                    for tc in tool_calls
                ]
            messages.append(assistant_msg)
        else:
            messages.append({"role": "assistant", "content": ""})

        # Feed tool result back (if tool was called)
        if tool_calls:
            for tc in tool_calls:
                tool_result = FAKE_WEATHER.get(city, f"Weather data for {city}")
                messages.append({
                    "role": "tool",
                    "tool_name": tc.name,
                    "content": tool_result,
                })

    # Analyze results
    notes_parts: list[str] = []

    # Check for format switching
    unique_formats = set(f for f in turn_formats if f != "none")
    format_switched = len(unique_formats) > 1

    if format_switched:
        notes_parts.append(f"FORMAT SWITCH DETECTED: {turn_formats}")
        native_or_text = "mixed"
    elif "native" in unique_formats:
        native_or_text = "native"
    elif "text" in unique_formats:
        native_or_text = "text"
    else:
        native_or_text = "none"
        notes_parts.append("No tool calls in any turn")

    # Count successful turns
    successful_turns = sum(1 for f in turn_formats if f != "none")
    notes_parts.append(f"Successful turns: {successful_turns}/5")
    notes_parts.append(f"Turn formats: {turn_formats}")

    # A model passes if all 5 turns produce tool calls and format is consistent
    passed = successful_turns == 5 and not format_switched

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=native_or_text,
        parse_success=successful_turns > 0,
        notes="; ".join(notes_parts),
        details={
            "turn_formats": turn_formats,
            "format_switched": format_switched,
            "successful_turns": successful_turns,
            "turns": turn_details,
        },
    )
