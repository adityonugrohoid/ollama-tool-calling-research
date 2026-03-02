# Test Results — 20260302T202447

**Models:** ministral-3:3b, gemma3:4b, ministral-3:8b, rnj-1:8b, gemma3:12b, gpt-oss:20b, ministral-3:14b, devstral-small-2:24b, gemma3:27b
**Tests:** single_tool, multi_tool, parallel_calls, multi_step, tool_count_scaling, voxel_tools, voxel_tools_text
**Flag combos:** S0T0, S0T1, S1T0, S1T1

## S0T0 (stream=False, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| ministral-3:3b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemma3:4b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| ministral-3:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| gemma3:12b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | FAIL () | PASS (native) | FAIL (native) | FAIL (text) |
| ministral-3:14b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| devstral-small-2:24b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| gemma3:27b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |

## S0T1 (stream=False, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| ministral-3:3b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemma3:4b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| ministral-3:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| gemma3:12b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| ministral-3:14b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| devstral-small-2:24b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| gemma3:27b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |

## S1T0 (stream=True, think=False)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| ministral-3:3b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemma3:4b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| ministral-3:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| gemma3:12b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| ministral-3:14b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| devstral-small-2:24b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| gemma3:27b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |

## S1T1 (stream=True, think=True)

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| ministral-3:3b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| gemma3:4b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| ministral-3:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| gemma3:12b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | PASS (native) | PASS (native) | FAIL (native) | FAIL (text) |
| ministral-3:14b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) |
| devstral-small-2:24b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | FAIL (native) | PASS (text) |
| gemma3:27b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (native) | PASS (text) |

## Flag Comparison

Positions: 0=S0T0 1=S0T1 2=S1T0 3=S1T1 | P=pass F=fail S=skip

| Model | single_tool | multi_tool | parallel_calls | multi_step | tool_count_scaling | voxel_tools | voxel_tools_text |
|-------|------|------|------|------|------|------|------|
| ministral-3:3b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |
| gemma3:4b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP |
| ministral-3:8b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |
| rnj-1:8b | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | FFFF |
| gemma3:12b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP |
| gpt-oss:20b | PPPP | PPPP | FFFF | FPPP | PPPP | FFFF | FFFF |
| ministral-3:14b | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP | PPPP |
| devstral-small-2:24b | PPPP | PPPP | PPPP | PPPP | PPPP | FFFF | PPPP |
| gemma3:27b | FFFF | FFFF | FFFF | FFFF | FFFF | FFFF | PPPP |

## Detailed Results

### ministral-3:3b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:3b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:3b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:3b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:3b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:3b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:3b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:3b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:3b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:3b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:3b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### ministral-3:3b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:3b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I currently don't have real-time weather data for Paris, but I can help you check it! Let me fetch the weather for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I'm checking the weather for you now!"}]}

### ministral-3:3b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I currently don't have real-time weather data for Paris, but I can help you check it! Let me fetch the weather for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:3b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I currently don't have real-time weather data for Paris, but I can check it for you! Let me fetch the weather information."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:3b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': "I currently don't have real-time weather data for Paris, but I can help you check it! Let me fetch the weather for you."}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:3b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:3b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:3b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:3b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:3b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:3b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:3b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:3b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:3b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:3b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:3b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:3b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:4b / single_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:4b / single_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:4b / single_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:4b / single_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:4b / multi_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:4b / multi_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:4b / multi_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:4b / multi_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:4b / parallel_calls [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:4b / parallel_calls [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:4b / parallel_calls [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:4b / parallel_calls [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:4b / multi_step [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, here's the current weather in Tokyo:\n\n**As of November 3, 2023, at 11:30 AM JST (Japan Standard Time):**\n\n*   **Temperature:** 16°C (61°F)\n*   **Feels Like:** 16°C (61°F)\n*   **Condition:** Part"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Paris as of November 3, 2023, at 11:30 AM CET (Central European Time):\n\n*   **Temperature:** 12°C (54°F)\n*   **Feels Like:** 10°C (50°F)\n*   **Condition:** Overcast\n*   **H'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in New York City as of November 3, 2023, at 11:30 AM EST (Eastern Standard Time):\n\n*   **Temperature:** 11°C (52°F)\n*   **Feels Like:** 9°C (48°F)\n*   **Condition:** Partly Cl'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in London as of November 3, 2023, at 11:30 AM GMT (Greenwich Mean Time):\n\n*   **Temperature:** 10°C (50°F)\n*   **Feels Like:** 8°C (46°F)\n*   **Condition:** Cloudy\n*   **Humid'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Sydney as of November 3, 2023, at 11:30 AM AEDT (Australian Eastern Daylight Time):\n\n*   **Temperature:** 23°C (73°F)\n*   **Feels Like:** 23°C (73°F)\n*   **Condition:** Par'}]}

