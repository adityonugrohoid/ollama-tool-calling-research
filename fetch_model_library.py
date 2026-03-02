#!/usr/bin/env python3
"""
Fetch all available models from Ollama Cloud API and build a model library JSON.

Usage:
    python fetch_model_library.py

Requires:
    - OLLAMA_API_KEY environment variable or .env file
    - pip install requests python-dotenv
"""

import json
import os
import time
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OLLAMA_API_KEY")
HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

OUTPUT_FILE = "model-library.json"


def fetch_tags():
    """GET /api/tags — list all available models."""
    print("Fetching model list from /api/tags...")
    resp = requests.get(f"{HOST}/api/tags", headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    models = data.get("models", [])
    print(f"  Found {len(models)} models\n")
    return models


def fetch_show(model_name: str):
    """POST /api/show — get model details (template, parameters, license, etc.)."""
    resp = requests.post(
        f"{HOST}/api/show",
        headers=HEADERS,
        json={"model": model_name}
    )

    if resp.status_code == 200:
        return resp.json()
    else:
        return {
            "error": resp.status_code,
            "message": resp.text.strip()
        }


def format_size(size_bytes: int) -> str:
    """Convert bytes to human-readable size."""
    if size_bytes == 0:
        return "unknown"
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(size_bytes) < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"


def build_library():
    models = fetch_tags()

    library = {
        "metadata": {
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "host": HOST,
            "total_models": len(models)
        },
        "models": {}
    }

    for i, model in enumerate(models):
        name = model["name"]
        print(f"[{i+1}/{len(models)}] Fetching details for: {name}")

        show_data = fetch_show(name)

        entry = {
            # From /api/tags
            "name": name,
            "model": model.get("model", name),
            "modified_at": model.get("modified_at", ""),
            "size_bytes": model.get("size", 0),
            "size_human": format_size(model.get("size", 0)),
            "digest": model.get("digest", ""),
            "tags_details": model.get("details", {}),
        }

        # From /api/show
        if "error" not in show_data:
            entry["show"] = {
                "modelfile": show_data.get("modelfile", ""),
                "template": show_data.get("template", ""),
                "parameters": show_data.get("parameters", ""),
                "system": show_data.get("system", ""),
                "license": show_data.get("license", ""),
                "details": show_data.get("details", {}),
                "model_info": show_data.get("model_info", {}),
                "capabilities": show_data.get("capabilities", []),
            }
        else:
            entry["show"] = {
                "error": show_data["error"],
                "message": show_data["message"]
            }

        library["models"][name] = entry

        # Small delay to avoid rate limiting
        time.sleep(0.3)

    return library


def main():
    if not API_KEY:
        print("ERROR: OLLAMA_API_KEY not set. Create a .env file or export it.")
        return

    print(f"Host: {HOST}")
    print(f"API Key: {API_KEY[:8]}...{API_KEY[-4:]}\n")

    library = build_library()

    with open(OUTPUT_FILE, "w") as f:
        json.dump(library, f, indent=2, ensure_ascii=False)

    print(f"\nDone! Saved {len(library['models'])} models to {OUTPUT_FILE}")

    # Print summary table
    print(f"\n{'Model':<35} {'Size':>12} {'Show':>8} {'Capabilities'}")
    print("-" * 85)
    for name, entry in library["models"].items():
        size = entry["size_human"]
        show_status = "✅" if "error" not in entry["show"] else f"❌ {entry['show']['error']}"
        caps = ", ".join(entry["show"].get("capabilities", [])) if "error" not in entry["show"] else "-"
        print(f"{name:<35} {size:>12} {show_status:>8} {caps}")


if __name__ == "__main__":
    main()
