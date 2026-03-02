"""Test 8: Text-based tool calling baseline (no native tools param).

Uses prompt-level instructions to request tool calls in XML format
instead of the native `tools` parameter. Measures parse success rate.

This establishes a baseline for the text-based fallback strategy.
"""

from src.ollama_client import chat
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import (
    DEFAULT_OPTIONS,
    TOOL_GET_WEATHER,
    build_text_tool_system_prompt,
)


TEST_NAME = "test_text_fallback"

PROMPT = "What is the current weather in Tokyo?"

# Number of times to repeat the test for measuring parse success rate
REPETITIONS = 3


def run(model: str) -> TestResult:
    """Run text-based tool calling baseline test."""
    tools = [TOOL_GET_WEATHER]
    system_prompt = build_text_tool_system_prompt(tools)

    successes = 0
    failures = 0
    attempt_details: list[dict] = []

    for attempt in range(REPETITIONS):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": PROMPT},
        ]

        # No tools parameter — forcing text-based approach
        response = chat(
            model=model,
            messages=messages,
            test_name=f"{TEST_NAME}_attempt{attempt + 1}",
            tools=None,
            stream=False,
            options=DEFAULT_OPTIONS,
        )

        result = parse_text(response)

        if result.success:
            successes += 1
            tc = result.tool_calls[0]
            correct_tool = tc.name == "get_weather"
            attempt_details.append({
                "attempt": attempt + 1,
                "parsed": True,
                "correct_tool": correct_tool,
                "tool_name": tc.name,
                "arguments": tc.arguments,
            })
        else:
            failures += 1
            attempt_details.append({
                "attempt": attempt + 1,
                "parsed": False,
                "error": result.error,
                "raw_preview": result.raw_content[:300] if result.raw_content else "",
            })

    # Calculate success rate
    success_rate = successes / REPETITIONS
    notes_parts: list[str] = [
        f"Parse rate: {successes}/{REPETITIONS} ({success_rate:.0%})",
    ]

    # Check correct tool in successful attempts
    correct_in_successes = sum(
        1 for d in attempt_details if d.get("parsed") and d.get("correct_tool")
    )
    if successes > 0:
        notes_parts.append(f"Correct tool: {correct_in_successes}/{successes}")

    # Pass if at least 2/3 attempts parse successfully with correct tool
    passed = correct_in_successes >= 2

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text="text",
        parse_success=successes > 0,
        notes="; ".join(notes_parts),
        details={
            "successes": successes,
            "failures": failures,
            "success_rate": success_rate,
            "attempts": attempt_details,
        },
    )
