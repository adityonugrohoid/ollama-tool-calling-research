# Research Methodology

## Objective

Systematically document how open-source LLMs handle native tool calling through Ollama, identifying failure modes, inconsistencies, and thresholds that affect reliability.

## Test Design Principles

### Reproducibility

Every test uses fixed parameters to ensure reproducible results:

- **temperature=0** — Eliminates randomness in output
- **seed=42** — Fixed random seed for deterministic behavior
- **num_ctx=4096** — Consistent context window across models

### Flag Matrix

Each test runs across 4 flag combinations to reveal how streaming and thinking interact with each scenario:

| | think=false | think=true |
|---|---|---|
| **stream=false** | S0T0 — baseline | S0T1 — thinking interference |
| **stream=true** | S1T0 — stream integrity | S1T1 — combined stress |

This produces **7 tests × 4 flag combos = 28 runs per model**.

### Raw Data Preservation

Every API call logs:
- The full request payload (model, messages, tools, options, stream, think)
- The full response JSON (including all metadata: timing, token counts, etc.)
- Timestamp for temporal tracking
- File path: `observations/raw/{model}_{test_name}_{timestamp}.json`

This is a research repo — raw data is the primary deliverable.

### Error Isolation

Each test catches all exceptions. A model crash, timeout, or malformed response is logged as a result, not propagated as an error. The test suite continues running other models and tests.

## Response Layer Classification

Each response is analyzed across all three layers by `extract_layers()`:

### Layer 1: Native (`message.tool_calls`)
- Tool calls appear in `response.message.tool_calls` as structured objects
- Parsed by `tool_parser_native.py`
- This is the expected behavior when the `tools` parameter is provided

### Layer 2: Content Text (`message.content`)
- Tool calls appear in `response.message.content` as text
- May use XML delimiters: `<tool_call>{"name": ..., "arguments": ...}</tool_call>`
- May use markdown code blocks: `` ```json ... ``` ``
- May be raw JSON embedded in text
- Parsed by `parse_text_from_string()`

### Layer 3: Thinking Text (`message.thinking`)
- Tool calls appear in `response.message.thinking` — only present when `think=true`
- Same parsing strategies as content text
- Indicates the model "misrouted" the tool call to its thinking layer

### Classification

`extract_layers()` returns a `ResponseLayers` object with a classification:

- **`native`** — Tool calls found in `message.tool_calls` (ideal behavior)
- **`text`** — Tool calls found in `message.content` via text parsing
- **`misrouted`** — Tool calls found only in `message.thinking` (model put tool call in wrong layer)
- **`none`** — No tool calls detected in any layer
- **`mixed`** — Used in multi-turn tests where classification changes mid-conversation

The `best_tool_calls` property returns the first non-empty layer: native → content → thinking.

## Test Suite

### 1. Single Tool (`test_single_tool.py`)
- **What:** One tool (get_weather), one question
- **Validates:** Tool calls present, correct name, valid arguments, no hallucinated params

### 2. Multi-Tool Selection (`test_multi_tool.py`)
- **What:** 3 tools available, question requiring one
- **Validates:** Correct tool selected, others not called

### 3. Parallel Calls (`test_parallel_calls.py`)
- **What:** Question requiring 2+ simultaneous tool calls
- **Validates:** Multiple tool calls returned, correct tools, valid arguments

### 4. Multi-Step Loop (`test_multi_step.py`)
- **What:** 5-turn tool calling conversation with simulated tool results
- **Validates:** Consistent format across turns, all turns produce tool calls
- **Key detection:** Mid-conversation format switching

### 5. Tool Count Scaling (`test_tool_count_scaling.py`)
- **What:** Same prompt with 1, 3, 5, 8, 10, 15 tool definitions
- **Validates:** Consistent format at all counts, correct tool selected
- **Key detection:** Tool count threshold where format switches

### 6. Voxel Arena Tools (`test_voxel_tools.py`)
- **What:** 4 real-world tools with complex schemas: integer constraints (min/max 0-15), enum types (12 block types), zero-parameter tools, mixed signatures (0-4 params)
- **Validates:** Whether tool calling mechanics hold up with real-world tool complexity
- **5 sub-checks:**
  - `tool_selection` — correct tool from 4 options, all 4 params valid
  - `enum_adherence` — block type is exactly a valid enum value
  - `integer_constraints` — coordinates are ints within 0-15 range
  - `zero_param_tool` — calls getWorldState with empty args
  - `tool_discrimination` — calls removeBlock not placeBlock
- Pass = all 5 sub-checks pass; each is a single independent API call

### 7. Voxel Arena Tools — Text Fallback (`test_voxel_tools_text.py`)
- **What:** Same 5 sub-checks as Test 6, but via text-based tool calling (no native `tools` parameter). Uses `build_text_tool_system_prompt()` with enum values and min/max constraints rendered in the prompt.
- **Validates:** Whether text-based tool calling handles real-world tool complexity
- **Research question:** Comparing Test 6 (native) vs Test 7 (text) per model reveals whether text-based fallback is a viable uniform solution

## Schema Validation

All tool call arguments are validated against the provided tool schema:
- Required arguments must be present
- No hallucinated (extra) arguments allowed
- Type checking where possible (string, number, integer, boolean)
- Enum validation: values must be in the schema's allowed list
- Range validation: numeric values must satisfy minimum/maximum constraints

## Output

### Terminal
Rich-formatted summary tables:
- One table per flag combo (S0T0, S0T1, S1T0, S1T1) showing pass/fail/skip for each model × test
- A condensed comparison table with 4-char codes (e.g., `PPFP`) showing pass/fail across all flag combos
- Aggregate statistics (passed/failed/skipped/total)

### Summaries
Markdown reports saved to `observations/summaries/{timestamp}_results.md` with:
- Per-flag-combo summary tables
- Flag comparison table
- Detailed per-test results with classification

### Raw Data
JSON files in `observations/raw/` preserving every API request and response.
