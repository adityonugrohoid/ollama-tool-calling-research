"""Test 5: Streaming vs non-streaming tool calls.

Same prompt with stream=true vs stream=false.
Verifies:
- Tool calls survive streaming mode
- Results are consistent between modes
- Streaming doesn't silently drop tool calls
"""

from src.ollama_client import chat
from src.tool_parser_native import parse_native
from src.tool_parser_text import parse_text
from src.test_runner import TestResult
from tests.config import DEFAULT_OPTIONS, TOOL_GET_WEATHER


TEST_NAME = "test_streaming_tools"

PROMPT = "What is the current weather in Berlin?"


def _collect_streaming_response(stream_response) -> dict:
    """Collect a streaming response into a single dict resembling non-streaming format.

    The Ollama SDK returns an iterator of chunks when streaming.
    We accumulate content and tool_calls from all chunks.
    """
    content_parts: list[str] = []
    tool_calls_accumulated: list[dict] = []
    last_chunk = None

    for chunk in stream_response:
        last_chunk = chunk
        if hasattr(chunk, "message"):
            msg = chunk.message
            if hasattr(msg, "content") and msg.content:
                content_parts.append(msg.content)
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    if hasattr(tc, "function"):
                        tool_calls_accumulated.append({
                            "function": {
                                "name": tc.function.name if hasattr(tc.function, "name") else tc.function.get("name", ""),
                                "arguments": tc.function.arguments if hasattr(tc.function, "arguments") else tc.function.get("arguments", {}),
                            }
                        })

    # Build a pseudo-response object
    class PseudoMessage:
        def __init__(self, content: str, tool_calls: list | None):
            self.content = content
            self.tool_calls = tool_calls

    class PseudoToolCall:
        def __init__(self, func_dict: dict):
            self.function = type("Func", (), {
                "name": func_dict["function"]["name"],
                "arguments": func_dict["function"]["arguments"],
            })()

    class PseudoResponse:
        def __init__(self, content: str, tool_calls_raw: list[dict]):
            tc_objects = [PseudoToolCall(tc) for tc in tool_calls_raw] if tool_calls_raw else None
            self.message = PseudoMessage(content, tc_objects)

    return PseudoResponse(
        content="".join(content_parts),
        tool_calls_raw=tool_calls_accumulated,
    )


def run(model: str) -> TestResult:
    """Run streaming vs non-streaming comparison."""
    messages = [{"role": "user", "content": PROMPT}]
    tools = [TOOL_GET_WEATHER]

    # Non-streaming request
    response_nostream = chat(
        model=model,
        messages=messages,
        test_name=f"{TEST_NAME}_nostream",
        tools=tools,
        stream=False,
        options=DEFAULT_OPTIONS,
    )

    native_nostream = parse_native(response_nostream)
    text_nostream = parse_text(response_nostream)
    nostream_result = native_nostream if native_nostream.success else text_nostream

    # Streaming request
    try:
        stream_raw = chat(
            model=model,
            messages=messages,
            test_name=f"{TEST_NAME}_stream",
            tools=tools,
            stream=True,
            options=DEFAULT_OPTIONS,
        )
        response_stream = _collect_streaming_response(stream_raw)

        native_stream = parse_native(response_stream)
        text_stream = parse_text(response_stream)
        stream_result = native_stream if native_stream.success else text_stream

    except Exception as e:
        stream_result = None
        stream_error = str(e)

    notes_parts: list[str] = []

    nostream_ok = nostream_result.success
    stream_ok = stream_result.success if stream_result else False

    notes_parts.append(f"Non-stream: {'OK' if nostream_ok else 'FAIL'} ({nostream_result.format_type})")

    if stream_result:
        notes_parts.append(f"Stream: {'OK' if stream_ok else 'FAIL'} ({stream_result.format_type})")
    else:
        notes_parts.append(f"Stream: ERROR ({stream_error})")

    # Compare results
    if nostream_ok and stream_ok:
        # Check if same tool was called
        ns_names = [tc.name for tc in nostream_result.tool_calls]
        s_names = [tc.name for tc in stream_result.tool_calls]
        consistent = ns_names == s_names
        if not consistent:
            notes_parts.append(f"INCONSISTENT: nostream={ns_names}, stream={s_names}")
    elif nostream_ok and not stream_ok:
        notes_parts.append("STREAMING DROPPED TOOL CALLS")
        consistent = False
    else:
        consistent = False

    passed = nostream_ok and stream_ok and consistent

    # Determine format
    if nostream_ok:
        native_or_text = nostream_result.format_type
    else:
        native_or_text = "none"

    return TestResult(
        model=model,
        test_name=TEST_NAME,
        passed=passed,
        native_or_text=native_or_text,
        parse_success=nostream_ok,
        notes="; ".join(notes_parts),
        details={
            "nostream_success": nostream_ok,
            "nostream_format": nostream_result.format_type,
            "stream_success": stream_ok,
            "stream_format": stream_result.format_type if stream_result else "error",
            "consistent": consistent if nostream_ok else None,
        },
    )
