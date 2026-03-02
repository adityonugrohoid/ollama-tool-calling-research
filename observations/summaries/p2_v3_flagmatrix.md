# Test Results — 20260302T234633

**Models:** minimax-m2, minimax-m2.1, minimax-m2.5, qwen3.5:397b, qwen3-vl:235b, qwen3-vl:235b-instruct, qwen3-coder:480b, mistral-large-3:675b, deepseek-v3.1:671b, cogito-2.1:671b, deepseek-v3.2, glm-4.6, glm-4.7, glm-5, kimi-k2:1t, kimi-k2.5, kimi-k2-thinking
**Tests:** single_tool, multi_tool, parallel_calls, multi_step, tool_count_scaling, voxel_tools, voxel_tools_text
**Flag combos:** S0T0, S0T1, S1T0, S1T1

## S0T0 (stream=False, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| minimax-m2 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| minimax-m2.1 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| minimax-m2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3-vl:235b | FAIL () | FAIL () | FAIL () | FAIL () | FAIL () | FAIL (native) | PASS (text) |
| qwen3-vl:235b-instruct | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3-coder:480b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| mistral-large-3:675b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| deepseek-v3.1:671b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| cogito-2.1:671b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (text) |
| glm-4.6 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-4.7 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| kimi-k2:1t | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| kimi-k2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2-thinking | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## S0T1 (stream=False, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| minimax-m2 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| minimax-m2.1 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| minimax-m2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3-vl:235b | FAIL () | FAIL () | FAIL () | FAIL () | FAIL () | FAIL (native) | PASS (text) |
| qwen3-vl:235b-instruct | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3-coder:480b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| mistral-large-3:675b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| deepseek-v3.1:671b | FAIL (none) | PASS (native) | FAIL (none) | FAIL (native) | FAIL (native) | FAIL (native) | PASS (text) |
| cogito-2.1:671b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (text) |
| glm-4.6 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-4.7 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| kimi-k2:1t | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2-thinking | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## S1T0 (stream=True, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| minimax-m2 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| minimax-m2.1 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| minimax-m2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (text) |
| qwen3-vl:235b | FAIL () | FAIL () | FAIL () | FAIL () | FAIL () | FAIL (native) | PASS (text) |
| qwen3-vl:235b-instruct | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3-coder:480b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| mistral-large-3:675b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| deepseek-v3.1:671b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (native) | FAIL (text) |
| cogito-2.1:671b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (none) | FAIL (native) | FAIL (text) |
| glm-4.6 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-4.7 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| kimi-k2:1t | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2-thinking | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## S1T1 (stream=True, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| minimax-m2 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| minimax-m2.1 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| minimax-m2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3-vl:235b | FAIL () | FAIL () | FAIL () | FAIL () | FAIL () | FAIL (native) | PASS (text) |
| qwen3-vl:235b-instruct | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | PASS (text) |
| qwen3-coder:480b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| mistral-large-3:675b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| deepseek-v3.1:671b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (native) | FAIL (native) | PASS (text) |
| cogito-2.1:671b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (text) |
| glm-4.6 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-4.7 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| glm-5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| kimi-k2:1t | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2.5 | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| kimi-k2-thinking | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## Flag Comparison

Positions: 0=S0T0 1=S0T1 2=S1T0 3=S1T1 | P=pass F=fail S=skip

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| minimax-m2 | PPPP | PPPP | PPPP | PPPP | PPPP | PFPP | PPPP |
| minimax-m2.1 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PFFF |
| minimax-m2.5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFPF |
| qwen3.5:397b | PPPP | PPPP | PPPP | PPPP | PPFP | PPPP | PPPF |
| qwen3-vl:235b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP |
| qwen3-vl:235b-instruct | PPPP | PPPP | PPPP | PFFF | PPPP | PPPP | PPPP |
| qwen3-coder:480b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF |
| mistral-large-3:675b | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | PPPP |
| deepseek-v3.1:671b | PFPF | PPPF | FFPF | PFPF | PFFF | PFFF | PPFP |
| cogito-2.1:671b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |
| deepseek-v3.2 | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF |
| glm-4.6 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF |
| glm-4.7 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF |
| glm-5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF |
| kimi-k2:1t | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FPPP |
| kimi-k2.5 | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |
| kimi-k2-thinking | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |

## Detailed Results

