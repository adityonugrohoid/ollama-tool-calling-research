# Research Methodology

## Objective

Systematically document how open-source LLMs handle native tool calling through Ollama, identifying failure modes, inconsistencies, and thresholds that affect reliability.

## Test Design Principles

### Reproducibility

Every test uses fixed parameters to ensure reproducible results:

- **temperature=0** — Eliminates randomness in output
- **seed=42** — Fixed random seed for deterministic behavior
- **stream=false** — Default mode (unless testing streaming specifically)
- **num_ctx=4096** — Consistent context window across models

### Raw Data Preservation

Every API call logs:
- The full request payload (model, messages, tools, options)
- The full response JSON (including all metadata: timing, token counts, etc.)
- Timestamp for temporal tracking
- File path: `observations/raw/{model}_{test_name}_{timestamp}.json`

This is a research repo — raw data is the primary deliverable.

### Error Isolation

Each test catches all exceptions. A model crash, timeout, or malformed response is logged as a result, not propagated as an error. The test suite continues running other models and tests.

## Native vs Text Classification

Each response is classified into one of three format types:

### Native (`native`)
- Tool calls appear in `response.message.tool_calls` as structured objects
- Parsed by `tool_parser_native.py`
- This is the expected behavior when the `tools` parameter is provided

### Text (`text`)
- Tool calls appear in `response.message.content` as text
- May use XML delimiters: `<tool_call>{"name": ..., "arguments": ...}</tool_call>`
- May use markdown code blocks: `` ```json ... ``` ``
- May be raw JSON embedded in text
- Parsed by `tool_parser_text.py`

### None (`none`)
- No tool calls detected in either native or text format
- The model either answered in plain text or produced unparseable output

### Mixed (`mixed`)
- Used in multi-turn tests where format changes mid-conversation
- E.g., turns 1-3 use native, turns 4-5 use text

## Test Suite

### 1. Single Tool (`test_single_tool.py`)
- **What:** One tool (get_weather), one question
- **Validates:** Tool calls present, correct name, valid arguments, no hallucinated params
- **Known issue tested:** #5 (missing prefix), #6 (hallucinated parameters)

### 2. Multi-Tool Selection (`test_multi_tool.py`)
- **What:** 3 tools available, question requiring one
- **Validates:** Correct tool selected, others not called
- **Known issue tested:** #6 (hallucinated parameters)

### 3. Parallel Calls (`test_parallel_calls.py`)
- **What:** Question requiring 2+ simultaneous tool calls
- **Validates:** Multiple tool calls returned, correct tools, valid arguments
- **Known issue tested:** Parallel call support varies by model

### 4. Multi-Step Loop (`test_multi_step.py`)
- **What:** 5-turn tool calling conversation with simulated tool results
- **Validates:** Consistent format across turns, all turns produce tool calls
- **Known issue tested:** #1 (mid-conversation format switching)

### 5. Streaming (`test_streaming_tools.py`)
- **What:** Same prompt with stream=true vs stream=false
- **Validates:** Tool calls survive streaming, results consistent
- **Known issue tested:** #3 (streaming drops tool calls)

### 6. Tool Count Scaling (`test_tool_count_scaling.py`)
- **What:** Same prompt with 1, 3, 5, 8, 10, 15 tool definitions
- **Validates:** Consistent format at all counts, correct tool selected
- **Known issue tested:** #2 (tool count threshold)

### 7. Thinking + Tools (`test_thinking_with_tools.py`)
- **What:** think=true with tool calling
- **Validates:** Thinking tokens don't corrupt tool JSON, tool call valid
- **Known issue tested:** #4 (thinking mode interference)

### 8. Text Fallback Baseline (`test_text_fallback.py`)
- **What:** No native tools param, prompt-level instructions for XML tool calls
- **Validates:** Parse success rate of text-based approach
- **Known issue tested:** #7 (text-as-JSON malformation)
- Runs 3 repetitions to measure reliability

## Schema Validation

All tool call arguments are validated against the provided tool schema:
- Required arguments must be present
- No hallucinated (extra) arguments allowed
- Type checking where possible (string, number, integer, boolean)

## Output

### Terminal
Rich-formatted summary matrix showing pass/fail/skip for each model x test combination.

### Summaries
Markdown reports saved to `observations/summaries/{timestamp}_results.md` with:
- Summary table
- Detailed per-test results
- Format classification for each result

### Raw Data
JSON files in `observations/raw/` preserving every API request and response.
