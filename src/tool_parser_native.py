"""Parse native tool_calls from Ollama SDK response into standardized ToolCall dataclass."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolCall:
    """Standardized tool call representation used across native and text parsers."""
    name: str
    arguments: dict[str, Any]
    source: str = "native"  # "native" or "text"


@dataclass
class ParseResult:
    """Result of attempting to parse tool calls from a response."""
    success: bool
    tool_calls: list[ToolCall] = field(default_factory=list)
    format_type: str = "none"  # "native", "text", "none"
    error: str | None = None
    raw_content: str = ""


def parse_native(response: Any) -> ParseResult:
    """Parse tool_calls from an Ollama SDK response object.

    Handles the response.message.tool_calls structure returned by the SDK.

    Args:
        response: Raw Ollama SDK chat response.

    Returns:
        ParseResult with extracted tool calls or error info.
    """
    try:
        message = response.message if hasattr(response, "message") else response.get("message", {})
    except (AttributeError, TypeError):
        return ParseResult(
            success=False,
            format_type="none",
            error="Response has no message field",
        )

    # Get content for raw logging
    if hasattr(message, "content"):
        raw_content = message.content or ""
    elif isinstance(message, dict):
        raw_content = message.get("content", "") or ""
    else:
        raw_content = ""

    # Extract tool_calls
    if hasattr(message, "tool_calls"):
        tool_calls_raw = message.tool_calls
    elif isinstance(message, dict):
        tool_calls_raw = message.get("tool_calls")
    else:
        tool_calls_raw = None

    if not tool_calls_raw:
        return ParseResult(
            success=False,
            format_type="none",
            error="No tool_calls in response",
            raw_content=raw_content,
        )

    tool_calls: list[ToolCall] = []
    for tc in tool_calls_raw:
        try:
            # SDK returns objects with .function.name and .function.arguments
            if hasattr(tc, "function"):
                func = tc.function
                name = func.name if hasattr(func, "name") else func.get("name", "")
                args = func.arguments if hasattr(func, "arguments") else func.get("arguments", {})
            elif isinstance(tc, dict):
                func = tc.get("function", {})
                name = func.get("name", "")
                args = func.get("arguments", {})
            else:
                continue

            if isinstance(args, str):
                import json
                args = json.loads(args)

            tool_calls.append(ToolCall(name=name, arguments=args, source="native"))
        except Exception as e:
            return ParseResult(
                success=False,
                format_type="native",
                error=f"Failed to parse tool call: {e}",
                raw_content=raw_content,
            )

    return ParseResult(
        success=len(tool_calls) > 0,
        tool_calls=tool_calls,
        format_type="native",
        raw_content=raw_content,
    )


def validate_arguments(
    tool_call: ToolCall,
    schema: dict[str, Any],
) -> tuple[bool, list[str]]:
    """Validate tool call arguments against the provided schema.

    Returns (is_valid, list_of_issues).
    """
    issues: list[str] = []
    properties = schema.get("parameters", {}).get("properties", {})
    required = schema.get("parameters", {}).get("required", [])

    # Check for missing required arguments
    for req in required:
        if req not in tool_call.arguments:
            issues.append(f"Missing required argument: {req}")

    # Check for hallucinated (extra) arguments
    for arg_name in tool_call.arguments:
        if arg_name not in properties:
            issues.append(f"Hallucinated argument: {arg_name}")

    # Check types where possible
    for arg_name, arg_value in tool_call.arguments.items():
        if arg_name in properties:
            prop_schema = properties[arg_name]
            expected_type = prop_schema.get("type")
            if expected_type == "string" and not isinstance(arg_value, str):
                issues.append(f"Wrong type for {arg_name}: expected string, got {type(arg_value).__name__}")
            elif expected_type == "number" and not isinstance(arg_value, (int, float)):
                issues.append(f"Wrong type for {arg_name}: expected number, got {type(arg_value).__name__}")
            elif expected_type == "integer" and not isinstance(arg_value, int):
                issues.append(f"Wrong type for {arg_name}: expected integer, got {type(arg_value).__name__}")
            elif expected_type == "boolean" and not isinstance(arg_value, bool):
                issues.append(f"Wrong type for {arg_name}: expected boolean, got {type(arg_value).__name__}")

            # Enum validation
            if "enum" in prop_schema and arg_value not in prop_schema["enum"]:
                issues.append(
                    f"Invalid enum value for {arg_name}: {arg_value!r} not in {prop_schema['enum']}"
                )

            # Minimum/maximum validation (only for numeric types)
            if isinstance(arg_value, (int, float)) and not isinstance(arg_value, bool):
                if "minimum" in prop_schema and arg_value < prop_schema["minimum"]:
                    issues.append(
                        f"Value too low for {arg_name}: {arg_value} < minimum {prop_schema['minimum']}"
                    )
                if "maximum" in prop_schema and arg_value > prop_schema["maximum"]:
                    issues.append(
                        f"Value too high for {arg_name}: {arg_value} > maximum {prop_schema['maximum']}"
                    )

    return len(issues) == 0, issues
