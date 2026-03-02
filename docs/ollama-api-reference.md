# Ollama Tool Calling Research — API Reference & Project Plan

> **Last updated:** March 2, 2026
> **Source:** [docs.ollama.com](https://docs.ollama.com/api/introduction) · [github.com/ollama/ollama](https://github.com/ollama/ollama/blob/main/docs/api.md)

---

## 1. Repo Overview

### Recommended Name

**`ollama-tool-calling-research`**

Alternative options:
- `ollama-toolcall-bench` (shorter, benchmark-focused)
- `open-llm-tool-calling-lab` (broader scope)

### Purpose

A research repository documenting the inconsistencies of native tool calling across open-source LLMs served through Ollama. Includes reproducible test scripts, per-model behavior logs, and a text-based tool calling reference implementation as a standardized fallback.

### Repo Structure

```
ollama-tool-calling-research/
├── README.md                          # Project overview, findings summary
├── docs/
│   ├── ollama-api-reference.md        # This file — full API surface
│   ├── research-methodology.md        # How tests are structured
│   └── findings/
│       ├── 00-models-tested.md        # Master list of models + versions
│       ├── 01-qwen3-8b.md            # Per-model observation logs
│       ├── 02-llama3.1-8b.md
│       ├── 03-mistral-7b.md
│       ├── 04-gemma2-9b.md
│       ├── 05-deepseek-r1.md
│       └── ...
├── tests/
│   ├── config.py                      # Ollama connection, model list
│   ├── test_single_tool.py            # Single tool, single call
│   ├── test_multi_tool.py             # Multiple tools available
│   ├── test_parallel_calls.py         # Parallel tool invocation
│   ├── test_multi_step.py             # Multi-turn tool loop
│   ├── test_streaming_tools.py        # stream=True with tools
│   ├── test_tool_count_scaling.py     # 1,3,5,8,10,15 tools
│   ├── test_thinking_with_tools.py    # think=True + tools
│   └── test_text_fallback.py          # Text-based tool calling baseline
├── observations/
│   ├── raw/                           # Raw JSON responses per test run
│   └── summaries/                     # Aggregated results tables
├── src/
│   ├── ollama_client.py               # Thin wrapper around Ollama API
│   ├── tool_parser_native.py          # Native tool_calls parser
│   ├── tool_parser_text.py            # Text-based XML/JSON parser
│   └── test_runner.py                 # Orchestrates all tests, logs results
├── requirements.txt
└── .env.example                       # OLLAMA_API_KEY, OLLAMA_HOST
```

---

## 2. Ollama API Reference

### 2.1 Base URLs

| Environment | Base URL |
|---|---|
| Local | `http://localhost:11434/api` |
| Cloud (ollama.com) | `https://ollama.com/api` |

### 2.2 Authentication

**Local:** No authentication required.

**Cloud:** Requires an Ollama account and API key.

```bash
# CLI sign-in
ollama signin

# API usage with key
curl https://ollama.com/api/chat \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -d '{ "model": "gpt-oss:120b", "messages": [...], "stream": false }'
```

**Python SDK (cloud):**
```python
import os
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY")}
)
```

### 2.3 Core Endpoints

#### `POST /api/generate` — Text Completion

Single-prompt text generation. No conversation history.

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

**Key parameters:**
| Parameter | Type | Description |
|---|---|---|
| `model` | string | **Required.** Model name |
| `prompt` | string | The prompt to generate from |
| `system` | string | System message (overrides Modelfile) |
| `template` | string | Prompt template (overrides Modelfile) |
| `context` | array | Context from previous `/generate` call (short-term memory) |
| `stream` | bool | Default `true`. Set `false` for single response |
| `format` | string/object | `"json"` or a JSON schema object |
| `options` | object | Model parameters (temperature, num_ctx, etc.) |
| `keep_alive` | string | How long to keep model loaded (e.g. `"5m"`, `"-1"` for forever) |
| `think` | bool | Enable thinking/reasoning trace |

**Response fields:**
| Field | Description |
|---|---|
| `response` | Generated text |
| `thinking` | Reasoning trace (if `think: true`) |
| `done` | Whether generation is complete |
| `done_reason` | `"stop"`, `"length"`, etc. |
| `total_duration` | Total time in nanoseconds |
| `load_duration` | Model load time |
| `prompt_eval_count` | Number of prompt tokens |
| `prompt_eval_duration` | Prompt evaluation time |
| `eval_count` | Number of generated tokens |
| `eval_duration` | Generation time |

---

#### `POST /api/chat` — Chat Completion ⭐ (Primary for tool calling)

Multi-turn conversation with message history. **This is the endpoint used for tool calling.**

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen3",
  "messages": [
    {"role": "user", "content": "What is the temperature in Tokyo?"}
  ],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_temperature",
        "description": "Get the current temperature for a city",
        "parameters": {
          "type": "object",
          "required": ["city"],
          "properties": {
            "city": {"type": "string", "description": "The name of the city"}
          }
        }
      }
    }
  ]
}'
```

**Key parameters:**
| Parameter | Type | Description |
|---|---|---|
| `model` | string | **Required.** Model name |
| `messages` | array | **Required.** Conversation messages |
| `tools` | array | Tool definitions (function schemas) |
| `stream` | bool | Default `true`. **Use `false` when tools are present** |
| `format` | string/object | `"json"` or JSON schema for structured output |
| `options` | object | Model parameters |
| `keep_alive` | string | How long to keep model loaded |
| `think` | bool | Enable thinking trace |

**Message roles:**
| Role | Purpose |
|---|---|
| `system` | System instructions |
| `user` | User input |
| `assistant` | Model response (may include `tool_calls`) |
| `tool` | Tool execution result (include `tool_name` and `content`) |

**Response — successful tool call:**
```json
{
  "model": "qwen3",
  "created_at": "2026-03-02T...",
  "message": {
    "role": "assistant",
    "content": "",
    "thinking": "...",
    "tool_calls": [
      {
        "function": {
          "name": "get_temperature",
          "arguments": {"city": "Tokyo"}
        }
      }
    ]
  },
  "done": true,
  "done_reason": "stop",
  "total_duration": 3244883583,
  "eval_count": 18
}
```

**Response — no tool call (text response):**
```json
{
  "message": {
    "role": "assistant",
    "content": "The temperature in Tokyo is typically...",
    "tool_calls": null
  },
  "done": true
}
```

**Feeding tool results back:**
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen3",
  "messages": [
    {"role": "user", "content": "What is the temperature in Tokyo?"},
    {
      "role": "assistant",
      "tool_calls": [{
        "function": {"name": "get_temperature", "arguments": {"city": "Tokyo"}}
      }]
    },
    {"role": "tool", "tool_name": "get_temperature", "content": "22°C"}
  ],
  "stream": false
}'
```

