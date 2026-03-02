# Ollama Tool Calling Research

A research repository documenting the inconsistencies of native tool calling across open-source LLMs served through Ollama. Includes reproducible test scripts, per-model behavior logs, and a text-based tool calling reference implementation as a standardized fallback.

## Why This Exists

Native tool calling in open-source LLMs is unreliable. Models behave differently depending on the number of tools, conversation length, streaming mode, and thinking mode. This repo systematically tests and documents these failure modes so builders can make informed decisions.

## Known Issues Under Investigation

| # | Issue | Test |
|---|-------|------|
| 1 | **Mid-conversation format switching** — Models start with native tool calls, then switch to text output mid-conversation | `test_multi_step.py` |
| 2 | **Tool count threshold** — Models switch from native JSON to XML/text when too many tools are provided | `test_tool_count_scaling.py` |
| 3 | **Streaming drops tool calls** — `stream=true` silently loses tool calls, returning empty content | `test_streaming_tools.py` |
| 4 | **Thinking mode interference** — Thinking tokens corrupt tool call JSON | `test_thinking_with_tools.py` |
| 5 | **Missing tool call prefix** — Raw JSON without expected wrapper tokens | All tests (raw response logging) |
| 6 | **Hallucinated parameters** — Tool calls include parameters not in the schema | `test_single_tool.py`, `test_multi_tool.py` |
| 7 | **Text-as-JSON malformation** — Text-based tool calls have broken JSON (missing braces, trailing commas, markdown wrapping) | `test_text_fallback.py` |

## Models Tested

**32 models** across all Ollama Cloud offerings (29 with tools, 3 without).

| Tier | Count | Size Range | Description |
|------|-------|-----------|-------------|
| P0 | 9 | 3B–27B | Small/fast — quick iteration, includes 3 gemma3 (no tools) for baseline |
| P1 | 6 | 30B–130B | Medium — diverse families (Nvidia, Qwen, GPT-OSS, Mistral, Google) |
| P2 | 17 | 230B–1T | Large — full coverage (DeepSeek, GLM, Kimi, MiniMax, Qwen-VL) |

See [docs/findings/00-models-tested.md](docs/findings/00-models-tested.md) for the full model list.

## Setup

```bash
# Clone
git clone https://github.com/YOUR_USER/ollama-tool-calling-research.git
cd ollama-tool-calling-research

# Virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your Ollama Cloud API key and host
```

## Running Tests

```bash
# Run all tests against P0 models (default)
python run_all.py

# Run specific tests against specific models
python run_all.py --models gpt-oss:20b,ministral-3:8b --tests test_single_tool,test_multi_tool

# Run all tests against a single model
python run_all.py --models gpt-oss:20b
```

### Output

- **Terminal:** Rich-formatted summary matrix (models x tests) with pass/fail/error
- **Raw responses:** Saved to `observations/raw/{model}_{test}_{timestamp}.json`
- **Summary reports:** Saved to `observations/summaries/{timestamp}_results.md`

## Test Design

All tests use:
- `temperature=0` and `seed=42` for reproducibility
- `stream=false` by default (unless testing streaming)
- Graceful error handling — a model crash is logged, not propagated
- Both native and text-based tool call parsing

See [docs/research-methodology.md](docs/research-methodology.md) for full methodology.

## Project Structure

```
ollama-tool-calling-research/
├── run_all.py                    # Entry point — run tests
├── src/
│   ├── ollama_client.py          # Ollama API wrapper with raw response logging
│   ├── tool_parser_native.py     # Parse native tool_calls
│   ├── tool_parser_text.py       # Parse text-based tool calls (XML/JSON)
│   └── test_runner.py            # Test orchestrator
├── tests/
│   ├── config.py                 # Connection config, model lists, tool definitions
│   ├── test_single_tool.py       # Single tool, single call
│   ├── test_multi_tool.py        # Multiple tools available
│   ├── test_parallel_calls.py    # Parallel tool invocation
│   ├── test_multi_step.py        # Multi-turn tool loop
│   ├── test_streaming_tools.py   # stream=true with tools
│   ├── test_tool_count_scaling.py# Tool count scaling (1-15)
│   ├── test_thinking_with_tools.py# think=true + tools
│   └── test_text_fallback.py     # Text-based tool calling baseline
├── observations/
│   ├── raw/                      # Raw JSON responses (gitignored)
│   └── summaries/                # Aggregated results tables
├── docs/
│   ├── ollama-api-reference.md   # Full API reference
│   ├── research-methodology.md   # Test design docs
│   └── findings/                 # Per-model observation logs
├── requirements.txt
└── .env.example
```

## License

Research use. No license specified yet.
