"""Test 6: Tool count scaling (1, 3, 5, 8, 10, 15 tools).

Same prompt but with increasing numbers of tool definitions.
Logs format (native vs text) and parse success at each count.
Detects the threshold where models switch from native to text output.
"""

from src.ollama_client import chat
from src.tool_parser_native import parse_native
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, generate_dummy_tools


TEST_NAME = "test_tool_count_scaling"

PROMPT = "What is the current weather in Tokyo?"

TOOL_COUNTS = [1, 3, 5, 8, 10, 15]


def run(model: str) -> TestResult:
    """Run tool count scaling test across multiple tool counts."""
    messages = [{"role": "user", "content": PROMPT}]

    scale_results: list[dict] = []
    notes_parts: list[str] = []
    formats_seen: list[str] = []
    all_parsed = True

    for count in TOOL_COUNTS:
        tools = generate_dummy_tools(count)

        response = chat(
            model=model,
            messages=messages,
            test_name=f"{TEST_NAME}_{count}tools",
            tools=tools,
            stream=False,
            options=DEFAULT_OPTIONS,
        )

        # Try native first, then text
        native_result = parse_native(response)
        text_result = parse_text(response)

        if native_result.success:
            fmt = "native"
            tool_calls = native_result.tool_calls
            parsed = True
        elif text_result.success:
            fmt = "text"
            tool_calls = text_result.tool_calls
            parsed = True
        else:
            fmt = "none"
            tool_calls = []
            parsed = False
            all_parsed = False

        formats_seen.append(fmt)

        # Check if correct tool was called (get_weather)
        correct_tool = any(tc.name == "get_weather" for tc in tool_calls) if tool_calls else False

        scale_results.append({
            "tool_count": count,
            "format": fmt,
            "parse_success": parsed,
            "correct_tool": correct_tool,
            "num_calls": len(tool_calls),
            "tool_names": [tc.name for tc in tool_calls],
        })

    # Analyze scaling behavior
    unique_formats = set(f for f in formats_seen if f != "none")
    format_switched = len(unique_formats) > 1

    if format_switched:
        # Find the switch point
        for i in range(1, len(formats_seen)):
            if formats_seen[i] != formats_seen[i - 1] and formats_seen[i] != "none":
                notes_parts.append(
                    f"FORMAT SWITCH at {TOOL_COUNTS[i]} tools: "
                    f"{formats_seen[i - 1]} -> {formats_seen[i]}"
                )
                break
        native_or_text = "mixed"
    elif "native" in unique_formats:
        native_or_text = "native"
    elif "text" in unique_formats:
        native_or_text = "text"
    else:
        native_or_text = "none"

    # Build scale summary
    scale_summary = " | ".join(
        f"{TOOL_COUNTS[i]}:{formats_seen[i]}" for i in range(len(TOOL_COUNTS))
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
        notes="; ".join(notes_parts),
        details={
            "scale_results": scale_results,
            "format_switched": format_switched,
            "formats_seen": formats_seen,
        },
    )
