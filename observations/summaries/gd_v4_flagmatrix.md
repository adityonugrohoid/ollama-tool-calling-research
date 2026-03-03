# Test Results — 20260303T160439

**Models:** qwen3-next:80b, rnj-1:8b, qwen3.5:397b, gpt-oss:20b, deepseek-v3.1:671b, deepseek-v3.2
**Tests:** single_tool, multi_tool, parallel_calls, multi_step, tool_count_scaling, voxel_tools, voxel_tools_text
**Flag combos:** S0T0, S0T1, S1T0, S1T1

## S0T0 (stream=False, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | PASS (native) | FAIL (mixed) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| deepseek-v3.1:671b | FAIL (none) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |

## S0T1 (stream=False, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | FAIL (mixed) | FAIL (mixed) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| deepseek-v3.1:671b | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (native) | FAIL (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (text) |

## S1T0 (stream=True, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | PASS (text) | FAIL (mixed) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| deepseek-v3.1:671b | FAIL (none) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (text) |

## S1T1 (stream=True, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | PASS (native) | FAIL (mixed) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| qwen3.5:397b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| deepseek-v3.1:671b | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | FAIL (native) | PASS (text) |
| deepseek-v3.2 | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | FAIL (text) |

## Flag Comparison

Positions: 0=S0T0 1=S0T1 2=S1T0 3=S1T1 | P=pass F=fail S=skip

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| qwen3-next:80b | PPPP | PPPP | PPPP | PFPP | FFFF | PPPP | PPPP |
| rnj-1:8b | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF |
| qwen3.5:397b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPFF |
| gpt-oss:20b | PPPP | PPPP | FFFF | PPPP | PPPP | FFFF | FFFF |
| deepseek-v3.1:671b | FPFP | PPPP | FPPP | PFPF | PFPP | FFFF | FPPP |
| deepseek-v3.2 | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PFFF |

## Detailed Results

### qwen3-next:80b / single_tool [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'text', 'schema_valid': True, 'schema_issues': [], 'classification': 'text'}

### qwen3-next:80b / single_tool [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'text', 'schema_valid': True, 'schema_issues': [], 'classification': 'text'}

### qwen3-next:80b / single_tool [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'text', 'schema_valid': True, 'schema_issues': [], 'classification': 'text'}

### qwen3-next:80b / single_tool [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'text', 'schema_valid': True, 'schema_issues': [], 'classification': 'text'}

### qwen3-next:80b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-next:80b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-next:80b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-next:80b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-next:80b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-next:80b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-next:80b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### qwen3-next:80b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-next:80b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}]}

### qwen3-next:80b / multi_step [S0T1] — FAIL
- Classification: mixed
- Parse success: True
- Stream: False, Think: True
- Notes: FORMAT SWITCH DETECTED: ['native', 'native', 'native', 'native', 'text']; Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'text']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'text'], 'format_switched': True, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 5, 'city': 'Sydney', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Sydney"}}\n</tools>'}]}

### qwen3-next:80b / multi_step [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['text', 'text', 'text', 'text', 'text']
- Details: {'turn_formats': ['text', 'text', 'text', 'text', 'text'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Tokyo"}}\n</tools>'}, {'turn': 2, 'city': 'Paris', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Paris"}}\n</tools>'}, {'turn': 3, 'city': 'New York', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "New York"}}\n</tools>'}, {'turn': 4, 'city': 'London', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "London"}}\n</tools>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Sydney"}}\n</tools>'}]}

### qwen3-next:80b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n'}]}

### qwen3-next:80b / tool_count_scaling [S0T0] — FAIL
- Classification: mixed
- Parse success: True
- Stream: False, Think: False
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:text | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'text', 'native']}

### qwen3-next:80b / tool_count_scaling [S0T1] — FAIL
- Classification: mixed
- Parse success: True
- Stream: False, Think: True
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:native | 15:text]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'native', 'text']}

### qwen3-next:80b / tool_count_scaling [S1T0] — FAIL
- Classification: mixed
- Parse success: True
- Stream: True, Think: False
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'native', 'native']}

### qwen3-next:80b / tool_count_scaling [S1T1] — FAIL
- Classification: mixed
- Parse success: True
- Stream: True, Think: True
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'native', 'native']}

### qwen3-next:80b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-next:80b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-next:80b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-next:80b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### rnj-1:8b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### rnj-1:8b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### rnj-1:8b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### rnj-1:8b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### rnj-1:8b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### rnj-1:8b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### rnj-1:8b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### rnj-1:8b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### rnj-1:8b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### rnj-1:8b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### rnj-1:8b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### rnj-1:8b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather function is the right tool for this task and confirmed that it requires only the city name as input. Since you provide'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you specif'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you spe'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Sydney, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}]}

### rnj-1:8b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather tool is the right way to retrieve this information. Since the tool requires a city parameter and you specified Tokyo, '}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified '}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specifi'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "THOUGHT: You've asked for the weather in several cities—Tokyo, Paris, New York, and London—and now you're asking about Sydney. I recognize this as a continuation of the same request pattern, so I use "}]}

