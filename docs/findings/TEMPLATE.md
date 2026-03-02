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

### Test: Multi-tool (3 tools available)
- Result: [Pass/Fail]
- Notes: [...]

### Test: Parallel calls
- Result: [Pass/Fail]
- Notes: [...]

### Test: Multi-step loop (5 turns)
- Result: [Pass/Fail]
- Turns with native format: [e.g., 1-3]
- Turns with text format: [e.g., 4-5]
- Notes: [e.g., "Switched from native to text after turn 3"]

### Test: Streaming
- Result: [Pass/Fail]
- Notes: [...]

### Test: Tool count scaling
| Tools | Format | Parse Success |
|-------|--------|---------------|
| 1     |        |               |
| 3     |        |               |
| 5     |        |               |
| 8     |        |               |
| 10    |        |               |
| 15    |        |               |

### Test: Thinking + tools
- Result: [Pass/Fail]
- Thinking content present: [Yes/No]
- Corruption detected: [Yes/No]
- Notes: [...]

### Test: Text-based fallback
- Result: [Pass/Fail]
- Parse success rate: [X/3]
- Notes: [...]

## Summary
[1-2 sentence verdict on this model's tool calling reliability]
