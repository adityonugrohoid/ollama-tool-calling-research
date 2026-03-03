# Ollama Tool Calling Research

A research repository documenting tool calling behavior across 32 open-source LLMs served through Ollama Cloud API. Includes reproducible test scripts, per-model behavior logs, and text-based tool calling as a standardized fallback.

## Key Results

**32 models** tested across **7 tests** and **4 flag combinations** (`stream` x `think`), producing **60 scored checks per model**. Two independent sweeps (v3 + v4) totaling **1,792 runs**.

### Top Model Families by Stable Performance

Ranked by: all members score 55+/60, rock-stable across sweeps, flag-agnostic (same behavior regardless of `stream`/`think` settings).

| Rank | Family | Models | v4 Score | Badges |
|------|--------|--------|----------|--------|
| 1 | **Ministral** | 3:3b, 3:8b, 3:14b | 60/60 (all 3) | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 2 | **Kimi** | k2.5, k2-thinking, k2:1t | 60/60 (all 3) | `PERFECT` `DUAL-LAYER` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 3 | **Gemini** | 3-flash-preview | 60/60 | `PERFECT` `DUAL-LAYER` `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 4 | **Devstral** | 2:123b, small-2:24b | 60, 56 | `ROCK-STABLE` `DETERMINISTIC` `FLAG-AGNOSTIC` |
| 5 | **Qwen VL** | vl:235b, vl:235b-instruct | 60, 57 | `ROCK-STABLE` (instruct) |

**Why Ministral ranks #1:** All three sizes (3B, 8B, 14B) achieve identical perfect scores — every sub-check is `PPPP` across both sweeps, bit-for-bit deterministic. The 3B model matches 1T-parameter models, making it the strongest evidence against size-quality correlation in the dataset.

### Findings at a Glance

1. **No size-quality correlation** — ministral-3:3b (3B) = 60/60, deepseek-v3.2 (671B) = 16/60
2. **Streaming degrades, never improves** — `stream=true` adds failure risk, never rescues a failing model
3. **Thinking is a wild card** — `think=true` can help OR hurt specific tests (deepseek-v3.1 alternation)
4. **Layer independence** — native and text-based tool calling are orthogonal capabilities
5. **Flag agnosticism = reliability** — all 10 perfect models are completely flag-agnostic
6. **Voxel tests are the real discriminator** — 25/32 pass simple tests, only 10/32 pass all voxel sub-checks
7. **Measurement reproducibility is high** — 14/32 models are fully deterministic at sub-check level across sweeps

### Badge Legend

| Category | Badges |
|----------|--------|
| **Performance** | `PERFECT` 60/60 · `NEAR-PERFECT` 55-59 · `FUNCTIONAL` 40-54 · `MINIMAL` <40 |
| **Layer** | `DUAL-LAYER` both pass · `NATIVE-ONLY` · `TEXT-ONLY` · `MIXED-LAYER` |
| **Stability** | `ROCK-STABLE` delta=0 · `DETERMINISTIC` identical sub-checks across sweeps |
| **Flags** | `FLAG-AGNOSTIC` no stream/think effect · `STREAM-SENSITIVE` · `THINK-ALTERNATING` |
| **Failure** | `ENUM-HALLUCINATOR` · `BOUNDARY-CONFUSED` · `PARALLEL-INCAPABLE` · `SERVER-BLOCKED` |

### Score Distribution

| Tier | Range | Models | % |
|------|-------|--------|---|
| `PERFECT` | 60/60 | 10 | 31% |
| `NEAR-PERFECT` | 55-59 | 6 | 19% |
| `FUNCTIONAL` | 40-54 | 11 | 34% |
| `MINIMAL` | <40 | 5 | 16% |

Full report: [`observations/summaries/research_report.md`](observations/summaries/research_report.md)

## Methodology

### Test Suite (7 tests, 3 tiers)

| Tier | Test | Tools | What it surfaces |
|------|------|-------|-----------------|
| **Core** | single_tool | 1 | Cannot invoke any tool |
| **Core** | multi_tool | 3 | Cannot select from set |
| **Core** | parallel_calls | 3 | Cannot return multiple calls |
| **Stress** | multi_step | 1 x 5 turns | Format instability over time |
| **Stress** | tool_count_scaling | 1-15 | Breaks under tool proliferation |
| **Schema** | voxel_tools | 4 (native) | Schema constraint violations (5 sub-checks) |
| **Schema** | voxel_tools_text | 4 (text) | Text fallback schema violations (5 sub-checks) |

### Flag Matrix (4 combinations per test)

```
                 think=false          think=true
