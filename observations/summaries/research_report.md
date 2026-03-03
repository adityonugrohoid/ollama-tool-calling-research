# Tool Calling Behavior Across Open-Source LLMs on Ollama Cloud

**Date:** March 2026
**Scope:** 32 models, 1,792 test runs across two independent sweeps (v3 + v4)
**Platform:** Ollama Cloud API

## Abstract

This report documents the tool calling capabilities of 32 open-source large language models served through the Ollama Cloud API. Each model was evaluated across 7 tests and 4 flag combinations (stream × think), producing 60 scored checks per model. Two complete sweeps (v3 and v4) totaling 1,792 runs provide both behavioral analysis and measurement reproducibility data. Key findings: model size does not predict tool calling quality (3B and 1T models both achieve perfect scores), native and text-based tool calling are orthogonal capabilities, the `stream=true` flag degrades but never improves tool calling, and `think=true` produces unpredictable per-test effects in certain model families. Of 32 models tested, 10 achieve perfect 60/60 scores across all conditions, while specific failure patterns — enum hallucination, integer boundary confusion, parallel call inability — reproduce consistently across sweeps, confirming they are genuine model limitations rather than measurement noise.

---

## 1. Test Arsenal

The test suite comprises 7 tests organized into three tiers of increasing complexity. Each test targets a specific failure mode observed in real-world tool calling deployments.

All tests use deterministic settings: `temperature=0`, `seed=42`. Context window (`num_ctx`) uses each model's default — no artificial truncation is applied.

### Tier 1 — Core Plumbing

These tests validate the fundamental mechanics of tool calling. A model that fails here cannot reliably invoke any tool.

#### Test 1: single_tool

**Purpose:** Verify a model can invoke a single tool with correct name and arguments.

**Prompt:** `"What is the current weather in Tokyo?"`

**Tools provided:**
```json
{
  "name": "get_weather",
  "parameters": {
    "type": "object",
    "required": ["city"],
    "properties": {
      "city": {"type": "string", "description": "The city name"}
    }
  }
}
```

**Pass criteria:** Tool call present, name is `get_weather`, arguments are schema-valid, `city` is non-empty.

#### Test 2: multi_tool

**Purpose:** Verify a model selects the correct tool from a set of 3.

**Prompt:** `"What's the weather like in Paris right now?"`

**Tools provided:** `get_weather`, `search_restaurants`, `book_flight` (3 tools)

**Pass criteria:** Exactly 1 tool call, correct tool selected (`get_weather` not `search_restaurants` or `book_flight`), arguments schema-valid.

#### Test 3: parallel_calls

**Purpose:** Verify a model can return multiple tool calls in a single response.

**Prompt:** `"What is the weather in London and also what is the population of London?"`

**Tools provided:** `get_weather`, `get_temperature`, `get_population` (3 tools)

**Pass criteria:** At least 2 tool calls returned, at least 2 different tools called (diversity check), all arguments schema-valid.

### Tier 2 — Behavioral Stress

These tests apply sustained pressure to surface format instability and scaling limits.

#### Test 4: multi_step

**Purpose:** Verify format consistency across a 5-turn conversation.

**Prompts (sequential):**
1. `"What is the weather in Tokyo?"`
2. `"Now tell me the weather in Paris."`
3. `"Now tell me the weather in New York."`
4. `"Now tell me the weather in London."`
5. `"Now tell me the weather in Sydney."`

**Tools provided:** `get_weather` (1 tool, same across all 5 turns)

**Pass criteria:** All 5 turns produce tool calls, no format switching (native-to-text or text-to-native) mid-conversation.

#### Test 5: tool_count_scaling

**Purpose:** Verify correct tool selection as the tool set scales from 1 to 15.

**Prompt:** `"What is the current weather in Tokyo?"` (same at every scale)

**Tools provided:** 1, 3, 5, 8, 10, then 15 tools. `get_weather` is always the first tool; the remaining slots are filled with unrelated dummy tools (`calculate_tax`, `translate_text`, `send_email`, etc.).

**Pass criteria:** Correct tool selected at every scale point, format consistent across all counts, all arguments schema-valid.

### Tier 3 — Schema Complexity

These tests use a voxel world domain with complex schemas: enum constraints, integer boundaries, zero-parameter tools, and tool discrimination. Each test produces 5 sub-checks.

#### Test 6: voxel_tools (native path)

**Purpose:** Validate schema adherence when tools have complex parameter constraints.

**Tools provided (via `tools` parameter):**
```
placeBlock(x: int 0-15, y: int 0-15, z: int 0-15, type: enum[stone,dirt,grass,
           wood,sand,water,glass,brick,iron,gold,diamond,obsidian])
removeBlock(x: int 0-15, y: int 0-15, z: int 0-15)
getWorldState()  — zero parameters
done(description: string)
```

**5 sub-checks:**

| Sub-check | Prompt | Expected | Validates |
|-----------|--------|----------|-----------|
| **v_sel** (tool selection) | "Place a stone block at position x=3, y=0, z=5." | `placeBlock(3,0,5,"stone")` | Correct tool + all args |
| **v_enum** (enum adherence) | "Place a gold block at x=7, y=1, z=7." | `placeBlock(7,1,7,"gold")` | Enum value is exactly `"gold"` |
| **v_int** (integer constraints) | "Place a stone block at the highest point: x=15, y=15, z=15." | `placeBlock(15,15,15,"stone")` | Boundary integers (max=15) |
| **v_zero** (zero-param tool) | "Check the current state of the world." | `getWorldState()` | Handles empty parameter set |
| **v_disc** (tool discrimination) | "Remove the block at position x=3, y=0, z=5." | `removeBlock(3,0,5)` | Picks `removeBlock` not `placeBlock` |

