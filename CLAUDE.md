# CLAUDE.md — Ollama Tool Calling Research

## Overview
Research repo documenting tool calling inconsistencies across open-source LLMs served through Ollama Cloud API. Includes reproducible test scripts, per-model behavior logs, and text-based tool calling as a standardized fallback.

## Tech Stack
- Python 3.12+, venv at `.venv/`
- `ollama` SDK — cloud client with `Client(host=..., headers=...)`
- `rich` — terminal output (tables, progress)
- `pydantic` — data validation
- `python-dotenv` — .env config

## Architecture

### Core (src/)
- `ollama_client.py` — Thin wrapper around Ollama SDK. Every call logs raw request+response JSON to `observations/raw/`. Module-level singleton client built from `.env`.
- `tool_parser_native.py` — Parses `response.message.tool_calls` into `ToolCall` dataclass. Includes `validate_arguments()` for schema checking.
- `tool_parser_text.py` — Fallback parser for text-based tool calls. Tries XML `<tool_call>` tags, markdown code blocks, then raw JSON detection.
- `test_runner.py` — Orchestrator: runs test functions against model lists, handles errors gracefully, outputs rich summary tables, saves markdown reports.

### Tests (tests/)
- `config.py` — Model lists (P0/P1/P2, 32 total), tool definitions, `generate_dummy_tools(n)`, `build_text_tool_system_prompt()`.
- 9 test scripts: `test_single_tool`, `test_multi_tool`, `test_parallel_calls`, `test_multi_step`, `test_streaming_tools`, `test_tool_count_scaling`, `test_thinking_with_tools`, `test_text_fallback`, `test_voxel_tools`.
- Each test takes a model name, returns a `TestResult` dataclass.

### Entry Point
- `run_all.py` — `--models` (comma-separated or "all") and `--tests` flags. Defaults to P0 models.

## Key Commands
```bash
# Run all tests against P0 models
python run_all.py

# Run specific tests against specific models
python run_all.py --models gpt-oss:20b,ministral-3:8b --tests test_single_tool,test_multi_tool

# Run all tests against all 32 models
python run_all.py --models all

# Refresh model library from cloud
python fetch_model_library.py
```

## Key Patterns
- All tests use `temperature=0`, `seed=42`, `stream=false` for reproducibility
- Every API call saves raw JSON to `observations/raw/{model}_{test}_{timestamp}.json`
- Tests catch all exceptions — model crashes are logged, not propagated
- Native parsing tried first, text parsing as fallback
- `build_text_tool_system_prompt()` uses `$TOOL_DESCRIPTIONS` placeholder (not `str.format()`) to avoid JSON brace conflicts

## Model Config
- 32 models total from Ollama Cloud (29 with tools, 3 gemma3 without)
- P0 (9 models, <30B): fast iteration
- P1 (6 models, 30-130B): deeper investigation
- P2 (17 models, 200B+): full coverage
- Model names must match `model-library.json` exactly (fetched from `/api/tags`)

## Important Notes
- This connects to Ollama Cloud API (not local). Requires `OLLAMA_API_KEY` in `.env`.
- `observations/raw/` is gitignored — raw data is large and regenerable
- `observations/summaries/` is tracked — these are the research deliverables
- gemma3 models have NO native tool support but pass text-based fallback
- gpt-oss:20b fails parallel calls (returns 1 instead of 2+) and text fallback