---

#### `POST /api/embed` — Generate Embeddings

```bash
curl http://localhost:11434/api/embed -d '{
  "model": "all-minilm",
  "input": "Why is the sky blue?"
}'
```

| Parameter | Type | Description |
|---|---|---|
| `model` | string | **Required.** Model name |
| `input` | string/array | Text(s) to embed |
| `options` | object | Model parameters |
| `keep_alive` | string | How long to keep model loaded |

---

### 2.4 Model Management Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/tags` | GET | List locally available models |
| `/api/ps` | GET | List currently running/loaded models |
| `/api/show` | POST | Show model details (parameters, template, license) |
| `/api/create` | POST | Create a model from a Modelfile |
| `/api/copy` | POST | Copy/alias a model |
| `/api/pull` | POST | Download a model from Ollama library |
| `/api/push` | POST | Push a model to Ollama library |
| `/api/delete` | DELETE | Delete a local model |
| `/api/blobs/:digest` | POST | Upload a blob (GGUF file) |
| `/api/version` | GET | Get Ollama version |

**Useful for research — list models:**
```bash
curl http://localhost:11434/api/tags
```

Returns model name, size, family, parameter count, quantization level, and modification date.

**Useful for research — show model details:**
```bash
curl http://localhost:11434/api/show -d '{"model": "qwen3:8b"}'
```

Returns the full Modelfile, template, parameters, and system prompt.

---

### 2.5 OpenAI-Compatible Endpoints

Ollama exposes an OpenAI-compatible API layer for drop-in replacement with existing tooling.