**Pass criteria:** All 5 sub-checks pass.

#### Test 7: voxel_tools_text (text fallback path)

**Purpose:** Same 5 sub-checks as Test 6, but using text-based tool calling.

**Difference from Test 6:** No `tools` parameter is passed. Instead, tool definitions are embedded in a system prompt instructing the model to output tool calls in XML format:

```xml
<tool_call>
{"name": "TOOL_NAME", "arguments": {"arg1": "value1"}}
</tool_call>
```

The parser attempts XML tags first, then markdown code blocks, then raw JSON detection.

**Pass criteria:** Same as Test 6 — all 5 sub-checks pass via text extraction.

### Test Summary

| Tier | Test | Tools | Checks | What failure surfaces |
|------|------|-------|--------|----------------------|
| 1 | single_tool | 1 | 1 | Cannot invoke any tool |
| 1 | multi_tool | 3 | 1 | Cannot select from set |
| 1 | parallel_calls | 3 | 1 | Cannot return multiple calls |
| 2 | multi_step | 1 × 5 turns | 1 | Format instability over time |
| 2 | tool_count_scaling | 1→15 | 1 | Breaks under tool proliferation |
| 3 | voxel_tools | 4 | 5 | Schema constraint violations |
| 3 | voxel_tools_text | 4 (text) | 5 | Text fallback schema violations |
| | **Total per flag combo** | | **15** | |

---

## 2. Flag Matrix — The 2×2 Stress Dimension

Every test runs across 4 flag combinations, forming a 2×2 matrix:

```
                 think=false          think=true
stream=false     S0T0 (baseline)      S0T1 (thinking interference)
stream=true      S1T0 (streaming)     S1T1 (combined stress)
```

**Why a matrix, not standalone tests:** The `stream` and `think` flags interact in ways that are not additive. A model may handle streaming perfectly in isolation but fail when thinking is enabled simultaneously. The matrix captures these interactions.

**Scoring per model:**
- 7 tests × 4 flag combos = 28 test-level runs
- Voxel tests expand: 5 sub-checks each × 4 combos × 2 tests = 40 voxel checks
- Plus 5 non-voxel tests × 4 combos = 20 simple checks
- **Total: 60 checks per model**

**Score values:**
- **P** (pass) — Model returned correct tool call(s)
- **F** (fail) — Model returned incorrect output (wrong tool, bad args, no tool call, format switch)
- **T** (transient) — Server error (HTTP 500 or 503) despite retry with exponential backoff (3 attempts, 2s/4s/8s)

---

## 3. Observable Behavior: Streaming Flag

### 3a. Stream amplifies transient errors

The clearest streaming effect is on server stability. The `cogito-2.1:671b` pattern demonstrates this:

| Flag combo | Score | Pattern |
|------------|-------|---------|
| S0T0 (baseline) | 8/15 | single/multi/parallel pass; step/scale/voxel timeout |
| S0T1 (think only) | 6/15 | Similar but more voxel_text timeouts |
| S1T0 (stream only) | 3/15 | voxel_tools AND voxel_tools_text both timeout |
| S1T1 (both) | 3/15 | Same as S1T0 — streaming dominates |

Streaming keeps the HTTP connection open longer, making it more susceptible to 503 timeouts. The simple tests (single/multi/parallel) still pass because they complete quickly, but complex tests that require multiple API calls (voxel sub-checks, multi-step turns) timeout under streaming.

### 3b. Stream triggers format instability

- **nemotron-3-nano:30b:** multi_step pattern `PPFP` — S1T0 fails while all other combos pass. Streaming disrupts multi-turn format consistency.
- **minimax-m2.5:** voxel_tools_text vt_zero pattern `PFFF` — Only the non-streaming, non-thinking baseline passes; all other combos fail the zero-parameter tool sub-check.

### 3c. Stream-agnostic models

Most models show no streaming effect:
- **10 perfect models:** Identical 15/15 across all 4 combos
- **gemma3 family:** `FFFF` on all native checks regardless of streaming (no native support)
- **GLM family:** Native `PPPP` regardless, text `FFFF` regardless — streaming changes nothing
- **devstral-small-2:24b:** v_int `FFFF` across all combos — a model-level bug unaffected by streaming

### 3d. Streaming observability gap

Analysis of 8,170 raw response logs revealed a significant blind spot: **47% of raw logs (3,831 files) are streaming responses saved as Python generator object strings**, not serialized response data. The `stream_collector.py` module assembles chunks into a `PseudoResponse` for real-time processing, but discards final-chunk metadata (`done_reason`, `eval_count`, `prompt_eval_count`). This means post-hoc analysis of streaming token counts and completion reasons is impossible from the raw logs alone.

However, streaming is a transport-layer mechanism — the same deterministic settings (`temperature=0`, `seed=42`) produce identical token sequences regardless of delivery method. Streaming failures in the dataset are connection-level issues (503 timeouts from sustained HTTP connections), not generation-level differences. The 4,338 analyzable non-streaming responses are therefore representative of the token generation behavior across all runs.

### 3e. Key finding

> **Streaming never improves a failing model's tool calling. It occasionally degrades a passing model, and significantly amplifies transient server errors. Streaming is a transport-layer concern — it does not change what the model generates, only how reliably the connection delivers it.**

---

## 4. Observable Behavior: Thinking Flag

### 4a. Thinking interference — the deepseek-v3.1 pattern

The most distinctive pattern in the dataset is `deepseek-v3.1:671b`'s systematic alternation:

| Test | Pattern | Interpretation |
|------|---------|----------------|
| single_tool | `FPFP` | think=false → **F**, think=true → **P** |
| multi_step | `PFPF` | think=false → **P**, think=true → **F** |

