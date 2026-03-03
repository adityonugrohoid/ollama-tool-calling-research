# P0 — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gpt-oss:20b | P | P | F | T | P | PFPPP | PPPFP | 11/15 (1T) |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gpt-oss:20b | P | P | F | P | P | TFPPP | PPPFP | 11/15 (1T) |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gpt-oss:20b | P | P | F | P | P | PFFPP | PPFFP | 10/15 |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| ministral-3:3b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemma3:4b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| ministral-3:8b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| rnj-1:8b | P | P | P | P | P | PPPTP | PPFPP | 13/15 (1T) |
| gemma3:12b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |
| gpt-oss:20b | P | P | F | P | P | PTPPP | PPPFP | 12/15 (1T) |
| ministral-3:14b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| devstral-small-2:24b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| gemma3:27b | F | F | F | F | F | FFFFF | PPPPP | 5/15 |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| ministral-3:3b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| gemma3:4b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 |
| ministral-3:8b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| rnj-1:8b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TTTT | PPPP | PPPP | PPPP | FFFF | PPPP | PPPP | 52/60 (4T) |
| gemma3:12b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 |
| gpt-oss:20b | PPPP | PPPP | FFFF | TPPP | PPPP | PTPP | FFFT | PPFP | PPPP | PPPP | PPPP | PPPP | PPFP | FFFF | PPPP | 44/60 (3T) |
| ministral-3:14b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| devstral-small-2:24b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 56/60 |
| gemma3:27b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 |

---

# P1 — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | FPFPF | 12/15 |
| qwen3-next:80b | P | P | P | P | F | PPPPP | PPPPP | 14/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| gpt-oss:120b | P | P | F | P | P | PFPPP | PPPPP | 13/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| qwen3-next:80b | P | P | P | T | F | PPPPP | PPPPP | 13/15 (1T) |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| gpt-oss:120b | P | P | F | F | P | PPPPP | PPPPP | 13/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | FPFPP | 13/15 |
| qwen3-next:80b | P | P | P | P | F | PPPPP | PPPPP | 14/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| gpt-oss:120b | P | P | F | P | P | PFPPP | PPPPP | 13/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| nemotron-3-nano:30b | P | P | P | P | P | PPPPP | FFTPF | 11/15 (1T) |
| qwen3-next:80b | P | P | P | P | F | PPPPP | PPPFP | 13/15 |
| qwen3-coder-next | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| gpt-oss:120b | P | P | F | P | P | PFPPP | PPPPP | 13/15 |
| devstral-2:123b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| gemini-3-flash-preview | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| nemotron-3-nano:30b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | PFPF | FFFT | PPPP | FFPF | 47/60 (1T) |
| qwen3-next:80b | PPPP | PPPP | PPPP | PTPP | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPF | PPPP | 54/60 (1T) |
| qwen3-coder-next | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TTTT | TTTT | TTTT | TTTT | TTTT | 40/60 (20T) |
| gpt-oss:120b | PPPP | PPPP | FFFF | PFPP | PPPP | PPPP | FPFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 52/60 |
| devstral-2:123b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| gemini-3-flash-preview | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |

---

# P2 — Expanded Sub-check Results

