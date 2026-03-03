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
- `ollama_client.py` — Thin wrapper around Ollama SDK. Every call logs raw request+response JSON to `observations/raw/`. Includes retry with exponential backoff (3 attempts, 2/4/8s) for transient server errors (500/503/-1). Module-level singleton client built from `.env`.
- `tool_parser_native.py` — Parses `response.message.tool_calls` into `ToolCall` dataclass. Includes `validate_arguments()` for schema checking.
- `tool_parser_text.py` — Fallback parser for text-based tool calls. Tries XML `<tool_call>` tags, markdown code blocks, then raw JSON detection. Exposes `parse_text_from_string()` for use by response_layers.
- `response_layers.py` — Layer-aware response extraction. `extract_layers()` checks all three layers (native tool_calls, content text, thinking text) and classifies as "native"/"text"/"misrouted"/"none". Central abstraction replacing the manual parse_native→parse_text dance.
- `stream_collector.py` — Collects streaming chunks into a `PseudoResponse` compatible with `extract_layers()`. Handles content, tool_calls, and thinking.
- `test_runner.py` — Orchestrator: triple loop (models × tests × flag_combos), handles errors gracefully, outputs rich summary tables per flag combo plus comparison table, saves markdown reports.

### Tests (tests/)
- `config.py` — Model lists (GA/GB/GC/GD, 32 total), tool definitions, `generate_dummy_tools(n)`, `build_text_tool_system_prompt()`, `FlagCombo` dataclass, `ALL_FLAG_COMBOS`.
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
- `run_all.py` — `--models` (comma-separated or group shorthand: ga/gb/gc/gd/all), `--tests`, and `--flags` (e.g. `S0T0,S1T0`). Defaults to GA models and all 4 flag combos.

## Key Commands
```bash
# Run all tests against GA models (default, all 4 flag combos)
python run_all.py

# Run specific group
python run_all.py --models gb

# Run baseline only against one model (7 runs)
python run_all.py --models cogito-2.1:671b --flags S0T0

# Run all 4 combos against one model (28 runs)
python run_all.py --models cogito-2.1:671b

# Run specific tests against specific models
python run_all.py --models gpt-oss:20b,ministral-3:8b --tests single_tool,multi_tool

# Run all tests against all 32 models
python run_all.py --models all

# Generate subcheck tables from sweep results
python scripts/generate_subcheck_tables.py

# Refresh model library from cloud
python fetch_model_library.py
```

## Key Patterns
- All tests use `temperature=0`, `seed=42` for reproducibility; `num_ctx` uses each model's default (not hardcoded). `stream` and `think` vary per flag combo
- Every API call saves raw JSON to `observations/raw/{model}_{test}_{timestamp}.json`
- Tests catch all exceptions — model crashes are logged, not propagated
- `extract_layers()` checks native → content text → thinking text, classifying as native/text/misrouted/none
- `build_text_tool_system_prompt()` uses `$TOOL_DESCRIPTIONS` placeholder (not `str.format()`) to avoid JSON brace conflicts
- `think=True` when flags.think is True, `think=None` otherwise (not False)
- Transient errors (500/503/-1) are retried 3 times with exponential backoff (2s, 4s, 8s) before failing

### Analysis Scripts (scripts/)
- `generate_subcheck_tables.py` — Parses `g{a,b,c,d}_v4_flagmatrix.md` sweep files, generates expanded sub-check tables with P/F/T values. Outputs per-flag-combo tables and cumulative comparison to `v4_subcheck_tables.md`.

## Model Groups (behavior-based, from model_groups.md)
32 models grouped by native (40 checks) vs text (20 checks) layer pass patterns:
- **GA: All P (60/60)** — 10 models: ministral-3:3b/8b/14b, devstral-2:123b, gemini-3-flash-preview, cogito-2.1:671b, kimi-k2.5, kimi-k2-thinking, minimax-m2, kimi-k2:1t
- **GB: All native P, text varies** — 8 models: minimax-m2.1/m2.5, glm-4.6/4.7/5, nemotron-3-nano:30b, qwen3-coder-next, qwen3-coder:480b
- **GC: All text P, native varies** — 8 models: qwen3-vl:235b-instruct/235b, devstral-small-2:24b, mistral-large-3:675b, gpt-oss:120b, gemma3:4b/12b/27b
- **GD: Remaining (both layers have F)** — 6 models: qwen3-next:80b, rnj-1:8b, qwen3.5:397b, gpt-oss:20b, deepseek-v3.1:671b, deepseek-v3.2