This is not random noise — it is a systematic inversion by the think flag. With `think=true`, the model's internal routing changes: it gains the ability to invoke a single tool (previously failing) but loses the ability to maintain format consistency across turns (previously passing). The same alternation appears across streaming combinations, confirming the think flag as the causal variable.

Additional deepseek-v3.1 patterns showing think-sensitivity:
- scale: `PFPP` — S0T1 fails (think breaks at scale)
- v_sel: `FFPF` — complex mixed pattern
- v_disc: `PFPP` — think breaks discrimination on S0T1

### 4b. Thinking helps sometimes

- **qwen3-vl:235b-instruct:** step `FPFF` — Only S0T1 passes (think=true helps without streaming)
- **gpt-oss:120b:** step `FPTP` — S0T1 and S1T1 pass (think helps regardless of streaming)
- **mistral-large-3:675b:** scale `FPPP` — S0T0 fails, but all think=true combos pass

### 4c. Thinking hurts sometimes

- **qwen3-next:80b:** step `PFPP` — S0T1 fails (think breaks multi-step consistency)
- **deepseek-v3.1:671b:** step `PFPF` — think=true consistently breaks multi-step

### 4d. Think-agnostic models

- **10 perfect models:** Identical results across think=false and think=true
- **gemma3 family:** `FFFF` regardless (no native support)
- **Most GB models:** Native `PPPP`, text `FFFF` regardless of thinking

### 4e. Thinking derailment — token-level evidence

Analysis of 4,338 non-streaming raw response logs reveals the mechanism behind thinking-related failures. Key findings:

**No truncation detected.** Zero responses (0/4,338) show `done_reason="length"` — every response completed naturally. The maximum observed token count was 4,296 (`prompt_eval_count` + `eval_count`), with a median of ~450 tokens. Only 25 responses exceeded 2,000 tokens.

**Thinking derailment, not cutoff.** The 2,000+ token responses are dominated by `deepseek-v3.1:671b` with `think=true`, which generates massive internal reasoning chains (up to 13,000 characters / 3,874 eval tokens). The model completes its thinking but then fails to produce a valid tool call — the extended reasoning derails the model from the task rather than being truncated mid-thought.

**Parser gap for model-specific formats.** 10 deepseek-v3.1 responses contain tool calls embedded in model-specific special token format (`<｜tool▁calls▁begin｜>`) within the thinking layer. The text parser (which handles XML `<tool_call>` tags, markdown code blocks, and raw JSON) cannot extract these. These are scored as F, though the model did generate tool call intent — it used an unparseable internal format.

**Available response metrics on Ollama Cloud.** Every non-streaming response includes: `done_reason`, `total_duration`, `prompt_eval_count`, and `eval_count` (100% present). The fields `load_duration`, `prompt_eval_duration`, `eval_duration`, and `logprobs` are always `None` on the cloud endpoint — per-token timing and log probabilities are not available.

### 4f. Key finding

> **`think=true` is neither universally positive nor negative. It changes internal model routing, which can flip specific test outcomes in either direction. The failure mechanism is thinking derailment (extended reasoning that loses track of the task), not context truncation. Only deepseek-v3.1 shows systematic alternation — a unique failure mode. All production-ready models (GA group) are completely think-agnostic.**

---

## 5. Temporal Consistency: v3 vs v4 Sub-check Comparison

Two complete sweeps of 32 models (v3 and v4, each 896 runs) provide a natural experiment in measurement reproducibility. The v3 sweep used size-based groups (P0/P1/P2); v4 used behavior-based groups (GA/GB/GC/GD). Both used identical test code, deterministic settings, and the same Ollama Cloud API endpoint.

### Sub-check-level deterministic models

These models reproduced the exact same P/F/T pattern at every sub-check position across both sweeps:

| Model | Pattern | Both sweeps |
|-------|---------|-------------|
| ministral-3:3b | PPPP × 15 | 60/60 |
| ministral-3:8b | PPPP × 15 | 60/60 |
| ministral-3:14b | PPPP × 15 | 60/60 |
| devstral-2:123b | PPPP × 15 | 60/60 |
| gemini-3-flash-preview | PPPP × 15 | 60/60 |
| kimi-k2.5 | PPPP × 15 | 60/60 |
| kimi-k2-thinking | PPPP × 15 | 60/60 |
| devstral-small-2:24b | v_int FFFF, rest PPPP | 56/60 |
| qwen3-coder-next | native PPPP×10, text TTTT×5 | 40/60 (20T) |
| qwen3-coder:480b | native PPPP×10, text TTTT×5 | 40/60 (20T) |
| rnj-1:8b | v_zero TTTT, vt_int FFFF, rest PPPP | 52/60 (4T) |
| gemma3:4b | native FFFF×10, text PPPP×5 | 20/60 |
| gemma3:12b | native FFFF×10, text PPPP×5 | 20/60 |
| gemma3:27b | native FFFF×10, text PPPP×5 | 20/60 |

**14 of 32 models** are fully deterministic at the sub-check level across sweeps.

### Total-stable but sub-check-nondeterministic

These models achieved the same total score in both sweeps, but specific sub-check outcomes shuffled between positions:

| Model | Score (both) | What changed |
|-------|-------------|--------------|
| gpt-oss:20b | 44/60 (3T) | v3: step `TPPP`, v_int `PPFP` / v4: step `PPPP`, v_int `PPPP`, vt_int `FPPP` — same total, different cells flip |
| minimax-m2.5 | 57/60 | v3: vt_zero `FFPF` / v4: vt_zero `PFFF` — same 3F count, positions shift |
| glm-4.7 | 42/60 | v3: vt_zero `PPFF` / v4: vt_zero `FPPF` — same 2F count, positions shift |
| qwen3-vl:235b-instruct | 57/60 | v3: step `PFFF` / v4: step `FPFF` — same 3F count, positions shift |
| qwen3.5:397b | 58/60 | v3: scale `PPFP`, vt_enum `PPPT` / v4: scale `PPPP`, vt_sel `PPTT` — different non-P positions |

