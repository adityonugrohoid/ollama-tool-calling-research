# Model Groups — Based on P0/P1/P2 Flag Matrix Results + Reruns

32 models scored on 60 checks each: 40 native checks (5 single tests + 5 voxel sub-checks, across 4 flag combos) and 20 text checks (5 voxel_text sub-checks, across 4 flag combos).

Values: P=pass, F=fail (model error), T=transient (server 500/503/-1 error).

Rerun results incorporated — 7 rerun candidates resolved, T markers reclassified.

---

## Group A: All P (60/60) — 10 models

Native 40/40 P, text 20/20 P. No failures, no transient errors.

| Model | Sweep | Size | Rerun |
|-------|-------|------|-------|
| ministral-3:3b | P0 | 3B | — |
| ministral-3:8b | P0 | 8B | — |
| ministral-3:14b | P0 | 14B | — |
| devstral-2:123b | P1 | 123B | — |
| gemini-3-flash-preview | P1 | unknown | — |
| cogito-2.1:671b | P2 | 671B | — |
| kimi-k2.5 | P2 | 1T | — |
| kimi-k2-thinking | P2 | 1T | — |
| minimax-m2 | P2 | 230B | v_zero S0T1: T→P, migrated from B |
| kimi-k2:1t | P2 | 1T | vt_sel S0T0: T→P, migrated from B |

---

## Group B: All native P (40/40), text varies — 8 models

Native layer is perfect across all 4 flag combos. Text layer has confirmed F failures.