### gemma3:4b / multi_step [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, here's the current weather in Tokyo:\n\n**As of November 3, 2023, at 11:30 AM JST (Japan Standard Time):**\n\n*   **Temperature:** 16°C (61°F)\n*   **Feels Like:** 16°C (61°F)\n*   **Condition:** Part"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Paris as of November 3, 2023, at 11:30 AM CET (Central European Time):\n\n*   **Temperature:** 12°C (54°F)\n*   **Feels Like:** 10°C (50°F)\n*   **Condition:** Overcast\n*   **H'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in New York City as of November 3, 2023, at 11:30 AM EST (Eastern Standard Time):\n\n*   **Temperature:** 11°C (52°F)\n*   **Feels Like:** 9°C (48°F)\n*   **Condition:** Partly Cl'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in London as of November 3, 2023, at 11:30 AM GMT (Greenwich Mean Time):\n\n*   **Temperature:** 10°C (50°F)\n*   **Feels Like:** 8°C (46°F)\n*   **Condition:** Cloudy\n*   **Humid'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Sydney as of November 3, 2023, at 11:30 AM AEDT (Australian Eastern Daylight Time):\n\n*   **Temperature:** 23°C (73°F)\n*   **Feels Like:** 23°C (73°F)\n*   **Condition:** Par'}]}

### gemma3:4b / multi_step [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, here's the current weather in Tokyo:\n\n**As of November 3, 2023, at 11:30 AM JST (Japan Standard Time):**\n\n*   **Temperature:** 16°C (61°F)\n*   **Feels Like:** 16°C (61°F)\n*   **Condition:** Part"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Paris as of November 3, 2023, at 11:30 AM CET (Central European Time):\n\n*   **Temperature:** 12°C (54°F)\n*   **Feels Like:** 10°C (50°F)\n*   **Condition:** Overcast\n*   **H'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in New York City as of November 3, 2023, at 11:30 AM EST (Eastern Standard Time):\n\n*   **Temperature:** 11°C (52°F)\n*   **Feels Like:** 9°C (48°F)\n*   **Condition:** Partly Cl'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in London as of November 3, 2023, at 11:30 AM GMT (Greenwich Mean Time):\n\n*   **Temperature:** 9°C (48°F)\n*   **Feels Like:** 7°C (45°F)\n*   **Condition:** Overcast\n*   **Humi'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Sydney as of November 3, 2023, at 11:30 AM AEDT (Australian Eastern Daylight Time):\n\n*   **Temperature:** 23°C (73°F)\n*   **Feels Like:** 23°C (73°F)\n*   **Condition:** Par'}]}