**5 models** are nondeterministic: the total score reproduces, but individual sub-check outcomes are not stable.

### Server-unstable

Dramatic score changes driven by infrastructure, not model behavior:

| Model | v3 | v4 | Cause |
|-------|-----|-----|-------|
| cogito-2.1:671b | 60/60 | 20/60 (40T) | Server 503 regression on streaming |
| qwen3-vl:235b | 20/60 (40T) | 60/60 | Server fix — T resolved to P |
| minimax-m2 | 59/60 (1T) | 52/60 (7T) | Server destabilization |

### Consistent failure signatures across sweeps

These failure patterns reproduced identically in both v3 and v4, confirming they are genuine model limitations:

- **gpt-oss parallel `FFFF`** — both sizes, both sweeps
- **devstral-small-2 v_int `FFFF`** — calls `getWorldState` at boundary values
- **mistral-large-3 v_int `FFFF`** — same boundary confusion as devstral-small-2
- **GLM family vt_sel/vt_enum `FFFF`** — systematic text fallback failure
- **qwen3-next scale `FFFF`** — breaks under tool proliferation
- **deepseek-v3.1 think alternation** — PFPF/FPFP pattern in both sweeps

---

## 6. Test Suite Discriminating Power

### Universal pass (low discriminating power)

- **single_tool:** 27/32 models pass all 4 combos. Only gemma3×3 (no native support), deepseek-v3.1 (think alternation `FPFP`), and deepseek-v3.2 (fully broken `FFFF`) fail.
- **multi_tool:** 28/32 models pass. Same failures minus deepseek-v3.1 (which passes multi_tool `PPPP`).

These tests confirm basic plumbing works for the vast majority of models, but provide little differentiation among functional models.

### Medium discriminating power

- **parallel_calls:** Surfaces gpt-oss `FFFF` (both sizes return 1 call instead of 2+), gemma3 `FFFF`, deepseek-v3.2 `FFFF`, deepseek-v3.1 `FPPP`.
- **multi_step:** Surfaces format switching — deepseek-v3.1 `PFPF`, qwen3-vl:235b-instruct `FPFF`, qwen3-next `PFPP`, nemotron step `PPFP`.
- **tool_count_scaling:** Surfaces qwen3-next `FFFF`, mistral-large-3 `FPPP`, deepseek-v3.1 `PFPP`.

### Highest discriminating power

- **voxel_tools:** 12+ models fail at least one sub-check. Surfaces enum hallucination (gpt-oss `gold_block`), integer boundary confusion (devstral-small-2, mistral-large-3), zero-param failures (rnj-1 `TTTT`).
- **voxel_tools_text:** Most discriminating test overall. GLM family `FFFF` on sel/enum, qwen-coder `TTTT` (server rejection), deepseek-v3.2 mixed failures, gpt-oss:20b scattered failures.

### Sub-check discriminating power

| Sub-check | Failure pattern | Models affected |
|-----------|----------------|-----------------|
| v_sel | Rarely fails alone | Correlates with total native failure |
| v_enum | gpt-oss `gold_block` hallucination | gpt-oss:120b `FFFP`, gpt-oss:20b `FFFT` |
| v_int | Boundary value confusion | devstral-small-2 `FFFF`, mistral-large-3 `FFFF` |
| v_zero | Empty parameter handling | rnj-1:8b `TTTT`, minimax-m2 intermittent |
| v_disc | Rarely fails alone | Deepseek-v3.1 scattered |
| vt_sel | Text tool selection | GLM-4.6/4.7/5 `FFFF`, nemotron scattered |
| vt_enum | Text enum adherence | GLM family `FFFF` |
| vt_int | Text integer handling | GLM family `FFFF`, rnj-1 `FFFF` |
| vt_zero | Text zero-param | minimax-m2.5 `PFFF`, GLM scattered, gpt-oss:20b `FFFF` |
| vt_disc | Text discrimination | GLM-4.7/5 `FFFF`, nemotron scattered |

---

## 7. Badge System

Badges are tag identifiers for quick model characterization across multiple dimensions.

### Performance Tier (v4 score)

| Badge | Criteria | Count |
|-------|----------|-------|
| `PERFECT` | 60/60 | 10 |
| `NEAR-PERFECT` | 55–59/60 | 6 |
| `FUNCTIONAL` | 40–54/60 | 11 |
| `MINIMAL` | 15–39/60 | 5 |

### Layer Capability

| Badge | Criteria | Count |
|-------|----------|-------|
| `DUAL-LAYER` | Native 40/40 P and text 20/20 P | 10 (GA) |
| `NATIVE-ONLY` | Native 40/40 P, text has F | 8 (GB) |
| `TEXT-ONLY` | Text 20/20 P, native has F | 8 (GC) |
| `MIXED-LAYER` | Both layers have F | 6 (GD) |

### Temporal Stability (v3→v4 delta)

| Badge | Criteria | Count |
|-------|----------|-------|
| `ROCK-STABLE` | Delta = 0 | 19 |
| `IMPROVED` | Delta +1 to +3 | 4 |
| `MAJOR-UPGRADE` | Delta > +3 | 2 |
| `SLIGHT-REGRESSION` | Delta -1 to -3 | 5 |
| `MAJOR-REGRESSION` | Delta < -3 | 2 |

### Measurement Reproducibility (sub-check level)

