"""Thin wrapper around the Ollama Python SDK.

Handles both local and cloud connections via .env config.
Every call logs the raw request and full raw response JSON to observations/raw/.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from ollama import Client

load_dotenv()

RAW_DIR = Path(__file__).parent.parent / "observations" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def _build_client() -> Client:
    """Build an Ollama Client from environment variables."""
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    api_key = os.getenv("OLLAMA_API_KEY")

    kwargs: dict[str, Any] = {"host": host}
    if api_key:
        kwargs["headers"] = {"Authorization": f"Bearer {api_key}"}

    return Client(**kwargs)


# Module-level singleton
client = _build_client()


def _serialize(obj: Any) -> Any:
    """Make Ollama SDK response objects JSON-serializable."""
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if hasattr(obj, "__dict__"):
        return {k: _serialize(v) for k, v in obj.__dict__.items()}
    if isinstance(obj, list):
        return [_serialize(i) for i in obj]
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    return obj


def _save_raw(
    model: str,
    test_name: str,
    request_payload: dict[str, Any],
    response_data: Any,
) -> Path:
    """Save raw request + response JSON to observations/raw/."""
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    # Sanitize model name for filename (replace : and / with -)
    safe_model = model.replace(":", "-").replace("/", "-")
    filename = f"{safe_model}_{test_name}_{ts}.json"
    filepath = RAW_DIR / filename

    payload = {
        "timestamp": ts,
        "model": model,
        "test_name": test_name,
        "request": request_payload,
        "response": _serialize(response_data),
    }

    filepath.write_text(json.dumps(payload, indent=2, default=str))
    return filepath


def chat(
    model: str,
    messages: list[dict[str, Any]],
    test_name: str = "unknown",
    tools: list[dict[str, Any]] | None = None,
    stream: bool = False,
    options: dict[str, Any] | None = None,
    think: bool | None = None,
) -> Any:
    """Send a chat request and log the raw request/response.

    Returns the raw Ollama SDK response object.
    """
    # Build request payload for logging
    request_payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": stream,
    }

    # Build kwargs for the SDK call
    kwargs: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": stream,
    }

    if tools:
        kwargs["tools"] = tools
        request_payload["tools"] = tools

    if options:
        kwargs["options"] = options
        request_payload["options"] = options

    if think is not None:
        kwargs["think"] = think
        request_payload["think"] = think

    response = client.chat(**kwargs)

    _save_raw(model, test_name, request_payload, response)

    return response


def list_models() -> list[str]:
    """List available models on the connected Ollama instance."""
    try:
        result = client.list()
        return [m.model for m in result.models]
    except Exception:
        return []


def is_model_available(model: str) -> bool:
    """Check if a model is available (either locally or on cloud)."""
    try:
        available = list_models()
        # Check exact match or prefix match (e.g. "qwen3:8b" matches "qwen3:8b")
        return any(model == m or m.startswith(model) for m in available)
    except Exception:
        return False
