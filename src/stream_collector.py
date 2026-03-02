"""Streaming response collector.

Collects chunks from an Ollama streaming response into a PseudoResponse
object that is compatible with extract_layers().
"""

from typing import Any


class PseudoMessage:
    """Mimics an Ollama SDK message object."""

    def __init__(
        self,
        content: str,
        tool_calls: list[Any] | None,
        thinking: str = "",
    ):
        self.content = content
        self.tool_calls = tool_calls
        self.thinking = thinking


class PseudoToolCall:
    """Mimics an Ollama SDK tool call object."""

    def __init__(self, func_dict: dict):
        self.function = type(
            "Func",
            (),
            {
                "name": func_dict["function"]["name"],
                "arguments": func_dict["function"]["arguments"],
            },
        )()


class PseudoResponse:
    """Mimics an Ollama SDK response object."""

    def __init__(
        self,
        content: str,
        tool_calls_raw: list[dict],
        thinking: str = "",
    ):
        tc_objects = (
            [PseudoToolCall(tc) for tc in tool_calls_raw]
            if tool_calls_raw
            else None
        )
        self.message = PseudoMessage(content, tc_objects, thinking)


def collect_streaming_response(stream_response: Any) -> PseudoResponse:
    """Collect a streaming response into a PseudoResponse.

    Accumulates content, tool_calls, and thinking from all chunks.

    Args:
        stream_response: Iterator of streaming chunks from Ollama SDK.

    Returns:
        PseudoResponse compatible with extract_layers().
    """
    content_parts: list[str] = []
    thinking_parts: list[str] = []
    tool_calls_accumulated: list[dict] = []

    for chunk in stream_response:
        if hasattr(chunk, "message"):
            msg = chunk.message
            if hasattr(msg, "content") and msg.content:
                content_parts.append(msg.content)
            if hasattr(msg, "thinking") and msg.thinking:
                thinking_parts.append(msg.thinking)
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    if hasattr(tc, "function"):
                        func = tc.function
                        name = (
                            func.name
                            if hasattr(func, "name")
                            else func.get("name", "")
                        )
                        arguments = (
                            func.arguments
                            if hasattr(func, "arguments")
                            else func.get("arguments", {})
                        )
                        tool_calls_accumulated.append(
                            {"function": {"name": name, "arguments": arguments}}
                        )

    return PseudoResponse(
        content="".join(content_parts),
        tool_calls_raw=tool_calls_accumulated,
        thinking="".join(thinking_parts),
    )