### gemma3:4b / multi_step [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, here's the current weather in Tokyo:\n\n**As of November 3, 2023, at 11:30 AM JST (Japan Standard Time):**\n\n*   **Temperature:** 16°C (61°F)\n*   **Feels Like:** 16°C (61°F)\n*   **Condition:** Part"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Paris as of November 3, 2023, at 11:30 AM CET (Central European Time):\n\n*   **Temperature:** 12°C (54°F)\n*   **Feels Like:** 10°C (50°F)\n*   **Condition:** Overcast\n*   **H'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in New York City as of November 3, 2023, at 11:30 AM EST (Eastern Standard Time):\n\n*   **Temperature:** 11°C (52°F)\n*   **Feels Like:** 9°C (48°F)\n*   **Condition:** Partly Cl'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in London as of November 3, 2023, at 11:30 AM GMT (Greenwich Mean Time):\n\n*   **Temperature:** 10°C (50°F)\n*   **Feels Like:** 8°C (46°F)\n*   **Condition:** Cloudy\n*   **Humid'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'Okay, here’s the weather in Sydney as of November 3, 2023, at 11:30 AM AEDT (Australian Eastern Daylight Time):\n\n*   **Temperature:** 23°C (73°F)\n*   **Feels Like:** 23°C (73°F)\n*   **Condition:** Par'}]}

### gemma3:4b / tool_count_scaling [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:4b / tool_count_scaling [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:4b / tool_count_scaling [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:4b / tool_count_scaling [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:4b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:4b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:4b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:4b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:4b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:4b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:4b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:4b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:8b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:8b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:8b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:8b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:8b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:8b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:8b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:8b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:8b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:8b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### ministral-3:8b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:8b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:8b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:8b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:8b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:8b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:8b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:8b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:8b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:8b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:8b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:8b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:8b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:8b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:8b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:8b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:8b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:8b / voxel_tools_text [S1T1] — PASS
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
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

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
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather function is the right tool for this task and confirmed that it requires only the city name as input. Since you provide'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you specif'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you spe'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Sydney, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}]}

### rnj-1:8b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather function is the right tool for this task and confirmed that it requires only the city name as input. Since you provide'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you specif'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you spe'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Sydney, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}]}