| Badge | Criteria | Count |
|-------|----------|-------|
| `DETERMINISTIC` | Identical sub-check pattern across both sweeps | 14 |
| `NONDETERMINISTIC` | Same total score, sub-check outcomes shuffle | 5 |
| `SERVER-UNSTABLE` | Score change driven by infrastructure | 3 |

### Flag Sensitivity

| Badge | Criteria |
|-------|----------|
| `FLAG-AGNOSTIC` | Every check is uniformly P, F, or T across all 4 combos |
| `STREAM-SENSITIVE` | stream=true changes outcomes |
| `THINK-SENSITIVE` | think=true changes outcomes |
| `THINK-ALTERNATING` | Systematic PFPF/FPFP pattern (think inverts pass/fail) |

### Failure Signature

| Badge | Failure mode |
|-------|-------------|
| `ENUM-HALLUCINATOR` | Fabricates enum values not in schema (e.g., `gold_block` for `gold`) |
| `BOUNDARY-CONFUSED` | Fails at integer min/max boundaries (calls wrong tool at x=15,y=15,z=15) |
| `PARALLEL-INCAPABLE` | Returns 1 tool call instead of 2+ when asked for parallel calls |
| `FORMAT-SWITCHER` | Changes native↔text format mid-conversation |
| `SERVER-BLOCKED` | Server rejects the request (tools=None rejection, etc.) |
| `ZERO-PARAM-FAIL` | Cannot handle tools with zero parameters |

---

## 8. Model Family Performance Review

### Ministral Family (3b, 8b, 14b) — Group GA

Badges: `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `FLAG-AGNOSTIC` `DETERMINISTIC`

| Model | Size | v3 | v4 | Delta |
|-------|------|-----|-----|-------|
| ministral-3:3b | 3B | 60/60 | 60/60 | 0 |
| ministral-3:8b | 8B | 60/60 | 60/60 | 0 |
| ministral-3:14b | 14B | 60/60 | 60/60 | 0 |

All three sizes achieve identical perfect scores across every dimension: every sub-check is `PPPP`, both sweeps produce bit-for-bit identical results, and no flag combination affects behavior. The 3B model achieves the same quality as models 300× its size, making this the most compelling evidence against size-quality correlation in the dataset.

### Gemini (flash-preview) — Group GA

Badges: `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `FLAG-AGNOSTIC` `DETERMINISTIC`

| Model | v3 | v4 | Delta |
|-------|-----|-----|-------|
| gemini-3-flash-preview | 60/60 | 60/60 | 0 |

Zero variation across all dimensions. Perfect deterministic behavior.

### Kimi Family (k2.5, k2-thinking, k2:1t) — Group GA

All: `PERFECT` `DUAL-LAYER` `FLAG-AGNOSTIC` `DETERMINISTIC`

| Model | Size | v3 | v4 | Delta | Stability |
|-------|------|-----|-----|-------|-----------|
| kimi-k2.5 | 1T | 60/60 | 60/60 | 0 | `ROCK-STABLE` |
| kimi-k2-thinking | 1T | 60/60 | 60/60 | 0 | `ROCK-STABLE` |
| kimi-k2:1t | 1T | 59/60 (1T) | 60/60 | +1 | `IMPROVED` |

Three 1T-parameter models, all perfect in v4. kimi-k2:1t had a single transient error in v3 that resolved by v4.

### Devstral Family (2:123b, small-2:24b) — Groups GA/GC

| Model | Group | Size | v3 | v4 | Delta | Badges |
|-------|-------|------|-----|-----|-------|--------|
| devstral-2:123b | GA | 123B | 60/60 | 60/60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `FLAG-AGNOSTIC` `DETERMINISTIC` |
| devstral-small-2:24b | GC | 24B | 56/60 | 56/60 | 0 | `NEAR-PERFECT` `TEXT-ONLY` `ROCK-STABLE` `FLAG-AGNOSTIC` `DETERMINISTIC` `BOUNDARY-CONFUSED` |

devstral-small-2 has a single persistent failure: v_int `FFFF` across all combos and both sweeps. When prompted to place a block at boundary values (x=15, y=15, z=15), it calls `getWorldState` instead of `placeBlock`. The text layer (20/20) is perfect, confirming this is a native-path schema interpretation issue.

### Minimax Family (m2, m2.1, m2.5) — Groups GA/GB

| Model | Group | v3 | v4 | Delta | Key badges |
|-------|-------|-----|-----|-------|------------|
| minimax-m2 | GA | 59/60 (1T) | 52/60 (7T) | -7 | `FUNCTIONAL` `DUAL-LAYER` `MAJOR-REGRESSION` `SERVER-UNSTABLE` |
| minimax-m2.1 | GB | 57/60 | 60/60 | +3 | `PERFECT` `DUAL-LAYER` `IMPROVED` `FLAG-AGNOSTIC` |
| minimax-m2.5 | GB | 57/60 | 57/60 | 0 | `NEAR-PERFECT` `NATIVE-ONLY` `ROCK-STABLE` `NONDETERMINISTIC` |

A family with divergent trajectories: m2.1 improved to perfect (vt_zero resolved), m2 regressed due to server instability (7 new transient errors), and m2.5 is stable but nondeterministic — its vt_zero pattern shifted from `FFPF` (v3) to `PFFF` (v4), same 3 failures but different positions.

### GLM Family (4.6, 4.7, 5) — Group GB

All: `NATIVE-ONLY`

