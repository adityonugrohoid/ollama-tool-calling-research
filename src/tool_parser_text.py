"""Parse tool calls from text content (non-native format).

Handles:
1. XML-delimited tool calls: <tool_call>...</tool_call>
2. Raw JSON detection as fallback
3. Markdown-wrapped JSON (```json ... ```)

Returns the same ToolCall dataclass as tool_parser_native.
"""

import json
import re
from typing import Any

from src.tool_parser_native import ParseResult, ToolCall


def parse_text(response: Any) -> ParseResult:
    """Parse tool calls from text content in an Ollama response.

    Tries multiple strategies in order:
    1. XML-delimited: <tool_call>{"name": ..., "arguments": ...}</tool_call>
    2. Markdown code blocks containing tool call JSON
    3. Raw JSON objects with "name" and "arguments" keys

    Args:
        response: Raw Ollama SDK chat response.

    Returns:
        ParseResult with extracted tool calls or error info.
    """
    # Extract text content
    try:
        if hasattr(response, "message"):
            message = response.message
            content = message.content if hasattr(message, "content") else ""
        elif isinstance(response, dict):
            content = response.get("message", {}).get("content", "")
        else:
            content = str(response)
    except Exception:
        content = ""

    if not content or not content.strip():
        return ParseResult(
            success=False,
            format_type="none",
            error="No text content to parse",
            raw_content=content or "",
        )

    # Strategy 1: XML-delimited tool calls
    tool_calls = _parse_xml_tool_calls(content)
    if tool_calls:
        return ParseResult(
            success=True,
            tool_calls=tool_calls,
            format_type="text",
            raw_content=content,
        )

    # Strategy 2: Markdown code blocks
    tool_calls = _parse_markdown_tool_calls(content)
    if tool_calls:
        return ParseResult(
            success=True,
            tool_calls=tool_calls,
            format_type="text",
            raw_content=content,
        )

    # Strategy 3: Raw JSON detection
    tool_calls = _parse_raw_json_tool_calls(content)
    if tool_calls:
        return ParseResult(
            success=True,
            tool_calls=tool_calls,
            format_type="text",
            raw_content=content,
        )

    return ParseResult(
        success=False,
        format_type="none",
        error="No tool calls found in text content",
        raw_content=content,
    )


def _parse_xml_tool_calls(content: str) -> list[ToolCall]:
    """Extract tool calls from <tool_call>...</tool_call> XML tags."""
    pattern = r"<tool_call>(.*?)</tool_call>"
    matches = re.findall(pattern, content, re.DOTALL)

    tool_calls: list[ToolCall] = []
    for match in matches:
        tc = _extract_tool_call_from_json(match.strip())
        if tc:
            tool_calls.append(tc)

    return tool_calls


def _parse_markdown_tool_calls(content: str) -> list[ToolCall]:
    """Extract tool calls from ```json ... ``` markdown blocks."""
    pattern = r"```(?:json)?\s*\n?(.*?)\n?```"
    matches = re.findall(pattern, content, re.DOTALL)

    tool_calls: list[ToolCall] = []
    for match in matches:
        tc = _extract_tool_call_from_json(match.strip())
        if tc:
            tool_calls.append(tc)

    return tool_calls


def _parse_raw_json_tool_calls(content: str) -> list[ToolCall]:
    """Detect and extract raw JSON tool calls from text.

    Looks for JSON objects containing "name" and "arguments" keys.
    """
    tool_calls: list[ToolCall] = []

    # Find all JSON-like objects in the text
    # Match balanced braces (simple depth tracking)
    for match in _find_json_objects(content):
        tc = _extract_tool_call_from_json(match)
        if tc:
            tool_calls.append(tc)

    return tool_calls


def _find_json_objects(text: str) -> list[str]:
    """Find potential JSON objects in text by tracking brace depth."""
    objects: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "{":
            depth = 0
            start = i
            in_string = False
            escape_next = False
            while i < len(text):
                char = text[i]
                if escape_next:
                    escape_next = False
                elif char == "\\":
                    escape_next = True
                elif char == '"' and not escape_next:
                    in_string = not in_string
                elif not in_string:
                    if char == "{":
                        depth += 1
                    elif char == "}":
                        depth -= 1
                        if depth == 0:
                            objects.append(text[start : i + 1])
                            break
                i += 1
        i += 1
    return objects


def _extract_tool_call_from_json(json_str: str) -> ToolCall | None:
    """Try to parse a JSON string as a tool call.

    Accepts formats:
    - {"name": "func", "arguments": {...}}
    - {"function": {"name": "func", "arguments": {...}}}
    """
    # Clean common issues
    json_str = json_str.strip()

    # Remove trailing commas before closing braces/brackets
    json_str = re.sub(r",\s*([}\]])", r"\1", json_str)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return None

    if not isinstance(data, dict):
        return None

    # Format 1: {"name": ..., "arguments": ...}
    if "name" in data and "arguments" in data:
        args = data["arguments"]
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except json.JSONDecodeError:
                args = {}
        return ToolCall(name=data["name"], arguments=args, source="text")

    # Format 2: {"function": {"name": ..., "arguments": ...}}
    if "function" in data and isinstance(data["function"], dict):
        func = data["function"]
        if "name" in func:
            args = func.get("arguments", {})
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except json.JSONDecodeError:
                    args = {}
            return ToolCall(name=func["name"], arguments=args, source="text")

    return None
