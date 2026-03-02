"""Layer-aware response extraction.

Extracts tool calls from all layers of an Ollama response:
- message.tool_calls (native)
- message.content (text-based)
- message.thinking (misrouted)

Replaces the manual parse_native() -> parse_text() dance in every test.
"""

from dataclasses import dataclass, field
from typing import Any

from src.tool_parser_native import ParseResult, ToolCall, parse_native
from src.tool_parser_text import parse_text_from_string


@dataclass
class ResponseLayers:
    """All layers of tool call information extracted from a response."""

    tool_calls: list[ToolCall] = field(default_factory=list)
    content: str = ""
    thinking: str = ""
    content_tool_calls: list[ToolCall] = field(default_factory=list)
    thinking_tool_calls: list[ToolCall] = field(default_factory=list)
    classification: str = "none"  # "native", "text", "misrouted", "none"

    @property
    def best_tool_calls(self) -> list[ToolCall]:
        """Return first non-empty: native -> content text -> thinking text."""
        if self.tool_calls:
            return self.tool_calls
        if self.content_tool_calls:
            return self.content_tool_calls
        if self.thinking_tool_calls:
            return self.thinking_tool_calls
        return []

    @property
    def has_tool_calls(self) -> bool:
        return len(self.best_tool_calls) > 0


def extract_layers(response: Any) -> ResponseLayers:
    """Extract all response layers and classify the tool call source.

    Args:
        response: Raw Ollama SDK response (or PseudoResponse from streaming).

    Returns:
        ResponseLayers with classification and tool calls from all layers.
    """
    # 1. Extract native tool_calls
    native_result = parse_native(response)
    native_tool_calls = native_result.tool_calls if native_result.success else []

    # 2. Extract content string
    content = ""
    try:
        if hasattr(response, "message"):
            msg = response.message
            content = (msg.content if hasattr(msg, "content") else "") or ""
        elif isinstance(response, dict):
            content = response.get("message", {}).get("content", "") or ""
    except Exception:
        pass

    # 3. Extract thinking string
    thinking = ""
    try:
        if hasattr(response, "message"):
            msg = response.message
            thinking = (msg.thinking if hasattr(msg, "thinking") else "") or ""
        elif isinstance(response, dict):
            thinking = response.get("message", {}).get("thinking", "") or ""
    except Exception:
        pass

    # 4. Parse text tool calls from content
    content_tool_calls = parse_text_from_string(content) if content else []

    # 5. Parse text tool calls from thinking
    thinking_tool_calls = parse_text_from_string(thinking) if thinking else []

    # 6. Classify
    if native_tool_calls:
        classification = "native"
    elif content_tool_calls:
        classification = "text"
    elif thinking_tool_calls:
        classification = "misrouted"
    else:
        classification = "none"

    return ResponseLayers(
        tool_calls=native_tool_calls,
        content=content,
        thinking=thinking,
        content_tool_calls=content_tool_calls,
        thinking_tool_calls=thinking_tool_calls,
        classification=classification,
    )