| Model | Size | v3 | v4 | Delta | Text score | Key badges |
|-------|------|-----|-----|-------|------------|------------|
| glm-4.6 | 357B | 49/60 | 48/60 | -1 | 8/20 | `FUNCTIONAL` `SLIGHT-REGRESSION` `FLAG-AGNOSTIC` |
| glm-4.7 | 357B | 42/60 | 42/60 | 0 | 2/20 | `FUNCTIONAL` `ROCK-STABLE` `NONDETERMINISTIC` |
| glm-5 | 756B | 43/60 | 41/60 | -2 | 1/20 | `FUNCTIONAL` `SLIGHT-REGRESSION` |

All three have perfect native (40/40) but systematically broken text fallback. The text failure pattern is consistent: vt_sel and vt_enum are `FFFF` across the family. Notably, glm-5 (756B, largest) has the worst text score (1/20), while glm-4.6 (357B) has the best (8/20) — another instance of larger not meaning better.

### Qwen Family (6 models) — Groups GB/GC/GD

The most diverse family in the dataset, spanning 3 groups:

| Model | Group | Size | v3 | v4 | Delta | Key badges |
|-------|-------|------|-----|-----|-------|------------|
| qwen3-coder-next | GB | 80B | 40/60 (20T) | 40/60 (20T) | 0 | `FUNCTIONAL` `NATIVE-ONLY` `ROCK-STABLE` `DETERMINISTIC` `SERVER-BLOCKED` |
| qwen3-coder:480b | GB | 480B | 40/60 (20T) | 40/60 (20T) | 0 | `FUNCTIONAL` `NATIVE-ONLY` `ROCK-STABLE` `DETERMINISTIC` `SERVER-BLOCKED` |
| qwen3-vl:235b | GC | 235B | 20/60 (40T) | 60/60 | +40 | `PERFECT` `DUAL-LAYER` `MAJOR-UPGRADE` `FLAG-AGNOSTIC` `SERVER-UNSTABLE` |
| qwen3-vl:235b-instruct | GC | 235B | 57/60 | 57/60 | 0 | `NEAR-PERFECT` `TEXT-ONLY` `ROCK-STABLE` `NONDETERMINISTIC` `THINK-SENSITIVE` |
| qwen3.5:397b | GD | 397B | 58/60 | 58/60 | 0 | `NEAR-PERFECT` `MIXED-LAYER` `ROCK-STABLE` `NONDETERMINISTIC` |
| qwen3-next:80b | GD | 80B | 54/60 | 55/60 | +1 | `NEAR-PERFECT` `MIXED-LAYER` `IMPROVED` |

Highlights:
- The qwen3-coder pair (80B and 480B) are identical: perfect native, all text blocked by server (T not F). The 6× size difference produces zero behavioral difference.
- qwen3-vl:235b is the biggest positive swing in the dataset (+40), going from completely blocked by server errors to perfect 60/60.
- qwen3-vl:235b-instruct shows think-sensitivity: step `FPFF` — only S0T1 passes.
- qwen3-next:80b has persistent scale `FFFF` but improved on step (54→55).

### GPT-OSS Family (20b, 120b) — Groups GC/GD

All: `PARALLEL-INCAPABLE` `ENUM-HALLUCINATOR`

| Model | Group | v3 | v4 | Delta | Key badges |
|-------|-------|-----|-----|-------|------------|
| gpt-oss:120b | GC | 52/60 | 51/60 (1T) | -1 | `FUNCTIONAL` `TEXT-ONLY` `SLIGHT-REGRESSION` |
| gpt-oss:20b | GD | 44/60 (3T) | 44/60 (3T) | 0 | `FUNCTIONAL` `MIXED-LAYER` `ROCK-STABLE` `NONDETERMINISTIC` |

Shared family failures:
1. **parallel_calls `FFFF`** — Both models consistently return 1 tool call instead of 2+, across all flag combos and both sweeps.
2. **v_enum hallucination** — When asked to place a `gold` block, both fabricate `gold_block` (not in the enum). gpt-oss:120b: v_enum `FFFP` (v4), gpt-oss:20b: v_enum `FFFT`.

### Gemma3 Family (4b, 12b, 27b) — Group GC

All: `MINIMAL` `TEXT-ONLY` `ROCK-STABLE` `FLAG-AGNOSTIC` `DETERMINISTIC`

| Model | Size | v3 | v4 | Delta |
|-------|------|-----|-----|-------|
| gemma3:4b | 4B | 20/60 | 20/60 | 0 |
| gemma3:12b | 12B | 20/60 | 20/60 | 0 |
| gemma3:27b | 27B | 20/60 | 20/60 | 0 |

All three are identical regardless of size: zero native tool calling (Ollama does not wire the `tools` parameter for gemma3), perfect text fallback (20/20). Every native check is `FFFF`, every text check is `PPPP`, perfectly deterministic across both sweeps.

### Deepseek Family (v3.1:671b, v3.2) — Group GD

| Model | Size | v3 | v4 | Delta | Key badges |
|-------|------|-----|-----|-------|------------|
| deepseek-v3.1:671b | 671B | 44/60 | 46/60 | +2 | `FUNCTIONAL` `MIXED-LAYER` `IMPROVED` `THINK-ALTERNATING` |
| deepseek-v3.2 | 671B | 5/60 | 16/60 | +11 | `MINIMAL` `MIXED-LAYER` `MAJOR-UPGRADE` |

deepseek-v3.1 has the most unique failure mode in the dataset: systematic think-alternation. Key patterns:
- single_tool `FPFP` — think=true fixes single-tool invocation
- multi_step `PFPF` — think=true breaks multi-turn consistency
- v_sel `FFPF`, v_enum `PPFF` — complex mixed patterns showing think-dependent routing

deepseek-v3.2 improved from near-total failure (5/60) to minimal functionality (16/60). The text layer is recovering (from 5/20 to some passes) but native remains completely broken (`FFFF` × 10).

### Mistral Large (3:675b) — Group GC