## Model Config
- 32 models total from Ollama Cloud (29 with tools, 3 gemma3 without)
- GA (10 models): all P on v3 sweep — perfect baseline group
- GB (8 models): native perfect, text has confirmed failures
- GC (8 models): text perfect, native has confirmed failures
- GD (6 models): both layers have confirmed failures
- Model names must match `model-library.json` exactly (fetched from `/api/tags`)

## Sweep Results
### v4 (current, GA/GB/GC/GD groups, with retry)
- GA: 10 models, 280 runs — `observations/summaries/ga_v4_flagmatrix.md`
- GB: 8 models, 224 runs — `observations/summaries/gb_v4_flagmatrix.md`
- GC: 8 models, 224 runs — `observations/summaries/gc_v4_flagmatrix.md`
- GD: 6 models, 168 runs — `observations/summaries/gd_v4_flagmatrix.md`
- Sub-check tables: `observations/summaries/v4_subcheck_tables.md`
- Cogito rerun (with retry): `observations/summaries/rerun_cogito-2.1-671b_full_with_retry.md`

### v3 (historical, P0/P1/P2 size-based groups, no retry)
- P0: 9 models, 252 runs — `observations/summaries/p0_v3_flagmatrix.md`
- P1: 6 models, 168 runs — `observations/summaries/p1_v3_flagmatrix.md`
- P2: 17 models, 476 runs — `observations/summaries/p2_v3_flagmatrix.md`
- Sub-check tables: `observations/summaries/v3_subcheck_tables.md`
- Model groups: `observations/summaries/model_groups.md`

### Historical
- `p0_v1_8tests.md` (8-test baseline), `p0_v2_10tests.md` (10-test pre-restructure)

## v3→v4 Key Changes
- **qwen3-vl:235b**: 20/60 (40T) → 60/60 — server fixed, now perfect
- **minimax-m2.1**: 57/60 → 60/60 — vt_zero resolved
- **cogito-2.1:671b**: 60/60 → 20/60 (40T) — server regression (503 on streaming)
- **minimax-m2**: 59/60 → 52/60 (7T) — destabilized
- **deepseek-v3.2**: 5/60 → 16/60 — text layer improved
- 22/32 models stable (within ±1)
- Transient errors are exclusively HTTP 500 and 503 (no -1 seen)
- Cogito rerun with retry: 13/28 → 19/28 — stream=false recovers, stream=true still 503

## Important Notes
- This connects to Ollama Cloud API (not local). Requires `OLLAMA_API_KEY` in `.env`.
- `observations/raw/` is gitignored — raw data is large and regenerable
- `observations/summaries/` is tracked — these are the research deliverables
- P/F/T scoring: P=pass, F=model failure, T=transient server error (500/503)
- Voxel tests have 5 sub-checks each: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Total checks per model: 5 single tests + 5 voxel sub-checks + 5 voxel_text sub-checks = 15 per flag combo, 60 across all 4 combos
- Retry logic: 3 attempts with exponential backoff (2/4/8s) on ResponseError 500/503/-1

## num_ctx Analysis (v3/v4 sweeps used num_ctx=4096)
- v3/v4 sweeps ran with `num_ctx=4096` hardcoded. Changed to model default for future runs.
- **No truncation observed:** 0/4338 non-streaming responses had `done_reason="length"`. All were `"stop"`.
- **Streaming blind spot:** 47% of raw logs (3831 files) saved generator objects, not serialized responses. `stream_collector.py` does not capture `done_reason`/`eval_count` from final streaming chunk. Streaming responses should produce identical token counts (same deterministic settings), so non-streaming data is representative.
- **Cloud may ignore num_ctx:** One response hit 4296 total tokens (over 4096) with `done_reason="stop"`.
- **Token usage:** Median ~450 tokens. Only 25 responses exceeded 2000 tokens. Top consumers are deepseek-v3.1 think=True (up to 3874 eval tokens of thinking).
- **Thinking derailment, not truncation:** deepseek-v3.1 think=True failures are caused by massive thinking (up to 13K chars) that derails the model from the task or produces tool calls in unparseable internal token format (`<｜tool▁calls▁begin｜>`) inside thinking text. 10 responses had tool calls in deepseek special tokens that our text parser cannot extract.
- **Ollama response metrics available on non-streaming:** `done_reason`, `total_duration`, `prompt_eval_count`, `eval_count` (100% present). `load_duration`, `prompt_eval_duration`, `eval_duration`, `logprobs` always None on cloud.