### rnj-1:8b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather tool is the right way to retrieve this information. Since the tool requires a city parameter and you specified Tokyo, '}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified '}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specifi'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "THOUGHT: You've asked for the weather in several cities—Tokyo, Paris, New York, and London—and now you're asking about Sydney. I recognize this as a continuation of the same request pattern, so I use "}]}

### rnj-1:8b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather tool is the right way to retrieve this information. Since the tool requires a city parameter and you specified Tokyo, '}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified '}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specifi'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Sydney, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city parameter, and since you specified'}]}

### rnj-1:8b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### rnj-1:8b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### rnj-1:8b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### rnj-1:8b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### rnj-1:8b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### rnj-1:8b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### rnj-1:8b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### rnj-1:8b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### rnj-1:8b / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

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
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

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

### qwen3.5:397b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

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

### qwen3.5:397b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3.5:397b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gpt-oss:20b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:20b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:20b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:20b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:20b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:20b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:20b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:20b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:20b / parallel_calls [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:20b / parallel_calls [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:20b / parallel_calls [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:20b / parallel_calls [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:20b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:20b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:20b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:20b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:20b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:20b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:20b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:20b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:20b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: TOOL_NAME (expected placeBlock)'}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: tool_call (expected getWorldState)'}, 'tool_discrimination': {'passed': False, 'notes': 'wrong tool: tool_call (expected removeBlock)'}}

### gpt-oss:20b / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: tool.getWorldState (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: TOOL_CALL (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: tool_call (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / single_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### deepseek-v3.1:671b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### deepseek-v3.1:671b / single_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### deepseek-v3.1:671b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

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

### deepseek-v3.1:671b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### deepseek-v3.1:671b / parallel_calls [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### deepseek-v3.1:671b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### deepseek-v3.1:671b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### deepseek-v3.1:671b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### deepseek-v3.1:671b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Paris for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in New York for you."}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in London for you."}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Sydney for you."}]}

### deepseek-v3.1:671b / multi_step [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 3/5; Turn formats: ['none', 'native', 'native', 'native', 'none']
- Details: {'turn_formats': ['none', 'native', 'native', 'native', 'none'], 'format_switched': False, 'successful_turns': 3, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The current weather in Sydney is **Sunny and 22°C**.'}]}

### deepseek-v3.1:671b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Tokyo for you."}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Paris for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in New York for you."}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in London for you."}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'll check the current weather in Sydney for you."}]}

### deepseek-v3.1:671b / multi_step [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 3/5; Turn formats: ['none', 'native', 'native', 'native', 'none']
- Details: {'turn_formats': ['none', 'native', 'native', 'native', 'none'], 'format_switched': False, 'successful_turns': 3, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '{{#tool_call}}get_weather{"city":"Sydney"}{{/tool_call}}Sunny, 25°C'}]}

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
- Notes: Scale: [1:native | 3:none | 5:none | 8:native | 10:none | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'none', 'none', 'native', 'none', 'native']}

### deepseek-v3.1:671b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### deepseek-v3.1:671b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### deepseek-v3.1:671b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### deepseek-v3.1:671b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, zero_param_tool
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### deepseek-v3.1:671b / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.1:671b / voxel_tools_text [S1T1] — PASS
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
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Tokyo</parameter>\n</invoke>\n</function_calls>'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Paris</parameter>\n</invoke>\n</function_calls>'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">New York</parameter>\n</invoke>\n</function_calls>'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">London</parameter>\n</invoke>\n</function_calls>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Sydney</parameter>\n</invoke>\n</function_calls>'}]}

### deepseek-v3.2 / multi_step [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Tokyo</parameter>\n</invoke>\n</function_calls>'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Paris</parameter>\n</invoke>\n</function_calls>'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">New York</parameter>\n</invoke>\n</function_calls>'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">London</parameter>\n</invoke>\n</function_calls>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Sydney</parameter>\n</invoke>\n</function_calls>'}]}

### deepseek-v3.2 / multi_step [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Tokyo</parameter>\n</invoke>\n</function_calls>'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Paris</parameter>\n</invoke>\n</function_calls>'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<｜DSML｜parameter name="city" string="true">New York</｜DSML｜parameter>\n</｜DSML｜invoke>\n</｜DSML｜function_calls>'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">London</parameter>\n</invoke>\n</function_calls>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Sydney</parameter>\n</invoke>\n</function_calls>'}]}

### deepseek-v3.2 / multi_step [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Tokyo</parameter>\n</invoke>\n</function_calls>'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Paris</parameter>\n</invoke>\n</function_calls>'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">New York</parameter>\n</invoke>\n</function_calls>'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">London</parameter>\n</invoke>\n</function_calls>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': '\n\n<function_calls>\n<invoke name="get_weather">\n<parameter name="city" string="true">Sydney</parameter>\n</invoke>\n</function_calls>'}]}

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

### deepseek-v3.2 / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.2 / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via misrouted'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.2 / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### deepseek-v3.2 / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, zero_param_tool
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}