| Ollama Endpoint | OpenAI Equivalent |
|---|---|
| `/v1/chat/completions` | Chat completions |
| `/v1/completions` | Text completions (legacy) |
| `/v1/embeddings` | Embeddings |
| `/v1/models` | List models |
| `/v1/responses` | Responses API (newer) |

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"  # required but ignored for local
)

response = client.chat.completions.create(
    model="qwen3:8b",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### 2.6 Anthropic-Compatible Endpoint

Ollama also supports Anthropic API format (noted in docs sidebar, newer addition).

---

### 2.7 Capabilities Reference

#### Tool Calling

- Pass `tools` array in `/api/chat` request
- Tools use OpenAI-style function schema format
- Supports single tool call, parallel tool calls, and multi-turn loops
- **Critical:** Use `stream: false` when tools are present to avoid silent failures
- Streaming tool calls are supported but unreliable across models

#### Structured Outputs

- Pass `format: "json"` for basic JSON mode
- Pass `format: { JSON schema }` for schema-constrained output
- Works with Pydantic `model_json_schema()` in Python
- Independent from tool calling — can be used as alternative strategy

#### Thinking Mode

- Pass `think: true` to enable reasoning traces
- Supported models: qwen3, deepseek-r1, gpt-oss
- GPT-OSS uses levels: `"low"`, `"medium"`, `"high"` instead of boolean
- Thinking output in `message.thinking` field, final answer in `message.content`
- Can combine with tool calling: model thinks, then calls tool

#### Web Search (Built-in Tool)

- Ollama provides `web_search` and `web_fetch` as built-in tools via Python SDK
- Can be combined with custom tools in the same request

---

## 3. Key Model Parameters for Testing

These are set via the `options` field:

| Parameter | Default | Description |
|---|---|---|
| `temperature` | 0.8 | Creativity (lower = more deterministic) |
| `num_ctx` | 2048 | Context window size |
| `top_p` | 0.9 | Nucleus sampling threshold |
| `top_k` | 40 | Top-k sampling |
| `repeat_penalty` | 1.1 | Repetition penalty |
| `seed` | 0 | Random seed (set for reproducibility!) |
| `num_predict` | -1 | Max tokens to generate (-1 = unlimited) |

**For reproducible research, always set:**
```python
options = {
    "temperature": 0,
    "seed": 42,
    "num_ctx": 4096
}
```

---

## 4. Known Issues to Investigate

These are documented issues from Ollama's GitHub and community that form the basis of our research:

### 4.1 Model switches mid-conversation

**Observed:** Qwen models sometimes use native tool calling for the first few turns, then switch to outputting tool calls as text mid-conversation. This breaks parsers that expect consistent format throughout.

**Test:** `test_multi_step.py` — Run 5+ turn tool calling loops and log format per turn.

### 4.2 Tool count threshold

**Observed:** Some models (notably Qwen3-coder) switch from native JSON tool calls to XML-style text output when more than ~5 tools are provided. The threshold varies by model.

**Test:** `test_tool_count_scaling.py` — Incrementally add tools (1, 3, 5, 8, 10, 15) and observe output format.

### 4.3 Streaming silently drops tool calls

**Observed:** With `stream: true`, some models return empty content with `finish_reason: "stop"` instead of tool calls. The tool call is lost entirely.

**Test:** `test_streaming_tools.py` — Compare `stream: true` vs `stream: false` for same prompt.

### 4.4 Thinking mode interference

**Observed:** Models with thinking enabled (e.g., gpt-oss) sometimes emit thinking tokens inside the tool call JSON, corrupting it.

**Test:** `test_thinking_with_tools.py` — Enable `think: true` with tool calls.

### 4.5 Missing tool call prefix

**Observed:** Some models omit the expected tool call prefix tokens, producing raw JSON without wrapper. Ollama's parser may miss these.

**Test:** Log raw responses and check for prefix presence.

### 4.6 Hallucinated parameters

**Observed:** Models sometimes produce tool calls with parameters not in the schema, or with incorrect types.

**Test:** Validate all returned arguments against the provided tool schema.

### 4.7 Text-as-JSON fallback reliability

**Observed:** When models output tool calls as text (not native), the JSON is sometimes malformed — missing braces, trailing commas, or wrapped in markdown code blocks.

**Test:** `test_text_fallback.py` — Force text-based tool calling and measure parse success rate.

---

## 5. Observation Log Template

Each model gets a finding document with this structure:

```markdown
# Model: [name:tag]

## Metadata
- Family: [e.g., qwen2]
- Parameter size: [e.g., 7.6B]
- Quantization: [e.g., Q4_K_M]
- Ollama version tested: [e.g., 0.17.4]
- Date tested: [YYYY-MM-DD]

## Tool Calling Support
- Native tool calling: [Yes/No/Partial]
- Parallel calls: [Yes/No]
- Max reliable tool count: [number]
- Stream + tools: [Works/Fails/Partial]
- Think + tools: [Works/Fails/Partial]

## Observations

### Test: Single tool call
- Result: [Pass/Fail]
- Notes: [...]
- Raw response: [link to raw/model_test_single.json]

### Test: Multi-tool (5 tools available)
- Result: [Pass/Fail]
- Notes: [...]

### Test: Multi-step loop (5 turns)
- Result: [Pass/Fail]
- Turns with native format: [e.g., 1-3]
- Turns with text format: [e.g., 4-5]
- Notes: "Switched from native to text after turn 3"

### Test: Streaming
- Result: [Pass/Fail]
- Notes: [...]

### Test: Tool count scaling
| Tools | Format | Parse Success |
|-------|--------|---------------|
| 1     | native | ✅            |
| 3     | native | ✅            |
| 5     | native | ✅            |
| 8     | text   | ⚠️ partial    |
| 10    | text   | ❌            |
| 15    | text   | ❌            |

## Summary
[1-2 sentence verdict on this model's tool calling reliability]
```

---

## 6. Models to Test (Priority Order)

Based on popularity in Ollama library and known tool calling support:

| Priority | Model | Params | Known Tool Support |
|----------|-------|--------|--------------------|
| 🔴 P0 | qwen3:8b | 8B | Yes — known mid-conversation switching |
| 🔴 P0 | llama3.1:8b | 8B | Yes — generally reliable |
| 🔴 P0 | mistral:7b | 7B | Yes — streaming issues reported |
| 🟡 P1 | gpt-oss:20b | 20B | Yes — thinking interference |
| 🟡 P1 | gemma2:9b | 9B | Limited |
| 🟡 P1 | deepseek-r1:8b | 8B | Thinking model — tool calling unclear |
| 🟡 P1 | qwen2.5:7b | 7B | Older — known failures |
| 🟢 P2 | llama3.2:3b | 3B | Small — stress test |
| 🟢 P2 | phi4:14b | 14B | Microsoft — less documented |
| 🟢 P2 | devstral-small | varies | Newer — community reports positive |

---

## 7. Python SDK Quick Reference

```bash
pip install ollama
```

```python
from ollama import chat

# Basic chat
response = chat(model="qwen3:8b", messages=[...])

# With tools
response = chat(
    model="qwen3:8b",
    messages=[{"role": "user", "content": "What's the weather?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "required": ["city"],
                "properties": {
                    "city": {"type": "string"}
                }
            }
        }
    }]
)

# Check for tool calls
if response.message.tool_calls:
    for tc in response.message.tool_calls:
        print(tc.function.name, tc.function.arguments)
else:
    print(response.message.content)
```

**Cloud client:**
```python
from ollama import Client
import os

client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.environ["OLLAMA_API_KEY"]}
)

response = client.chat(
    model="gpt-oss:120b",
    messages=[...],
    tools=[...],
    stream=False
)
```

---

## 8. References

- [Ollama API Introduction](https://docs.ollama.com/api/introduction)
- [Ollama Chat Endpoint](https://docs.ollama.com/api/chat)
- [Ollama Tool Calling Docs](https://docs.ollama.com/capabilities/tool-calling)
- [Ollama Structured Outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [Ollama Thinking](https://docs.ollama.com/capabilities/thinking)
- [Ollama Streaming](https://docs.ollama.com/capabilities/streaming)
- [Ollama Cloud](https://docs.ollama.com/cloud)
- [Ollama OpenAI Compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama Modelfile Reference](https://docs.ollama.com/modelfile)
- [Ollama GitHub — API source](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Ollama GitHub — Issues (tool calling)](https://github.com/ollama/ollama/issues?q=tool+calling)
- [Ollama Blog — Streaming Tool Calls](https://ollama.com/blog/streaming-tool)
