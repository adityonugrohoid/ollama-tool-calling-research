# GA — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| cogito-2.1:671b | P | P | P | T | T | TTTTT | PPPPP | 8/15 (7T) |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2 | P | P | P | P | P | PPPPP | PPPTT | 13/15 (2T) |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| cogito-2.1:671b | P | P | P | T | T | TTTTT | PPPTT | 6/15 (9T) |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2 | P | P | P | P | P | TTPPP | PPTTP | 11/15 (4T) |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| cogito-2.1:671b | P | P | P | T | T | TTTTT | TTTTT | 3/15 (12T) |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| cogito-2.1:671b | P | P | P | T | T | TTTTT | TTTTT | 3/15 (12T) |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2 | P | P | P | P | P | PPPPP | PPFTP | 13/15 (1T) |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| ministral-3:3b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| ministral-3:8b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| ministral-3:14b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| devstral-2:123b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| gemini-3-flash-preview | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| cogito-2.1:671b | PPPP | PPPP | PPPP | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | PPTT | PPTT | PPTT | PTTT | PTTT | 20/60 (40T) |
| kimi-k2.5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| kimi-k2-thinking | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| minimax-m2 | PPPP | PPPP | PPPP | PPPP | PPPP | PTPP | PTPP | PPPP | PPPP | PPPP | PPPP | PPPP | PTPF | TTPT | TPPP | 52/60 (7T) |
| kimi-k2:1t | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |

---

# GB — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | PTPFP | 13/15 (1T) |
| glm-5 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | FFFTF | 10/15 (1T) |
| glm-5 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| nemotron-3-nano:30b | P | P | P | F | P | PPPPP | FFFFP | 10/15 |
| glm-5 | P | P | P | P | P | PPPPP | TFFTF | 10/15 (2T) |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| glm-5 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| minimax-m2.1 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| minimax-m2.5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PFFF | PPPP | 57/60 |
| glm-4.6 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF | FFFF | PPPP | PPPP | 48/60 |
| nemotron-3-nano:30b | PPPP | PPPP | PPPP | PPFP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PFFF | TFFF | PFFF | FTFP | PFPF | 44/60 (2T) |
| glm-5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFTF | FFFF | FFFF | PFTF | FFFF | 41/60 (2T) |
| glm-4.7 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF | FFFF | FPPF | FFFF | 42/60 |
| qwen3-coder-next | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TTTT | TTTT | TTTT | TTTT | TTTT | 40/60 (20T) |
| qwen3-coder:480b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TTTT | TTTT | TTTT | TTTT | TTTT | 40/60 (20T) |

---

# GC — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-vl:235b-instruct | P | P | P | F | P | PPPPP | PPPPP | 14/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| mistral-large-3:675b | P | P | P | P | F | PPFPP | PPPPP | 13/15 |
| gpt-oss:120b | P | P | F | F | P | PFPPP | PPPPP | 12/15 |
| qwen3-vl:235b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-vl:235b-instruct | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gpt-oss:120b | P | P | F | P | P | PFPPP | PPPPP | 13/15 |
| qwen3-vl:235b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-vl:235b-instruct | P | P | P | F | P | PPPPP | PPPPP | 14/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gpt-oss:120b | P | P | F | T | P | PFPPP | PPPPP | 12/15 (1T) |
| qwen3-vl:235b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-vl:235b-instruct | P | P | P | F | P | PPPPP | PPPPP | 14/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gpt-oss:120b | P | P | F | P | P | PPPPP | PPPPP | 14/15 |
| qwen3-vl:235b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| qwen3-vl:235b-instruct | PPPP | PPPP | PPPP | FPFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 57/60 |
| devstral-small-2:24b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 56/60 |
| mistral-large-3:675b | PPPP | PPPP | PPPP | PPPP | FPPP | PPPP | PPPP | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 55/60 |
| gpt-oss:120b | PPPP | PPPP | FFFF | FPTP | PPPP | PPPP | FFFP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 51/60 (1T) |
| qwen3-vl:235b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| gemma3:4b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 |
| gemma3:12b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 |
| gemma3:27b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 |

---

# GD — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-next:80b | P | P | P | P | F | PPPPP | PPPPP | 14/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| qwen3.5:397b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gpt-oss:20b | P | P | F | P | P | TFPPP | PPFFF | 9/15 (1T) |
| deepseek-v3.1:671b | F | P | F | P | P | FPPPP | PPPFP | 11/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-next:80b | P | P | P | F | F | PPPPP | PPPPP | 13/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| qwen3.5:397b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gpt-oss:20b | P | P | F | P | P | TFPPP | PPPFP | 11/15 (1T) |
| deepseek-v3.1:671b | P | P | P | F | F | FPPPF | PPPPP | 11/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | PFPPP | 4/15 |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-next:80b | P | P | P | P | F | PPPPP | PPPPP | 14/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| qwen3.5:397b | P | P | P | P | P | PPPPP | TPPPP | 14/15 (1T) |
| gpt-oss:20b | P | P | F | P | P | PFPPP | PPPFP | 12/15 |
| deepseek-v3.1:671b | F | P | P | P | P | PFPPP | PPPPP | 13/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | PPPFP | 4/15 |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| qwen3-next:80b | P | P | P | P | F | PPPPP | PPPPP | 14/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| qwen3.5:397b | P | P | P | P | P | PPPPP | TPPPP | 14/15 (1T) |
| gpt-oss:20b | P | P | F | P | P | PTPPP | PPPFP | 12/15 (1T) |
| deepseek-v3.1:671b | P | P | P | F | P | FFPFP | PPPPP | 11/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | FPPFP | 3/15 |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| qwen3-next:80b | PPPP | PPPP | PPPP | PFPP | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 55/60 |
| rnj-1:8b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TTTT | PPPP | PPPP | PPPP | FFFF | PPPP | PPPP | 52/60 (4T) |
| qwen3.5:397b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPTT | PPPP | PPPP | PPPP | PPPP | 58/60 (2T) |
| gpt-oss:20b | PPPP | PPPP | FFFF | PPPP | PPPP | TTPP | FFFT | PPPP | PPPP | PPPP | PPPP | PPPP | FPPP | FFFF | FPPP | 44/60 (3T) |
| deepseek-v3.1:671b | FPFP | PPPP | FPPP | PFPF | PFPP | FFPF | PPFF | PPPP | PPPF | PFPP | PPPP | PPPP | PPPP | FPPP | PPPP | 46/60 |
| deepseek-v3.2 | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPF | PFPP | PPPP | PPFF | PPPP | 16/60 |