### minimax-m2 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2 / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Service Temporarily Unavailable (status code: 503)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2 / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2 / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2 / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2 / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.1 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.1 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.1 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.1 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.1 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.1 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.1 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.1 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.1 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_temperature', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_temperature', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.1 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.1 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.1 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.1 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.1 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.1 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.1 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.1 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.1 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.1 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.1 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.1 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.1 / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.1 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.1 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.1 / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.1 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.1 / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.1 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.5 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.5 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.5 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.5 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### minimax-m2.5 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.5 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.5 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.5 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### minimax-m2.5 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.5 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.5 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.5 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### minimax-m2.5 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.5 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.5 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.5 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### minimax-m2.5 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.5 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.5 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.5 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### minimax-m2.5 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.5 / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.5 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.5 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### minimax-m2.5 / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.5 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.5 / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### minimax-m2.5 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3.5:397b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3.5:397b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3.5:397b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3.5:397b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3.5:397b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3.5:397b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3.5:397b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3.5:397b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3.5:397b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3.5:397b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3.5:397b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### qwen3.5:397b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3.5:397b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3.5:397b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3.5:397b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3.5:397b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3.5:397b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3.5:397b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3.5:397b / tool_count_scaling [S1T0] — FAIL
- Classification: native
- Parse success: False
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:none | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'none', 'native', 'native']}

### qwen3.5:397b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3.5:397b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3.5:397b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3.5:397b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3.5:397b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3.5:397b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3.5:397b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3.5:397b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3.5:397b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b / single_tool [S0T0] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / single_tool [S0T1] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / single_tool [S1T0] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / single_tool [S1T1] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_tool [S0T0] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_tool [S0T1] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_tool [S1T0] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_tool [S1T1] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / parallel_calls [S0T0] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / parallel_calls [S0T1] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / parallel_calls [S1T0] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / parallel_calls [S1T1] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_step [S0T0] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_step [S0T1] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_step [S1T0] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / multi_step [S1T1] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / tool_count_scaling [S0T0] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / tool_count_scaling [S0T1] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / tool_count_scaling [S1T0] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / tool_count_scaling [S1T1] — FAIL
- Classification: 
- Parse success: False
- Stream: True, Think: True
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### qwen3-vl:235b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-vl:235b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-vl:235b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-vl:235b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-vl:235b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b-instruct / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-vl:235b-instruct / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-vl:235b-instruct / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-vl:235b-instruct / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-vl:235b-instruct / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-vl:235b-instruct / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-vl:235b-instruct / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-vl:235b-instruct / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-vl:235b-instruct / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-vl:235b-instruct / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-vl:235b-instruct / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-vl:235b-instruct / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-vl:235b-instruct / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-vl:235b-instruct / multi_step [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 3/5; Turn formats: ['native', 'native', 'native', 'none', 'none']
- Details: {'turn_formats': ['native', 'native', 'native', 'none', 'none'], 'format_switched': False, 'successful_turns': 3, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in London is currently cloudy, with a temperature of 18°C.'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney is currently sunny, with a temperature of 22°C.'}]}

### qwen3-vl:235b-instruct / multi_step [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 3/5; Turn formats: ['native', 'native', 'native', 'none', 'none']
- Details: {'turn_formats': ['native', 'native', 'native', 'none', 'none'], 'format_switched': False, 'successful_turns': 3, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in London is currently cloudy, with a temperature of 18°C.'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney is currently sunny, with a temperature of 22°C.'}]}

### qwen3-vl:235b-instruct / multi_step [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 4/5; Turn formats: ['native', 'native', 'native', 'native', 'none']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'none'], 'format_switched': False, 'successful_turns': 4, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney is sunny, with a temperature of 24°C.'}]}

### qwen3-vl:235b-instruct / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-vl:235b-instruct / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-vl:235b-instruct / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-vl:235b-instruct / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-vl:235b-instruct / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-vl:235b-instruct / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-vl:235b-instruct / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-vl:235b-instruct / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-vl:235b-instruct / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b-instruct / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b-instruct / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-vl:235b-instruct / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-coder:480b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder:480b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder:480b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder:480b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder:480b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder:480b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder:480b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder:480b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder:480b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder:480b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder:480b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder:480b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder:480b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder:480b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder:480b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder:480b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder:480b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder:480b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder:480b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder:480b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder:480b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder:480b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder:480b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder:480b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder:480b / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: False
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-coder:480b / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: False
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-coder:480b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: False
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-coder:480b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: False
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### mistral-large-3:675b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### mistral-large-3:675b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### mistral-large-3:675b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### mistral-large-3:675b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### mistral-large-3:675b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### mistral-large-3:675b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### mistral-large-3:675b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### mistral-large-3:675b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### mistral-large-3:675b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### mistral-large-3:675b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### mistral-large-3:675b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### mistral-large-3:675b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### mistral-large-3:675b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### mistral-large-3:675b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### mistral-large-3:675b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### mistral-large-3:675b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### mistral-large-3:675b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### mistral-large-3:675b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### mistral-large-3:675b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### mistral-large-3:675b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### mistral-large-3:675b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### mistral-large-3:675b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### mistral-large-3:675b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### mistral-large-3:675b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### mistral-large-3:675b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### mistral-large-3:675b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### mistral-large-3:675b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### mistral-large-3:675b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### deepseek-v3.1:671b / single_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### deepseek-v3.1:671b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### deepseek-v3.1:671b / single_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### deepseek-v3.1:671b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### deepseek-v3.1:671b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### deepseek-v3.1:671b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### deepseek-v3.1:671b / multi_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### deepseek-v3.1:671b / parallel_calls [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### deepseek-v3.1:671b / parallel_calls [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### deepseek-v3.1:671b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### deepseek-v3.1:671b / parallel_calls [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### deepseek-v3.1:671b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Tokyo for you right now."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Paris for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in New York for you right away."}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in London for you."}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Sydney for you."}]}

