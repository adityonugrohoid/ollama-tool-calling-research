"""Test 5: Tool count scaling (1, 3, 5, 8, 10, 15 tools).

Same prompt but with increasing numbers of tool definitions.
Logs classification and parse success at each count.
Detects the threshold where models switch from native to text output.
"""

from src.ollama_client import chat
from src.response_layers import extract_layers
from src.stream_collector import collect_streaming_response
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, generate_dummy_tools, FlagCombo


TEST_NAME = "tool_count_scaling"

PROMPT = "What is the current weather in Tokyo?"

TOOL_COUNTS = [1, 3, 5, 8, 10, 15]


def run(model: str, flags: FlagCombo) -> TestResult:
    """Run tool count scaling test across multiple tool counts."""
    messages = [{"role": "user", "content": PROMPT}]

    scale_results: list[dict] = []
    notes_parts: list[str] = []
    classifications_seen: list[str] = []
    all_parsed = True

    for count in TOOL_COUNTS:
        tools = generate_dummy_tools(count)

        response_raw = chat(
            model=model,
            messages=messages,
            test_name=f"{TEST_NAME}_{count}tools",
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

        if layers.has_tool_calls:
            parsed = True
        else:
            parsed = False
            all_parsed = False

        classifications_seen.append(layers.classification)

        # Check if correct tool was called (get_weather)
        correct_tool = any(tc.name == "get_weather" for tc in tool_calls) if tool_calls else False

        scale_results.append({
            "tool_count": count,
            "classification": layers.classification,
            "parse_success": parsed,
            "correct_tool": correct_tool,
            "num_calls": len(tool_calls),
            "tool_names": [tc.name for tc in tool_calls],
        })

    # Analyze scaling behavior
    active_classifications = set(c for c in classifications_seen if c != "none")
    format_switched = len(active_classifications) > 1

    if format_switched:
        # Find the switch point
        for i in range(1, len(classifications_seen)):
            if classifications_seen[i] != classifications_seen[i - 1] and classifications_seen[i] != "none":
                notes_parts.append(
                    f"FORMAT SWITCH at {TOOL_COUNTS[i]} tools: "
                    f"{classifications_seen[i - 1]} -> {classifications_seen[i]}"
                )
                break
        native_or_text = "mixed"
        classification = "mixed"
    elif "native" in active_classifications:
        native_or_text = "native"
        classification = "native"
    elif "text" in active_classifications:
        native_or_text = "text"
        classification = "text"
    elif "misrouted" in active_classifications:
        native_or_text = "misrouted"
        classification = "misrouted"
    else:
        native_or_text = "none"
        classification = "none"

    # Build scale summary
    scale_summary = " | ".join(
        f"{TOOL_COUNTS[i]}:{classifications_seen[i]}" for i in range(len(TOOL_COUNTS))
    )
    notes_parts.append(f"Scale: [{scale_summary}]")

    # Check correct tool selection at each level
    correct_at_all = all(r["correct_tool"] for r in scale_results if r["parse_success"])
    if not correct_at_all:
        wrong = [r for r in scale_results if r["parse_success"] and not r["correct_tool"]]
        notes_parts.append(f"Wrong tool at counts: {[r['tool_count'] for r in wrong]}")

    passed = all_parsed and not format_switched and correct_at_all

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=native_or_text,
        parse_success=all_parsed,
        stream=flags.stream,
        think=flags.think,
        classification=classification,
        notes="; ".join(notes_parts),
        details={
            "scale_results": scale_results,
            "format_switched": format_switched,
            "classifications_seen": classifications_seen,
        },
    )