| Model | Sweep | Size | Native | Text (20) | Total | Text failure detail | Rerun |
|-------|-------|------|--------|-----------|-------|---------------------|-------|
| minimax-m2.1 | P2 | 230B | 40P | 17P+3F | 57/60 | vt_zero PFFF | — |
| minimax-m2.5 | P2 | 230B | 40P | 17P+3F | 57/60 | vt_zero FFPF | — |
| glm-4.6 | P2 | 357B | 40P | 9P+11F | 49/60 | vt_sel FFFF, vt_enum FFFF, vt_int FPFF | — |
| nemotron-3-nano:30b | P1 | 30B | 40P | 7P+12F+1T | 47/60 (1T) | vt_sel FFFF, vt_int FFFT, vt_disc FFPF | — (1T won't change group) |
| glm-5 | P2 | 756B | 40P | 3P+17F | 43/60 | vt_sel FFFF, vt_enum FFFF, vt_int FFFF, vt_disc FFFF | — |
| glm-4.7 | P2 | 357B | 40P | 2P+18F | 42/60 | vt_sel FFFF, vt_enum FFFF, vt_int FFFF, vt_zero PPFF, vt_disc FFFF | — |
| qwen3-coder-next | P1 | 80B | 40P | 0P+20F | 40/60 | All vt_* FFFF | T→F: server now responds, model fails all text sub-checks. Migrated from Rerun. |
| qwen3-coder:480b | P2 | 480B | 40P | 0P+20F | 40/60 | All vt_* FFFF | T→F: same as qwen3-coder-next. Migrated from Rerun. |

---

## Group C: All text P (20/20), native varies — 8 models

Text fallback layer is perfect across all 4 flag combos. Native layer has confirmed F failures.

| Model | Sweep | Size | Native (40) | Text | Total | Native failure detail | Rerun |
|-------|-------|------|-------------|------|-------|-----------------------|-------|
| qwen3-vl:235b-instruct | P2 | 235B | 37P+3F | 20P | 57/60 | step PFFF | — |
| devstral-small-2:24b | P0 | 24B | 36P+4F | 20P | 56/60 | v_int FFFF (calls getWorldState instead of placeBlock) | — |
| mistral-large-3:675b | P2 | 675B | 36P+4F | 20P | 56/60 | v_int FFFF (same boundary value confusion) | — |
| gpt-oss:120b | P1 | 120B | 32P+8F | 20P | 52/60 | parallel FFFF, step PFPP, v_enum FPFF (gold_block hallucination) | — |
| qwen3-vl:235b | P2 | 235B | 0P+40F | 20P | 20/60 | All native = F (server still returns ResponseError on rerun) | T→F: still blocked, reclassified as confirmed F. Migrated from Rerun. |
| gemma3:4b | P0 | 4B | 0P+40F | 20P | 20/60 | All native = F (Ollama doesn't wire tool calling) | — |
| gemma3:12b | P0 | 12B | 0P+40F | 20P | 20/60 | Same | — |
| gemma3:27b | P0 | 27B | 0P+40F | 20P | 20/60 | Same | — |

---

## Group D: Remaining — both layers have failures — 6 models

Neither native nor text is fully P. Confirmed F on both layers.

| Model | Sweep | Size | Native (40) | Text (20) | Total | Pattern | Rerun |
|-------|-------|------|-------------|-----------|-------|---------|-------|
| qwen3-next:80b | P1 | 80B | 35P+1T+4F | 19P+1F | 54/60 (1T) | scale FFFF, step PTPP, vt_zero PPPF | — (1T won't change group) |
| rnj-1:8b | P0 | 8B | 36P+4F | 16P+4F | 52/60 | v_zero FFFF, vt_int FFFF | T→F: v_zero confirmed model failure on rerun. Stays D. |
| qwen3.5:397b | P2 | 397B | 39P+1F | 17P+3F | 55/60 | scale PPFP, vt_sel/zero S1T1=F (worse on rerun than original) | T→F: rerun revealed more sub-check failures on S1T1. Stays D. |
| gpt-oss:20b | P0 | 20B | 29P+3T+8F | 15P+5F | 44/60 (3T) | parallel FFFF, v_enum FFFT, vt_zero FFFF + scattered | — (3T won't change group) |
| deepseek-v3.1:671b | P2 | 671B | 25P+15F | 19P+1F | 44/60 | think=true breaks native (PFPF pattern across tests) | — |
| deepseek-v3.2 | P2 | 671B | 0P+40F | 5P+15F | 5/60 | Both layers broken | — |

---

## Rerun Results Summary

7 models rerun to resolve T (transient) markers. 2 migrated up, 5 confirmed as F.

| Model | Original | Rerun target | Result | Migration |
|-------|----------|--------------|--------|-----------|
| minimax-m2 | 59/60 (1T) | v_zero S0T1 | **T→P** | **B → A** (now 60/60) |
| kimi-k2:1t | 59/60 (1T) | vt_sel S0T0 | **T→P** | **B → A** (now 60/60) |
| qwen3.5:397b | 58/60 (1T) | vt_enum S1T1 | **T→F** (plus vt_sel, vt_zero also failed) | stays D (worse: 55/60) |
| rnj-1:8b | 52/60 (4T) | v_zero ×4 | **T→F** (all 4 flags) | stays D (now 52/60 with 0T) |
| qwen3-coder-next | 40/60 (20T) | all vt_* ×4 | **T→F** (all 20 sub-checks) | Rerun → B (now 40/60 with 0T) |
| qwen3-coder:480b | 40/60 (20T) | all vt_* ×4 | **T→F** (all 20 sub-checks) | Rerun → B (now 40/60 with 0T) |
| qwen3-vl:235b | 20/60 (40T) | all native ×24 | **T→F** (still ResponseError) | Rerun → C (now 20/60 with 0T) |

Rerun output files: `observations/summaries/rerun_*.md`

---

## Summary

| Group | Count | Score range | Defining rule |
|-------|-------|-------------|---------------|
| A: All P | 10 | 60/60 | Native 40/40 P AND text 20/20 P |
| B: All native P | 8 | 40–57/60 | Native 40/40 P, text has confirmed F |
| C: All text P | 8 | 20–57/60 | Text 20/20 P, native has confirmed F |
| D: Remaining | 6 | 5–55/60 | Both layers have confirmed F |
| **Total** | **32** | | |

---

## Cross-cutting patterns

**Ministral family** (3b, 8b, 14b): All three Group A perfect 60/60. Smallest perfect models in the suite.

**Kimi family** (k2:1t, k2.5, k2-thinking): All Group A after rerun. k2:1t's single T was transient, confirmed P on rerun.

**Minimax family** (m2, m2.1, m2.5): m2 migrated to Group A on rerun. m2.1 and m2.5 stay Group B with vt_zero failures (PFFF and FFPF respectively).

**GLM family** (4.6, 4.7, 5): All Group B — native perfect 40/40, text fallback broken. glm-4.6 best (9/20 text), glm-4.7 worst (2/20 text). Text sub-checks vt_sel and vt_enum fail across the family.

**Qwen coder family** (qwen3-coder-next 80B, qwen3-coder:480b): Both Group B — native perfect 40/40. Rerun resolved T→F: server now responds but model fails all text sub-checks (0/20). Not a server issue — genuine text fallback failure.

**Gemma3 family** (4b, 12b, 27b): All Group C — identical behavior regardless of size. Zero native (Ollama doesn't wire tool calling), perfect text 20/20.

**GPT-OSS family** (20b, 120b): Both fail parallel_calls FFFF (return 1 tool not 2+) and hallucinate `gold_block` instead of `gold` for enum values. 120b is Group C (text perfect 20/20), 20b is Group D (text also has failures).

**Mistral v_int pair** (devstral-small-2:24b, mistral-large-3:675b): Both Group C with identical failure — v_int FFFF (calls getWorldState instead of placeBlock at integer boundary values). Text perfect 20/20.

**Deepseek family** (v3.1, v3.2): Both Group D. v3.1 has a clear think=true interference pattern (PFPF). v3.2 is broken on both layers (5/60).

**Size vs quality**: No correlation. ministral-3:3b (3B) scores 60/60, deepseek-v3.2 (671B) scores 5/60.