Badges: `NEAR-PERFECT` `TEXT-ONLY` `SLIGHT-REGRESSION` `BOUNDARY-CONFUSED`

| Model | v3 | v4 | Delta |
|-------|-----|-----|-------|
| mistral-large-3:675b | 56/60 | 55/60 | -1 |

Shares the exact same v_int `FFFF` bug as devstral-small-2:24b — calls `getWorldState` instead of `placeBlock` at boundary values (x=15, y=15, z=15). Both are Mistral-family models, suggesting a shared training or fine-tuning issue with integer boundary interpretation. The scale test changed from `PPPP` (v3) to `FPPP` (v4), but text layer remains perfect (20/20).

### Nemotron (3-nano:30b) — Group GB

Badges: `FUNCTIONAL` `NATIVE-ONLY` `SLIGHT-REGRESSION` `STREAM-SENSITIVE`

| Model | v3 | v4 | Delta |
|-------|-----|-----|-------|
| nemotron-3-nano:30b | 47/60 (1T) | 44/60 (2T) | -3 |

Native path is perfect (40/40) but text fallback is degrading: v3 had 7/20 text passes, v4 has 4/20. The step test shows `PPFP` — S1T0 (streaming without thinking) breaks multi-turn consistency, making this a clear stream-sensitive model.

### Cogito (2.1:671b) — Group GA (v3), regressed in v4

Badges: `MINIMAL` `DUAL-LAYER` `MAJOR-REGRESSION` `STREAM-SENSITIVE` `SERVER-UNSTABLE`

| Model | v3 | v4 | Delta |
|-------|-----|-----|-------|
| cogito-2.1:671b | 60/60 | 20/60 (40T) | -40 |

The largest regression in the dataset. In v3, cogito was a perfect 60/60 model. In v4, server 503 errors affect all complex tests under streaming. The pattern is clear:
- Simple tests (single/multi/parallel) still pass `PPPP` — these complete quickly
- Complex tests (step/scale/voxel) timeout `TTTT` — these require sustained connections
- Stream=false recovers some tests (v4 S0T0 = 8/15, S0T1 = 6/15)
- Stream=true is catastrophic (S1T0 = 3/15, S1T1 = 3/15)

A separate rerun with retry logic confirmed: stream=false recovers many tests, stream=true still triggers persistent 503s.

### RNJ (1:8b) — Group GD

Badges: `FUNCTIONAL` `MIXED-LAYER` `ROCK-STABLE` `FLAG-AGNOSTIC` `DETERMINISTIC` `ZERO-PARAM-FAIL`

| Model | v3 | v4 | Delta |
|-------|-----|-----|-------|
| rnj-1:8b | 52/60 (4T) | 52/60 (4T) | 0 |

Perfectly deterministic: v_zero `TTTT` and vt_int `FFFF` reproduced identically across both sweeps. The zero-parameter tool (`getWorldState`) consistently triggers transient errors, and text-based integer constraints consistently fail.

---

## 9. Scoring Summary

All 32 models sorted by v4 score. Badges shown are the primary identifiers for each model.

| # | Model | Group | v3 | v4 | Delta | Badges |
|---|-------|-------|-----|-----|-------|--------|
| 1 | ministral-3:3b | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 2 | ministral-3:8b | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 3 | ministral-3:14b | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 4 | devstral-2:123b | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 5 | gemini-3-flash-preview | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 6 | kimi-k2.5 | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 7 | kimi-k2-thinking | GA | 60 | 60 | 0 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 8 | kimi-k2:1t | GA | 59 | 60 | +1 | `PERFECT` `DUAL-LAYER` `IMPROVED` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 9 | minimax-m2.1 | GB | 57 | 60 | +3 | `PERFECT` `DUAL-LAYER` `IMPROVED` `FLAG-AGNOSTIC` |
| 10 | qwen3-vl:235b | GC | 20 | 60 | +40 | `PERFECT` `DUAL-LAYER` `MAJOR-UPGRADE` `FLAG-AGNOSTIC` `SERVER-UNSTABLE` |
| 11 | qwen3.5:397b | GD | 58 | 58 | 0 | `NEAR-PERFECT` `MIXED-LAYER` `ROCK-STABLE` `NONDETERMINISTIC` |
| 12 | qwen3-vl:235b-instruct | GC | 57 | 57 | 0 | `NEAR-PERFECT` `TEXT-ONLY` `ROCK-STABLE` `NONDETERMINISTIC` `THINK-SENSITIVE` |
| 13 | minimax-m2.5 | GB | 57 | 57 | 0 | `NEAR-PERFECT` `NATIVE-ONLY` `ROCK-STABLE` `NONDETERMINISTIC` |
| 14 | devstral-small-2:24b | GC | 56 | 56 | 0 | `NEAR-PERFECT` `TEXT-ONLY` `ROCK-STABLE` `DETERMINISTIC` `BOUNDARY-CONFUSED` |
| 15 | qwen3-next:80b | GD | 54 | 55 | +1 | `NEAR-PERFECT` `MIXED-LAYER` `IMPROVED` |
| 16 | mistral-large-3:675b | GC | 56 | 55 | -1 | `NEAR-PERFECT` `TEXT-ONLY` `SLIGHT-REGRESSION` `BOUNDARY-CONFUSED` |
| 17 | minimax-m2 | GA | 59 | 52 | -7 | `FUNCTIONAL` `DUAL-LAYER` `MAJOR-REGRESSION` `SERVER-UNSTABLE` |
| 18 | rnj-1:8b | GD | 52 | 52 | 0 | `FUNCTIONAL` `MIXED-LAYER` `ROCK-STABLE` `DETERMINISTIC` `ZERO-PARAM-FAIL` |
| 19 | gpt-oss:120b | GC | 52 | 51 | -1 | `FUNCTIONAL` `TEXT-ONLY` `SLIGHT-REGRESSION` `PARALLEL-INCAPABLE` `ENUM-HALLUCINATOR` |
| 20 | glm-4.6 | GB | 49 | 48 | -1 | `FUNCTIONAL` `NATIVE-ONLY` `SLIGHT-REGRESSION` `FLAG-AGNOSTIC` |
| 21 | deepseek-v3.1:671b | GD | 44 | 46 | +2 | `FUNCTIONAL` `MIXED-LAYER` `IMPROVED` `THINK-ALTERNATING` |
| 22 | gpt-oss:20b | GD | 44 | 44 | 0 | `FUNCTIONAL` `MIXED-LAYER` `ROCK-STABLE` `NONDETERMINISTIC` `PARALLEL-INCAPABLE` `ENUM-HALLUCINATOR` |
| 23 | nemotron-3-nano:30b | GB | 47 | 44 | -3 | `FUNCTIONAL` `NATIVE-ONLY` `SLIGHT-REGRESSION` `STREAM-SENSITIVE` |
| 24 | glm-4.7 | GB | 42 | 42 | 0 | `FUNCTIONAL` `NATIVE-ONLY` `ROCK-STABLE` `NONDETERMINISTIC` |
| 25 | glm-5 | GB | 43 | 41 | -2 | `FUNCTIONAL` `NATIVE-ONLY` `SLIGHT-REGRESSION` |
| 26 | qwen3-coder-next | GB | 40 | 40 | 0 | `FUNCTIONAL` `NATIVE-ONLY` `ROCK-STABLE` `DETERMINISTIC` `SERVER-BLOCKED` |
| 27 | qwen3-coder:480b | GB | 40 | 40 | 0 | `FUNCTIONAL` `NATIVE-ONLY` `ROCK-STABLE` `DETERMINISTIC` `SERVER-BLOCKED` |
| 28 | gemma3:4b | GC | 20 | 20 | 0 | `MINIMAL` `TEXT-ONLY` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 29 | gemma3:12b | GC | 20 | 20 | 0 | `MINIMAL` `TEXT-ONLY` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 30 | gemma3:27b | GC | 20 | 20 | 0 | `MINIMAL` `TEXT-ONLY` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 31 | cogito-2.1:671b | GA | 60 | 20 | -40 | `MINIMAL` `DUAL-LAYER` `MAJOR-REGRESSION` `STREAM-SENSITIVE` `SERVER-UNSTABLE` |
| 32 | deepseek-v3.2 | GD | 5 | 16 | +11 | `MINIMAL` `MIXED-LAYER` `MAJOR-UPGRADE` |

