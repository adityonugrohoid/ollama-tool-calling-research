"""Test 4: Multi-step tool calling loop (5 turns).

Runs a 5-turn tool calling conversation. Each turn:
1. Send user message (or tool result)
2. Get model response
3. Log the classification (native/text/misrouted/none)
4. Feed simulated tool result back

THIS IS KEY — detects mid-conversation format switching.
"""

from src.ollama_client import chat
from src.response_layers import extract_layers
from src.stream_collector import collect_streaming_response
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, TOOL_GET_WEATHER, FlagCombo


TEST_NAME = "multi_step"

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


def run(model: str, flags: FlagCombo) -> TestResult:
    """Run 5-turn multi-step tool calling test."""
    tools = [TOOL_GET_WEATHER]
    messages: list[dict] = []
    turn_formats: list[str] = []  # Track classification per turn
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
        response_raw = chat(
            model=model,
            messages=messages,
            test_name=f"{TEST_NAME}_turn{turn_idx + 1}",
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
        tool_calls = layers.best_tool_calls

        turn_formats.append(layers.classification)
        turn_details.append({
            "turn": turn_idx + 1,
            "city": city,
            "classification": layers.classification,
            "num_tool_calls": len(tool_calls),
            "tool_names": [tc.name for tc in tool_calls],
            "content_preview": layers.content[:200] if layers.content else "",
        })

        # Add assistant message to conversation
        assistant_msg: dict = {"role": "assistant", "content": layers.content or ""}
        if layers.classification == "native" and layers.tool_calls:
            assistant_msg["tool_calls"] = [
                {"function": {"name": tc.name, "arguments": tc.arguments}}
                for tc in layers.tool_calls
            ]
        messages.append(assistant_msg)

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

    # Check for format switching (ignore "none" turns)
    active_formats = set(f for f in turn_formats if f != "none")
    format_switched = len(active_formats) > 1

    if format_switched:
        notes_parts.append(f"FORMAT SWITCH DETECTED: {turn_formats}")
        native_or_text = "mixed"
    elif "native" in active_formats:
        native_or_text = "native"
    elif "text" in active_formats:
        native_or_text = "text"
    elif "misrouted" in active_formats:
        native_or_text = "misrouted"
    else:
        native_or_text = "none"
        notes_parts.append("No tool calls in any turn")

    # Count successful turns
    successful_turns = sum(1 for f in turn_formats if f != "none")
    notes_parts.append(f"Successful turns: {successful_turns}/5")
    notes_parts.append(f"Turn formats: {turn_formats}")

    # Overall classification: most common active format
    classification = native_or_text if native_or_text != "mixed" else "mixed"

    # A model passes if all 5 turns produce tool calls and format is consistent
    passed = successful_turns == 5 and not format_switched

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=native_or_text,
        parse_success=successful_turns > 0,
        stream=flags.stream,
        think=flags.think,
        classification=classification,
        notes="; ".join(notes_parts),
        details={
            "turn_formats": turn_formats,
            "format_switched": format_switched,
            "successful_turns": successful_turns,
            "turns": turn_details,
        },
    )