stream=false     S0T0 (baseline)      S0T1 (thinking interference)
stream=true      S1T0 (streaming)     S1T1 (combined stress)
```

7 tests x 4 combos = 28 runs per model. Voxel tests expand to 5 sub-checks each, producing **60 total checks per model**.

All tests use `temperature=0`, `seed=42` for reproducibility. Context window uses each model's default.

### Model Groups (behavior-based)

| Group | Pattern | Count | Description |
|-------|---------|-------|-------------|
| **GA** | All P (60/60) | 10 | Native 40/40, text 20/20 |
| **GB** | Native P, text varies | 8 | Native perfect, text has confirmed F |
| **GC** | Text P, native varies | 8 | Text perfect, native has confirmed F |
| **GD** | Both have F | 6 | Both layers have confirmed failures |

## Setup

```bash
git clone https://github.com/adityonugrohoid/ollama-tool-calling-research.git
cd ollama-tool-calling-research

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env with your Ollama Cloud API key and host
```

## Running Tests

```bash
# Run all tests against GA models (default, all 4 flag combos)
python run_all.py

# Run specific group
python run_all.py --models gb

# Run baseline only against one model
python run_all.py --models cogito-2.1:671b --flags S0T0

# Run all 4 combos against one model
python run_all.py --models cogito-2.1:671b

# Run specific tests against specific models
python run_all.py --models gpt-oss:20b,ministral-3:8b --tests single_tool,multi_tool

# Run all tests against all 32 models
python run_all.py --models all
```

## Project Structure

```
ollama-tool-calling-research/
├── run_all.py                      # Entry point — --models, --tests, --flags
├── src/
│   ├── ollama_client.py            # Ollama SDK wrapper, retry logic, raw logging
│   ├── response_layers.py          # Layer-aware extraction (native/text/thinking)
│   ├── stream_collector.py         # Streaming chunk collector
│   ├── tool_parser_native.py       # Parse native tool_calls
│   ├── tool_parser_text.py         # Parse text-based tool calls (XML/JSON)
│   └── test_runner.py              # Test orchestrator (model x test x flag loop)
├── tests/
│   ├── config.py                   # Model groups (GA-GD), tool defs, flag combos
│   ├── test_single_tool.py         # Basic tool invocation
│   ├── test_multi_tool.py          # Tool selection from set
│   ├── test_parallel_calls.py      # Parallel tool calls
│   ├── test_multi_step.py          # 5-turn format consistency
│   ├── test_tool_count_scaling.py  # 1-15 tool scaling
│   ├── test_voxel_tools.py         # Complex native schemas (5 sub-checks)
│   └── test_voxel_tools_text.py    # Complex text fallback (5 sub-checks)
├── scripts/
│   └── generate_subcheck_tables.py # Parse sweep results → sub-check tables
├── observations/
│   ├── raw/                        # Raw JSON responses (gitignored)
│   └── summaries/                  # Research deliverables (tracked)
│       ├── research_report.md      # Full research report
│       ├── v4_subcheck_tables.md   # v4 per-sub-check P/F/T data
│       ├── v3_subcheck_tables.md   # v3 per-sub-check P/F/T data
│       ├── model_groups.md         # Group definitions
│       └── g{a,b,c,d}_v4_flagmatrix.md  # v4 sweep results
├── requirements.txt
└── .env.example
```

## License

Research use. No license specified yet.
