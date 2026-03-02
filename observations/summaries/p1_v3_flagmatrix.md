# Test Results — 20260302T213301

**Models:** nemotron-3-nano:30b, qwen3-next:80b, qwen3-coder-next, gpt-oss:120b, devstral-2:123b, gemini-3-flash-preview
**Tests:** single_tool, multi_tool, parallel_calls, multi_step, tool_count_scaling, voxel_tools, voxel_tools_text
**Flag combos:** S0T0, S0T1, S1T0, S1T1

## S0T0 (stream=False, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| nemotron-3-nano:30b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | PASS (text) | FAIL (mixed) | PASS (native) | PASS (text) |
| qwen3-coder-next | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| gpt-oss:120b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| devstral-2:123b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemini-3-flash-preview | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## S0T1 (stream=False, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| nemotron-3-nano:30b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | FAIL () | FAIL (mixed) | PASS (native) | PASS (text) |
| qwen3-coder-next | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| gpt-oss:120b | PASS (native) | PASS (native) | FAIL (native) | FAIL (native) | PASS (native) | PASS (native) | PASS (text) |
| devstral-2:123b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemini-3-flash-preview | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## S1T0 (stream=True, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| nemotron-3-nano:30b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | PASS (text) | FAIL (mixed) | PASS (native) | PASS (text) |
| qwen3-coder-next | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| gpt-oss:120b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| devstral-2:123b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemini-3-flash-preview | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## S1T1 (stream=True, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| nemotron-3-nano:30b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| qwen3-next:80b | PASS (text) | PASS (native) | PASS (native) | PASS (text) | FAIL (mixed) | PASS (native) | FAIL (text) |
| qwen3-coder-next | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) |
| gpt-oss:120b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| devstral-2:123b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemini-3-flash-preview | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |

## Flag Comparison

Positions: 0=S0T0 1=S0T1 2=S1T0 3=S1T1 | P=pass F=fail S=skip

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| nemotron-3-nano:30b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF |
| qwen3-next:80b | PPPP | PPPP | PPPP | PFPP | FFFF | PPPP | PPPF |
| qwen3-coder-next | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF |
| gpt-oss:120b | PPPP | PPPP | FFFF | PFPP | PPPP | FPFF | PPPP |
| devstral-2:123b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |
| gemini-3-flash-preview | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |

## Detailed Results

### nemotron-3-nano:30b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### nemotron-3-nano:30b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### nemotron-3-nano:30b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### nemotron-3-nano:30b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### nemotron-3-nano:30b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### nemotron-3-nano:30b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### nemotron-3-nano:30b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### nemotron-3-nano:30b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### nemotron-3-nano:30b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### nemotron-3-nano:30b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### nemotron-3-nano:30b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### nemotron-3-nano:30b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### nemotron-3-nano:30b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### nemotron-3-nano:30b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### nemotron-3-nano:30b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### nemotron-3-nano:30b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### nemotron-3-nano:30b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### nemotron-3-nano:30b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### nemotron-3-nano:30b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### nemotron-3-nano:30b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### nemotron-3-nano:30b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'y': 1, 'x': 7, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### nemotron-3-nano:30b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'type': 'stone', 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### nemotron-3-nano:30b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### nemotron-3-nano:30b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'y': 0, 'z': 5, 'type': 'stone', 'x': 3}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'y': 1, 'x': 7, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'y': 15, 'z': 15, 'x': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### nemotron-3-nano:30b / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### nemotron-3-nano:30b / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': "schema issues: ['Wrong type for x: expected integer, got str', 'Wrong type for y: expected integer, got str', 'Wrong type for z: expected integer, got str']"}, 'enum_adherence': {'passed': False, 'notes': "schema issues: ['Wrong type for x: expected integer, got str', 'Wrong type for y: expected integer, got str', 'Wrong type for z: expected integer, got str']"}, 'integer_constraints': {'passed': False, 'notes': "schema issues: ['Wrong type for y: expected integer, got str', 'Wrong type for x: expected integer, got str', 'Wrong type for z: expected integer, got str']"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': "schema issues: ['Wrong type for x: expected integer, got str', 'Wrong type for y: expected integer, got str', 'Wrong type for z: expected integer, got str']"}}

### nemotron-3-nano:30b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, integer_constraints
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### nemotron-3-nano:30b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': "schema issues: ['Wrong type for y: expected integer, got str', 'Wrong type for x: expected integer, got str', 'Wrong type for z: expected integer, got str']"}, 'enum_adherence': {'passed': False, 'notes': "schema issues: ['Wrong type for x: expected integer, got str', 'Wrong type for y: expected integer, got str', 'Wrong type for z: expected integer, got str']"}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: -1)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': False, 'notes': "schema issues: ['Wrong type for y: expected integer, got str', 'Wrong type for x: expected integer, got str', 'Wrong type for z: expected integer, got str']"}}

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
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-next:80b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-next:80b / multi_step [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['text', 'text', 'text', 'text', 'text']
- Details: {'turn_formats': ['text', 'text', 'text', 'text', 'text'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Tokyo"}}\n</tools>'}, {'turn': 2, 'city': 'Paris', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Paris"}}\n</tools>'}, {'turn': 3, 'city': 'New York', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "New York"}}\n</tools>'}, {'turn': 4, 'city': 'London', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "London"}}\n</tools>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Sydney"}}\n</tools>'}]}

### qwen3-next:80b / multi_step [S0T1] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: True
- Notes: Exception: ResponseError
- Error: Service Temporarily Unavailable (status code: 503)