### Score distribution

| Tier | Range | Models | % |
|------|-------|--------|---|
| `PERFECT` | 60/60 | 10 | 31% |
| `NEAR-PERFECT` | 55–59 | 6 | 19% |
| `FUNCTIONAL` | 40–54 | 11 | 34% |
| `MINIMAL` | 15–39 | 5 | 16% |

---

## 10. Key Findings

1. **No size-quality correlation.** ministral-3:3b (3B parameters) scores 60/60. deepseek-v3.2 (671B parameters) scores 16/60. The qwen3-coder pair (80B and 480B) produce identical results. Within the gemma3 family, 4B/12B/27B are indistinguishable. Model size is not a predictor of tool calling capability.

2. **Layer independence.** Native and text-based tool calling are orthogonal capabilities. Group GB (8 models) proves native competence does not imply text competence. Group GC (8 models) proves the reverse. Building a reliable tool calling system requires testing both paths independently.

3. **Flag agnosticism equals reliability.** All 10 perfect models are completely flag-agnostic — their behavior is identical regardless of streaming or thinking settings. This is the strongest signal of production readiness. Models that show flag sensitivity have conditional reliability at best.

4. **Streaming degrades, never improves.** Across 32 models and 1,792 runs, `stream=true` never rescued a failing test. It occasionally degraded passing tests (nemotron multi-step, minimax-m2.5 voxel text) and significantly amplified transient server errors (cogito pattern: S0=8/15 → S1=3/15).

5. **Thinking is a wild card.** `think=true` can help or hurt specific tests on the same model. deepseek-v3.1's systematic FPFP/PFPF alternation is the clearest example: thinking fixes single-tool invocation but breaks multi-step consistency. For most models, thinking has zero effect.

6. **Server stability is a measurement variable.** Three models changed by more than 5 points between sweeps due to server behavior, not model behavior: cogito (-40T), qwen3-vl:235b (+40T→P), minimax-m2 (-7T). Any tool calling benchmark on cloud-hosted models must account for infrastructure variance.

7. **Family consistency.** Models in the same family tend to share failure patterns:
   - GLM: text fallback systematically broken (vt_sel/vt_enum `FFFF`)
   - GPT-OSS: parallel `FFFF` + enum hallucination (`gold_block`)
   - Gemma3: zero native support, perfect text
   - Mistral v_int pair: boundary confusion (`getWorldState` at x=15,y=15,z=15)

8. **Voxel tests are the real discriminator.** 25/32 models pass single/multi/parallel on baseline, but only 10/32 pass all voxel sub-checks. The schema complexity tests (enum adherence, integer boundaries, zero-param tools) reveal capability differences invisible to simpler tests.

9. **Measurement reproducibility is high.** 14/32 models are fully deterministic at the sub-check level across independent sweeps. 5/32 are nondeterministic (same total, shuffled sub-checks). 3/32 are server-unstable. Consistent failure signatures (parallel `FFFF`, v_int `FFFF`, GLM text `FFFF`) reproduce identically — these are confirmed model limitations, not noise.