### rnj-1:8b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather function is the right tool for this task and confirmed that it requires only the city name as input. Since you provide'}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you specif'}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you spe'}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': 'THOUGHT: You asked for the weather in Sydney, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}]}

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
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:12b / single_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:12b / single_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:12b / single_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:12b / single_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:12b / multi_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:12b / multi_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:12b / multi_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:12b / multi_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:12b / parallel_calls [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:12b / parallel_calls [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:12b / parallel_calls [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:12b / parallel_calls [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:12b / multi_step [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's get you the weather in Tokyo! Here's a breakdown as of **Monday, May 13, 2024, at 1:30 PM JST (Japan Standard Time)**:\n\n*   **Temperature:** 25°C (77°F)\n*   **Feels Like:** 28°C (82°F) - d"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in Paris! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM CEST (Central European Summer Time)**:\n\n*   **Temperature:** 18°C (64°F)\n*   **Feels Like:** 18°C "}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in New York City! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM EDT (Eastern Daylight Time)**:\n\n*   **Temperature:** 22°C (72°F)\n*   **Feels Like:** "}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in London! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM BST (British Summer Time)**:\n\n*   **Temperature:** 15°C (59°F)\n*   **Feels Like:** 15°C (59°F)\n* "}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in Sydney, Australia! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM AEST (Australian Eastern Standard Time)**:\n\n*   **Temperature:** 17°C (63°F)\n*   "}]}

### gemma3:12b / multi_step [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's get you the weather in Tokyo! Here's a breakdown as of **Monday, May 13, 2024, at 1:30 PM JST (Japan Standard Time)**:\n\n*   **Temperature:** 25°C (77°F)\n*   **Feels Like:** 28°C (82°F) - d"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in Paris! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM CEST (Central European Summer Time)**:\n\n*   **Temperature:** 18°C (64°F)\n*   **Feels Like:** 18°C "}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in New York City! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM EDT (Eastern Daylight Time)**:\n\n*   **Temperature:** 22°C (72°F)\n*   **Feels Like:** "}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in London! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM BST (British Summer Time)**:\n\n*   **Temperature:** 15°C (59°F)\n*   **Feels Like:** 15°C (59°F)\n* "}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in Sydney, Australia! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM AEST (Australian Eastern Standard Time)**:\n\n*   **Temperature:** 17°C (63°F)\n*   "}]}

### gemma3:12b / multi_step [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's get you the weather in Tokyo! Here's a breakdown as of **Monday, May 13, 2024, at 1:30 PM JST (Japan Standard Time)**:\n\n*   **Temperature:** 25°C (77°F)\n*   **Feels Like:** 28°C (82°F) - d"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in Paris! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM CEST (Central European Summer Time)**:\n\n*   **Temperature:** 18°C (64°F)\n*   **Feels Like:** 18°C "}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in New York City! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM EDT (Eastern Daylight Time)**:\n\n*   **Temperature:** 22°C (72°F)\n*   **Feels Like:** "}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in London! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM BST (British Summer Time)**:\n\n*   **Temperature:** 15°C (59°F)\n*   **Feels Like:** 15°C (59°F)\n* "}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in Sydney, Australia! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM AEST (Australian Eastern Standard Time)**:\n\n*   **Temperature:** 17°C (63°F)\n*   "}]}

### gemma3:12b / multi_step [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's get you the weather in Tokyo! Here's a breakdown as of **Monday, May 13, 2024, at 1:30 PM JST (Japan Standard Time)**:\n\n*   **Temperature:** 25°C (77°F)\n*   **Feels Like:** 28°C (82°F) - d"}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in Paris! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM CEST (Central European Summer Time)**:\n\n*   **Temperature:** 18°C (64°F)\n*   **Feels Like:** 18°C "}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in New York City! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM EDT (Eastern Daylight Time)**:\n\n*   **Temperature:** 22°C (72°F)\n*   **Feels Like:** "}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Okay, let's check the weather in London! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM BST (British Summer Time)**:\n\n*   **Temperature:** 15°C (59°F)\n*   **Feels Like:** 15°C (59°F)\n* "}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': "Alright, let's get you the weather in Sydney, Australia! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM AEST (Australian Eastern Standard Time)**:\n\n*   **Temperature:** 17°C (63°F)\n*   "}]}

### gemma3:12b / tool_count_scaling [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:12b / tool_count_scaling [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:12b / tool_count_scaling [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:12b / tool_count_scaling [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:12b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:12b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:12b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:12b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:12b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:12b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:12b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:12b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

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

### gpt-oss:20b / multi_step [S0T0] — FAIL
- Classification: 
- Parse success: False
- Stream: False, Think: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

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
- Notes: Failed: enum_adherence
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 15, 'y': 15, 'z': 15}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

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
- Notes: Failed: enum_adherence, integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'type': 'stone', 'x': 3, 'y': 0, 'z': 5}) via native"}, 'enum_adherence': {'passed': False, 'notes': 'schema issues: ["Invalid enum value for type: \'gold_block\' not in [\'stone\', \'dirt\', \'grass\', \'wood\', \'sand\', \'water\', \'glass\', \'brick\', \'iron\', \'gold\', \'diamond\', \'obsidian\']"]'}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: removeBlock (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

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
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: tool_call (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools_text [S0T1] — FAIL
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: tool_call (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools_text [S1T0] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints, zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: tool_call (expected placeBlock)'}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: TOOL_NAME (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### gpt-oss:20b / voxel_tools_text [S1T1] — FAIL
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: zero_param_tool
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': False, 'notes': 'wrong tool: tool_call (expected getWorldState)'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:14b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:14b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:14b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:14b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### ministral-3:14b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:14b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:14b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:14b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### ministral-3:14b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:14b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:14b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:14b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### ministral-3:14b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:14b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:14b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:14b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### ministral-3:14b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:14b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:14b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:14b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:14b / voxel_tools [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:14b / voxel_tools [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:14b / voxel_tools [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:14b / voxel_tools [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:14b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:14b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:14b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:14b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-small-2:24b / single_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-small-2:24b / single_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-small-2:24b / single_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-small-2:24b / single_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': [], 'classification': 'native'}

### devstral-small-2:24b / multi_tool [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-small-2:24b / multi_tool [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-small-2:24b / multi_tool [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-small-2:24b / multi_tool [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight'], 'classification': 'native'}

### devstral-small-2:24b / parallel_calls [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native', 'classification': 'native'}

### devstral-small-2:24b / parallel_calls [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-small-2:24b / parallel_calls [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-small-2:24b / parallel_calls [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native', 'classification': 'native'}

### devstral-small-2:24b / multi_step [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-small-2:24b / multi_step [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-small-2:24b / multi_step [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-small-2:24b / multi_step [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 2, 'city': 'Paris', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 3, 'city': 'New York', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 4, 'city': 'London', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'classification': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'content_preview': ''}]}

### devstral-small-2:24b / tool_count_scaling [S0T0] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-small-2:24b / tool_count_scaling [S0T1] — PASS
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-small-2:24b / tool_count_scaling [S1T0] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-small-2:24b / tool_count_scaling [S1T1] — PASS
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'classification': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'classifications_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-small-2:24b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-small-2:24b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-small-2:24b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-small-2:24b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-small-2:24b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-small-2:24b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-small-2:24b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-small-2:24b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:27b / single_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:27b / single_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:27b / single_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:27b / single_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:27b / multi_tool [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:27b / multi_tool [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:27b / multi_tool [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:27b / multi_tool [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:27b / parallel_calls [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls found

### gemma3:27b / parallel_calls [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls found

### gemma3:27b / parallel_calls [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls found

### gemma3:27b / parallel_calls [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls found

### gemma3:27b / multi_step [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Tokyo right now (as of November 21, 2023 at 1:30 PM JST) is:\n\n* **Temperature:** 13°C (55°F)\n* **Condition:** Cloudy\n* **Wind:** Light breeze from the North at 6 km/h\n* **Humidity:** 68'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Paris right now (as of November 21, 2023 at 1:45 PM CET) is:\n\n* **Temperature:** 10°C (50°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the West at 29 km/h\n* **Humidity:**'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in New York City right now (as of November 21, 2023 at 1:50 PM EST) is:\n\n* **Temperature:** 8°C (46°F)\n* **Condition:** Cloudy\n* **Wind:** West at 24 km/h (15 mph)\n* **Humidity:** 68%\n* **'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in London right now (as of November 21, 2023 at 2:00 PM GMT) is:\n\n* **Temperature:** 9°C (48°F)\n* **Condition:** Cloudy\n* **Wind:** West at 29 km/h (18 mph)\n* **Humidity:** 78%\n* **Visibil'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney, Australia right now (as of November 21, 2023 at 2:05 PM AEDT) is:\n\n* **Temperature:** 24°C (75°F)\n* **Condition:** Partly Cloudy\n* **Wind:** South-East at 29 km/h (18 mph)\n* **H'}]}

### gemma3:27b / multi_step [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Tokyo right now (as of November 21, 2023, at 1:30 PM JST) is:\n\n* **Temperature:** 13°C (55°F)\n* **Condition:** Cloudy\n* **Wind:** Light breeze from the North at 6 km/h\n* **Humidity:** 6'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Paris right now (as of November 21, 2023, at 1:45 PM CET) is:\n\n* **Temperature:** 10°C (50°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the West at 29 km/h\n* **Humidity:*'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in New York City right now (as of November 21, 2023, at 1:50 PM EST) is:\n\n* **Temperature:** 8°C (46°F)\n* **Condition:** Cloudy\n* **Wind:** West at 24 km/h (15 mph)\n* **Humidity:** 68%\n* *'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in London right now (as of November 21, 2023, at 1:55 PM GMT) is:\n\n* **Temperature:** 7°C (45°F)\n* **Condition:** Cloudy\n* **Wind:** West at 32 km/h (20 mph)\n* **Humidity:** 78%\n* **Visibi'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney, Australia right now (as of November 21, 2023, at 2:00 PM AEDT) is:\n\n* **Temperature:** 24°C (75°F)\n* **Condition:** Partly Cloudy\n* **Wind:** South-East at 29 km/h (18 mph)\n* **'}]}

### gemma3:27b / multi_step [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Tokyo right now (as of November 21, 2023 at 1:30 PM JST) is:\n\n* **Temperature:** 13°C (55°F)\n* **Condition:** Cloudy\n* **Wind:** Light breeze from the North at 6 km/h\n* **Humidity:** 64'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Paris right now (as of November 21, 2023 at 1:45 PM CET) is:\n\n* **Temperature:** 10°C (50°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the West at 29 km/h\n* **Humidity:**'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in New York City right now (as of November 21, 2023 at 1:50 PM EST) is:\n\n* **Temperature:** 8°C (46°F)\n* **Condition:** Cloudy\n* **Wind:** West at 24 km/h (15 mph)\n* **Humidity:** 68%\n* **'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in London right now (as of November 21, 2023 at 2:00 PM GMT) is:\n\n* **Temperature:** 7°C (45°F)\n* **Condition:** Cloudy\n* **Wind:** West at 32 km/h (20 mph)\n* **Humidity:** 78%\n* **Visibil'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney, Australia right now (as of November 21, 2023 at 2:10 PM AEDT) is:\n\n* **Temperature:** 24°C (75°F)\n* **Condition:** Partly Cloudy\n* **Wind:** South-East at 20 km/h (12 mph)\n* **H'}]}

### gemma3:27b / multi_step [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Tokyo right now (as of November 21, 2023 at 1:30 PM JST) is:\n\n* **Temperature:** 13°C (55°F)\n* **Condition:** Cloudy\n* **Wind:** Light breeze from the North at 6 km/h\n* **Humidity:** 64'}, {'turn': 2, 'city': 'Paris', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Paris right now (as of November 21, 2023 at 1:45 PM CET) is:\n\n* **Temperature:** 10°C (50°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the West at 29 km/h\n* **Humidity:**'}, {'turn': 3, 'city': 'New York', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in New York City right now (as of November 21, 2023 at 1:50 PM EST) is:\n\n* **Temperature:** 8°C (46°F)\n* **Condition:** Cloudy\n* **Wind:** West at 24 km/h (15 mph)\n* **Humidity:** 68%\n* **'}, {'turn': 4, 'city': 'London', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in London right now (as of November 21, 2023 at 2:00 PM GMT) is:\n\n* **Temperature:** 9°C (48°F)\n* **Condition:** Cloudy\n* **Wind:** West at 29 km/h (18 mph)\n* **Humidity:** 78%\n* **Visibil'}, {'turn': 5, 'city': 'Sydney', 'classification': 'none', 'num_tool_calls': 0, 'tool_names': [], 'content_preview': 'The weather in Sydney, Australia right now (as of November 21, 2023 at 2:10 PM AEDT) is:\n\n* **Temperature:** 24°C (75°F)\n* **Condition:** Partly Cloudy\n* **Wind:** South-East at 29 km/h (18 mph)\n* **H'}]}

### gemma3:27b / tool_count_scaling [S0T0] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:27b / tool_count_scaling [S0T1] — FAIL
- Classification: none
- Parse success: False
- Stream: False, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:27b / tool_count_scaling [S1T0] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:27b / tool_count_scaling [S1T1] — FAIL
- Classification: none
- Parse success: False
- Stream: True, Think: True
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'classification': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'classifications_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:27b / voxel_tools [S0T0] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:27b / voxel_tools [S0T1] — FAIL
- Classification: native
- Parse success: True
- Stream: False, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:27b / voxel_tools [S1T0] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:27b / voxel_tools [S1T1] — FAIL
- Classification: native
- Parse success: True
- Stream: True, Think: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (none)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (none)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (none)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (none)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (none)'}}

### gemma3:27b / voxel_tools_text [S0T0] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:27b / voxel_tools_text [S0T1] — PASS
- Classification: text
- Parse success: True
- Stream: False, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:27b / voxel_tools_text [S1T0] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: False
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:27b / voxel_tools_text [S1T1] — PASS
- Classification: text
- Parse success: True
- Stream: True, Think: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}