### qwen3-next:80b / multi_step [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['text', 'text', 'text', 'text', 'text']
- Details: {'turn_formats': ['text', 'text', 'text', 'text', 'text'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Tokyo"}}\n</tools>'}, {'turn': 2, 'city': 'Paris', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Paris"}}\n</tools>'}, {'turn': 3, 'city': 'New York', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "New York"}}\n</tools>'}, {'turn': 4, 'city': 'London', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "London"}}\n</tools>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Sydney"}}\n</tools>'}]}

### qwen3-next:80b / multi_step [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['text', 'text', 'text', 'text', 'text']
- Details: {'turn_formats': ['text', 'text', 'text', 'text', 'text'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Tokyo"}}\n</tools>'}, {'turn': 2, 'city': 'Paris', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Paris"}}\n</tools>'}, {'turn': 3, 'city': 'New York', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "New York"}}\n</tools>'}, {'turn': 4, 'city': 'London', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "London"}}\n</tools>'}, {'turn': 5, 'city': 'Sydney', 'classification': 'text', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': '\n\n<tools>\n{"name": "get_weather", "arguments": {"city": "Sydney"}}\n</tools>'}]}

### qwen3-next:80b / tool_count_scaling [S0T0] — FAIL
- Classification: mixed
- Parse success: True
- Stream: False, Think: False
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:native | 15:text]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'native', 'text']}

### qwen3-next:80b / tool_count_scaling [S0T1] — FAIL
- Classification: mixed
- Parse success: True
- Stream: False, Think: True
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'native', 'native']}

### qwen3-next:80b / tool_count_scaling [S1T0] — FAIL
- Classification: mixed
- Parse success: True
- Stream: True, Think: False
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:native | 10:text | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'native', 'text', 'native']}

### qwen3-next:80b / tool_count_scaling [S1T1] — FAIL
- Classification: mixed
- Parse success: True
- Stream: True, Think: True
- Notes: FORMAT SWITCH at 3 tools: text -> native; Scale: [1:text | 3:native | 5:native | 8:text | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'text', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': True, 'classifications_seen': ['text', 'native', 'native', 'text', 'native', 'native']}

### qwen3-next:80b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-next:80b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

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

### qwen3-next:80b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: TOOL_NAME (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### qwen3-coder-next / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder-next / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder-next / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder-next / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### qwen3-coder-next / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder-next / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder-next / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder-next / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### qwen3-coder-next / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder-next / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder-next / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder-next / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### qwen3-coder-next / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder-next / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder-next / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder-next / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### qwen3-coder-next / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder-next / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder-next / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder-next / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### qwen3-coder-next / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder-next / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder-next / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder-next / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### qwen3-coder-next / voxel_tools_text [S0T0] — FAIL
- Classification: text
- Parse success: False
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-coder-next / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: False
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-coder-next / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: False
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### qwen3-coder-next / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: False
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'enum_adherence': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'integer_constraints': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'zero_param_tool': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}, 'tool_discrimination': {'passed': False, 'notes': 'error: ResponseError: Internal Server Error (status code: 500)'}}

### gpt-oss:120b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:120b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:120b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:120b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gpt-oss:120b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:120b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:120b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:120b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gpt-oss:120b / parallel_calls [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:120b / parallel_calls [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:120b / parallel_calls [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:120b / parallel_calls [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native', 'classification': 'native'}

### gpt-oss:120b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['function'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:120b / multi_step [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 4/5; Turn formats: ['native', 'native', 'none', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'none', 'native', 'native'], 'format_switched': False, 'successful_turns': 4, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:120b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:120b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['function'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gpt-oss:120b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:120b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:120b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:120b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:120b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:120b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:120b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:120b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:120b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gpt-oss:120b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gpt-oss:120b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gpt-oss:120b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-2:123b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-2:123b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-2:123b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-2:123b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-2:123b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-2:123b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-2:123b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-2:123b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-2:123b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-2:123b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-2:123b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-2:123b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-2:123b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-2:123b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-2:123b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-2:123b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-2:123b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-2:123b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-2:123b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-2:123b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-2:123b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-2:123b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-2:123b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-2:123b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-2:123b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-2:123b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-2:123b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-2:123b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemini-3-flash-preview / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gemini-3-flash-preview / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gemini-3-flash-preview / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gemini-3-flash-preview / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### gemini-3-flash-preview / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gemini-3-flash-preview / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gemini-3-flash-preview / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gemini-3-flash-preview / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### gemini-3-flash-preview / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### gemini-3-flash-preview / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### gemini-3-flash-preview / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### gemini-3-flash-preview / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### gemini-3-flash-preview / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gemini-3-flash-preview / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gemini-3-flash-preview / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gemini-3-flash-preview / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### gemini-3-flash-preview / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gemini-3-flash-preview / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gemini-3-flash-preview / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gemini-3-flash-preview / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gemini-3-flash-preview / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'z': 7, 'type': 'gold', 'x': 7, 'y': 1}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'z': 15, 'y': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'z': 5, 'y': 0, 'x': 3}) via native"}}

### gemini-3-flash-preview / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'y': 0, 'x': 3, 'z': 5}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'y': 1, 'type': 'gold', 'x': 7, 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'z': 15, 'y': 15, 'x': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'z': 5, 'y': 0, 'x': 3}) via native"}}

### gemini-3-flash-preview / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'z': 5, 'type': 'stone', 'y': 0}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'z': 7, 'type': 'gold', 'x': 7, 'y': 1}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'type': 'stone', 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gemini-3-flash-preview / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'z': 5, 'x': 3, 'type': 'stone', 'y': 0}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'y': 1, 'x': 7, 'type': 'gold', 'z': 7}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'y': 0, 'x': 3, 'z': 5}) via native"}}

### gemini-3-flash-preview / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemini-3-flash-preview / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemini-3-flash-preview / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemini-3-flash-preview / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}
