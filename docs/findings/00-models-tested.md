# Models Tested

> Master list of all 32 models on Ollama Cloud, organized by priority tier.

## Summary

- **Total models on Ollama Cloud:** 32
- **With tools capability:** 29
- **Without tools capability:** 3 (gemma3 family — included for baseline comparison)
- **P0:** 9 models (small/fast, <30B)
- **P1:** 6 models (medium, 30B–130B)
- **P2:** 17 models (large, 200B+)

## P0 — Small/Fast (<30B)

Best for quick iteration and initial testing.

| Model | Size | Family | Capabilities | Status |
|-------|------|--------|-------------|--------|
| ministral-3:3b | 3B | mistral3 | tools, vision | Pending |
| gemma3:4b | 4B | gemma3 | vision | Pending |
| ministral-3:8b | 8B | mistral3 | tools, vision | Pending |
| rnj-1:8b | 8B | gemma3 | tools | Pending |
| gemma3:12b | 12B | gemma3 | vision | Pending |
| gpt-oss:20b | 20B | gptoss | tools, thinking | Pending |
| ministral-3:14b | 14B | mistral3 | tools, vision | Pending |
| devstral-small-2:24b | 24B | mistral3 | tools, vision | Pending |
| gemma3:27b | 27B | gemma3 | vision | Pending |

## P1 — Medium (30B–130B)

Deeper investigation, diverse model families.

| Model | Size | Family | Capabilities | Status |
|-------|------|--------|-------------|--------|
| nemotron-3-nano:30b | 30B | nemotron-3-nano | tools, thinking | Pending |
| qwen3-next:80b | 80B | qwen3next | tools, thinking | Pending |
| qwen3-coder-next | 80B | qwen3next | tools | Pending |
| gpt-oss:120b | 120B | gptoss | tools, thinking | Pending |
| devstral-2:123b | 123B | mistral3 | tools | Pending |
| gemini-3-flash-preview | ? | gemini | tools, thinking | Pending |

## P2 — Large (200B+)

Comprehensive coverage, all remaining models.

| Model | Size | Family | Capabilities | Status |
|-------|------|--------|-------------|--------|
| minimax-m2 | 230B | minimax-m2 | tools | Pending |
| minimax-m2.1 | 230B | minimax-m2 | tools, thinking | Pending |
| minimax-m2.5 | 230B | minimax-m2 | tools, thinking | Pending |
| qwen3-vl:235b | 235B | qwen3vlmoe | tools, thinking, vision | Pending |
| qwen3-vl:235b-instruct | 235B | qwen3vlmoe | tools, vision | Pending |
| glm-4.6 | 357B | glm4 | tools, thinking | Pending |
| glm-4.7 | 357B | glm4 | tools, thinking | Pending |
| qwen3.5:397b | 397B | qwen3.5 | tools, thinking, vision | Pending |
| qwen3-coder:480b | 480B | qwen3moe | tools | Pending |
| mistral-large-3:675b | 675B | mistral3 | tools, vision | Pending |
| deepseek-v3.1:671b | 671B | deepseek2 | tools, thinking | Pending |
| cogito-2.1:671b | 671B | deepseek2 | tools, thinking | Pending |
| deepseek-v3.2 | 671B | deepseek3.2 | tools, thinking | Pending |
| glm-5 | 756B | glm5 | tools, thinking | Pending |
| kimi-k2:1t | 1T | kimi-k2 | tools | Pending |
| kimi-k2.5 | 1T | kimi-k2 | tools, thinking, vision | Pending |
| kimi-k2-thinking | 1T | kimi-k2 | tools, thinking | Pending |

## Priority Definitions

- **P0 (Small/Fast):** Models under 30B. Quick to run, good for iterating on test design. Includes 3 gemma3 models without tool support for baseline comparison.
- **P1 (Medium):** Models 30B–130B. Deeper investigation of tool calling behavior across diverse families.
- **P2 (Large):** Models 200B+. Full coverage of all available models on Ollama Cloud.

## Notes

- All models tested via Ollama Cloud API (`https://ollama.com`)
- 3 gemma3 models lack native tool support — expected to fail native tests, useful for text-fallback baseline
- Model availability depends on cloud instance state; unavailable models are auto-skipped
- Source: `model-library.json` fetched 2026-03-02 from `/api/tags`