## S0T0 (stream=False, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| qwen3.5:397b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| qwen3-vl:235b | T | T | T | T | T | TTTTT | PPPPP | 5/15 (10T) |
| qwen3-vl:235b-instruct | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| deepseek-v3.1:671b | P | P | F | P | P | PPPPP | PPPPP | 14/15 |
| cogito-2.1:671b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | PFPFF | 2/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| glm-5 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| kimi-k2:1t | P | P | P | P | P | PPPPP | TPPPP | 14/15 (1T) |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S0T1 (stream=False, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2 | P | P | P | P | P | PPPTP | PPPPP | 14/15 (1T) |
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| qwen3.5:397b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| qwen3-vl:235b | T | T | T | T | T | TTTTT | PPPPP | 5/15 (10T) |
| qwen3-vl:235b-instruct | P | P | P | F | P | PPPPP | PPPPP | 14/15 |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| deepseek-v3.1:671b | F | P | F | F | F | PFPFP | PPPPP | 9/15 |
| cogito-2.1:671b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | FFFFF | 0/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFPPP | 13/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| glm-5 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S1T0 (stream=True, think=False)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| qwen3.5:397b | P | P | P | P | F | PPPPP | PPPPP | 14/15 |
| qwen3-vl:235b | T | T | T | T | T | TTTTT | PPPPP | 5/15 (10T) |
| qwen3-vl:235b-instruct | P | P | P | F | P | PPPPP | PPPPP | 14/15 |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| deepseek-v3.1:671b | P | P | P | P | F | PPFPP | PPFPP | 12/15 |
| cogito-2.1:671b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | FFFPP | 2/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| glm-5 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## S1T1 (stream=True, think=True)

| Model | single | multi | parallel | step | scale | voxel (sel/enum/int/zero/disc) | voxel_text (sel/enum/int/zero/disc) | Total |
|-------|--------|-------|----------|------|-------|------|------|------|
| minimax-m2 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| minimax-m2.1 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| minimax-m2.5 | P | P | P | P | P | PPPPP | PPPFP | 14/15 |
| qwen3.5:397b | P | P | P | P | P | PPPPP | PTPPP | 14/15 (1T) |
| qwen3-vl:235b | T | T | T | T | T | TTTTT | PPPPP | 5/15 (10T) |
| qwen3-vl:235b-instruct | P | P | P | F | P | PPPPP | PPPPP | 14/15 |
| qwen3-coder:480b | P | P | P | P | P | PPPPP | TTTTT | 10/15 (5T) |
| mistral-large-3:675b | P | P | P | P | P | PPFPP | PPPPP | 14/15 |
| deepseek-v3.1:671b | F | F | F | F | F | PFPPP | PPPPP | 9/15 |
| cogito-2.1:671b | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| deepseek-v3.2 | F | F | F | F | F | FFFFF | FPFFF | 1/15 |
| glm-4.6 | P | P | P | P | P | PPPPP | FFFPP | 12/15 |
| glm-4.7 | P | P | P | P | P | PPPPP | FFFFF | 10/15 |
| glm-5 | P | P | P | P | P | PPPPP | FFFPF | 11/15 |
| kimi-k2:1t | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2.5 | P | P | P | P | P | PPPPP | PPPPP | 15/15 |
| kimi-k2-thinking | P | P | P | P | P | PPPPP | PPPPP | 15/15 |

## Cumulative (all flag combos)

Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.

| Model | single | multi | parallel | step | scale | v_sel | v_enum | v_int | v_zero | v_disc | vt_sel | vt_enum | vt_int | vt_zero | vt_disc | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| minimax-m2 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PTPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 59/60 (1T) |
| minimax-m2.1 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PFFF | PPPP | 57/60 |
| minimax-m2.5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFPF | PPPP | 57/60 |
| qwen3.5:397b | PPPP | PPPP | PPPP | PPPP | PPFP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPT | PPPP | PPPP | PPPP | 58/60 (1T) |
| qwen3-vl:235b | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | TTTT | PPPP | PPPP | PPPP | PPPP | PPPP | 20/60 (40T) |
| qwen3-vl:235b-instruct | PPPP | PPPP | PPPP | PFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 57/60 |
| qwen3-coder:480b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TTTT | TTTT | TTTT | TTTT | TTTT | 40/60 (20T) |
| mistral-large-3:675b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 56/60 |
| deepseek-v3.1:671b | PFPF | PPPF | FFPF | PFPF | PFFF | PPPP | PFPF | PPFP | PFPP | PPPP | PPPP | PPPP | PPFP | PPPP | PPPP | 44/60 |
| cogito-2.1:671b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| deepseek-v3.2 | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PFFF | FFFP | PFFF | FFPF | FFPF | 5/60 |
| glm-4.6 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF | FPFF | PPPP | PPPP | 49/60 |
| glm-4.7 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF | FFFF | PPFF | FFFF | 42/60 |
| glm-5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF | FFFF | PFPP | FFFF | 43/60 |
| kimi-k2:1t | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | TPPP | PPPP | PPPP | PPPP | PPPP | 59/60 (1T) |
| kimi-k2.5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
| kimi-k2-thinking | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | 60/60 |