### deepseek-v3.1:671b / multi_step [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 4/5; Turn formats: ['native', 'none', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'none', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 4, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in New York for you."}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in London for you."}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Sydney for you."}]}

### deepseek-v3.1:671b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Paris for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in New York for you."}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in London for you."}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Sydney for you."}]}

### deepseek-v3.1:671b / multi_step [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 2/5; Turn formats: ['native', 'native', 'none', 'none', 'none']
- Details: {'turn_formats': ['native', 'native', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 2, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '{{get_weather}}{{"city":"New York"}}'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '⇬get_weather⇬{"city":"London"}⇬'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '⇬get_weather⇬{"city":"Sydney"}⇬'}]}

### deepseek-v3.1:671b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### deepseek-v3.1:671b / tool_count_scaling [S0T1] — FAIL
- Classification: native
- Parse success: False
- Stream: False, Think: True
- Notes: Scale: [1:none | 3:none | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'native', 'native', 'native', 'native']}

### deepseek-v3.1:671b / tool_count_scaling [S1T0] — FAIL
- Classification: native
- Parse success: False
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:none | 8:none | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'none', 'none', 'native', 'native']}

### deepseek-v3.1:671b / tool_count_scaling [S1T1] — FAIL
- Classification: native
- Parse success: False
- Stream: True, Think: True
- Notes: Scale: [1:none | 3:none | 5:native | 8:native | 10:none | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'native', 'native', 'none', 'native']}

### deepseek-v3.1:671b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: enum_adherence, zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### cogito-2.1:671b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### cogito-2.1:671b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### cogito-2.1:671b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### cogito-2.1:671b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### cogito-2.1:671b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### cogito-2.1:671b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### cogito-2.1:671b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### cogito-2.1:671b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### cogito-2.1:671b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### cogito-2.1:671b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### cogito-2.1:671b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### cogito-2.1:671b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### cogito-2.1:671b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### cogito-2.1:671b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### cogito-2.1:671b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### cogito-2.1:671b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### cogito-2.1:671b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### cogito-2.1:671b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### cogito-2.1:671b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### cogito-2.1:671b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### cogito-2.1:671b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### cogito-2.1:671b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### cogito-2.1:671b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### cogito-2.1:671b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### cogito-2.1:671b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### cogito-2.1:671b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### cogito-2.1:671b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### cogito-2.1:671b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.2 / single_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### deepseek-v3.2 / single_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### deepseek-v3.2 / single_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### deepseek-v3.2 / single_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### deepseek-v3.2 / multi_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### deepseek-v3.2 / multi_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### deepseek-v3.2 / multi_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### deepseek-v3.2 / multi_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### deepseek-v3.2 / parallel_calls [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### deepseek-v3.2 / parallel_calls [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### deepseek-v3.2 / parallel_calls [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### deepseek-v3.2 / parallel_calls [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### deepseek-v3.2 / multi_step [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}]}

### deepseek-v3.2 / multi_step [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}]}

### deepseek-v3.2 / multi_step [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 1/5; Turn formats: ['none', 'native', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'native', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 1, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}]}

### deepseek-v3.2 / multi_step [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}]}

