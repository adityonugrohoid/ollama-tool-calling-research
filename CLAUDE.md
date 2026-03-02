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
- `tool_parser_text.py` — Fallback parser for text-based tool calls. Tries XML `<tool_call>` tags, markdown code blocks, then raw JSON detection. Exposes `parse_text_from_string()` for use by response_layers.
- `response_layers.py` — Layer-aware response extraction. `extract_layers()` checks all three layers (native tool_calls, content text, thinking text) and classifies as "native"/"text"/"misrouted"/"none". Central abstraction replacing the manual parse_native→parse_text dance.
- `stream_collector.py` — Collects streaming chunks into a `PseudoResponse` compatible with `extract_layers()`. Handles content, tool_calls, and thinking.
- `test_runner.py` — Orchestrator: triple loop (models × tests × flag_combos), handles errors gracefully, outputs rich summary tables per flag combo plus comparison table, saves markdown reports.

### Tests (tests/)
- `config.py` — Model lists (P0/P1/P2, 32 total), tool definitions, `generate_dummy_tools(n)`, `build_text_tool_system_prompt()`, `FlagCombo` dataclass, `ALL_FLAG_COMBOS`.
- 7 core test scripts: `test_single_tool`, `test_multi_tool`, `test_parallel_calls`, `test_multi_step`, `test_tool_count_scaling`, `test_voxel_tools`, `test_voxel_tools_text`.
- Each test takes `(model: str, flags: FlagCombo)` and returns a `TestResult` dataclass.

### Flag Matrix
Each test runs across 4 flag combinations per model:

| | think=false | think=true |
|---|---|---|
| **stream=false** | S0T0 — baseline | S0T1 — thinking interference |
| **stream=true** | S1T0 — stream integrity | S1T1 — combined stress |

7 tests × 4 combos = **28 runs per model**.

### Entry Point
- `run_all.py` — `--models` (comma-separated or "all"), `--tests`, and `--flags` (e.g. `S0T0,S1T0`). Defaults to P0 models and all 4 flag combos.

## Key Commands
```bash
# Run all tests against P0 models (all 4 flag combos)
python run_all.py

# Run baseline only against one model (7 runs)
python run_all.py --models gpt-oss:20b --flags S0T0

# Run all 4 combos against one model (28 runs)
python run_all.py --models gpt-oss:20b

# Run specific tests against specific models
python run_all.py --models gpt-oss:20b,ministral-3:8b --tests single_tool,multi_tool

# Run all tests against all 32 models
python run_all.py --models all

# Refresh model library from cloud
python fetch_model_library.py
```

## Key Patterns
- All tests use `temperature=0`, `seed=42` for reproducibility; `stream` and `think` vary per flag combo
- Every API call saves raw JSON to `observations/raw/{model}_{test}_{timestamp}.json`
- Tests catch all exceptions — model crashes are logged, not propagated
- `extract_layers()` checks native → content text → thinking text, classifying as native/text/misrouted/none
- `build_text_tool_system_prompt()` uses `$TOOL_DESCRIPTIONS` placeholder (not `str.format()`) to avoid JSON brace conflicts
- `think=True` when flags.think is True, `think=None` otherwise (not False)

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