### deepseek-v3.2 / tool_count_scaling [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### deepseek-v3.2 / tool_count_scaling [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### deepseek-v3.2 / tool_count_scaling [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### deepseek-v3.2 / tool_count_scaling [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### deepseek-v3.2 / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.2 / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.2 / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.2 / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.2 / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: enum_adherence, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via misrouted"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.2 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: False
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.2 / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via misrouted'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.2 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via misrouted"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### glm-4.6 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.6 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.6 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.6 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.6 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.6 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.6 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.6 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.6 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.6 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.6 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.6 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.6 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.6 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.6 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.6 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.6 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.6 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.6 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.6 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.6 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.6 / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.6 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.6 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.6 / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### glm-4.6 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### glm-4.6 / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### glm-4.6 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### glm-4.7 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.7 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.7 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.7 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-4.7 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.7 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.7 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.7 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-4.7 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.7 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.7 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.7 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-4.7 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.7 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.7 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.7 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-4.7 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.7 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.7 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.7 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-4.7 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.7 / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.7 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.7 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-4.7 / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### glm-4.7 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### glm-4.7 / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: False
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### glm-4.7 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: False
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### glm-5 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-5 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-5 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-5 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### glm-5 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-5 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-5 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-5 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### glm-5 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-5 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-5 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-5 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### glm-5 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-5 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-5 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-5 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### glm-5 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-5 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-5 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-5 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### glm-5 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-5 / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-5 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-5 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### glm-5 / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 3, "y": 0, "z": 5, "type": "stone"}} (expected placeBlock)'}, 'enum_adherence': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 7, "y": 1, "z": 7, "type": "gold"}} (expected placeBlock)'}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 15, "y": 15, "z": 15, "type": "stone"}} (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': 'wrong tool: {"name": "removeBlock", "arguments": {"x": 3, "y": 0, "z": 5}} (expected removeBlock)'}}

### glm-5 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: False
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 3, "y": 0, "z": 5, "type": "stone"}} (expected placeBlock)'}, 'enum_adherence': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 7, "y": 1, "z": 7, "type": "gold"}} (expected placeBlock)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'wrong tool: {"name": "removeBlock", "arguments": {"x": 3, "y": 0, "z": 5}} (expected removeBlock)'}}

### glm-5 / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 3, "y": 0, "z": 5, "type": "stone"}} (expected placeBlock)'}, 'enum_adherence': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 7, "y": 1, "z": 7, "type": "gold"}} (expected placeBlock)'}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: placeBlock({"x": 15, "y": 15, "z": 15, "type": "stone"}) (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': 'wrong tool: {"name": "removeBlock", "arguments": {"x": 3, "y": 0, "z": 5}} (expected removeBlock)'}}

### glm-5 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 3, "y": 0, "z": 5, "type": "stone"}} (expected placeBlock)'}, 'enum_adherence': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 7, "y": 1, "z": 7, "type": "gold"}} (expected placeBlock)'}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: {"name": "placeBlock", "arguments": {"x": 15, "y": 15, "z": 15, "type": "stone"}} (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': 'wrong tool: {"name": "removeBlock", "arguments": {"x": 3, "y": 0, "z": 5}} (expected removeBlock)'}}

### kimi-k2:1t / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2:1t / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2:1t / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2:1t / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2:1t / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2:1t / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2:1t / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2:1t / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2:1t / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2:1t / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2:1t / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2:1t / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2:1t / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll get the current weather for Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2:1t / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2:1t / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2:1t / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2:1t / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2:1t / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2:1t / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2:1t / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2:1t / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2:1t / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2:1t / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2:1t / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2:1t / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Service Temporarily Unavailable (status code: 503)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2:1t / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2:1t / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2:1t / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2.5 / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2.5 / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2.5 / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2.5 / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2.5 / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2.5 / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2.5 / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2.5 / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2.5 / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2.5 / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2.5 / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2.5 / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2.5 / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you. "}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2.5 / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Tokyo for you. "}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2.5 / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Tokyo for you. "}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2.5 / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the weather in Tokyo for you. "}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2.5 / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2.5 / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2.5 / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2.5 / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2.5 / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'y': 0, 'z': 5, 'x': 3}) via native"}}

### kimi-k2.5 / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'z': 5, 'type': 'stone', 'x': 3, 'y': 0}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'y': 0, 'z': 5, 'x': 3}) via native"}}

### kimi-k2.5 / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'z': 5, 'type': 'stone', 'x': 3, 'y': 0}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'z': 5, 'x': 3, 'y': 0}) via native"}}

### kimi-k2.5 / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2.5 / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2.5 / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2.5 / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2.5 / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2-thinking / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2-thinking / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2-thinking / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2-thinking / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### kimi-k2-thinking / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2-thinking / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2-thinking / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2-thinking / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### kimi-k2-thinking / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### kimi-k2-thinking / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### kimi-k2-thinking / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2-thinking / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### kimi-k2-thinking / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2-thinking / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2-thinking / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2-thinking / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### kimi-k2-thinking / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2-thinking / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2-thinking / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2-thinking / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### kimi-k2-thinking / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2-thinking / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2-thinking / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2-thinking / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### kimi-k2-thinking / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via misrouted'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2-thinking / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2-thinking / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### kimi-k2-thinking / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}
