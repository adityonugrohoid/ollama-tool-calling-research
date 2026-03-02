# Test Results — 20260302T165536

**Models:** ministral-3:3b, gemma3:4b, ministral-3:8b, rnj-1:8b, gemma3:12b, gpt-oss:20b, ministral-3:14b, devstral-small-2:24b, gemma3:27b
**Tests:** test_single_tool, test_multi_tool, test_parallel_calls, test_multi_step, test_streaming_tools, test_tool_count_scaling, test_thinking_with_tools, test_text_fallback, test_voxel_tools, test_voxel_tools_text

| Model | test_single_tool | test_multi_tool | test_parallel_calls | test_multi_step | test_streaming_tools | test_tool_count_scaling | test_thinking_with_tools | test_text_fallback | test_voxel_tools | test_voxel_tools_text |
|-------|------|------|------|------|------|------|------|------|------|------|
| ministral-3:3b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) | PASS (native) | PASS (text) |
| gemma3:4b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | PASS (text) | FAIL (native) | PASS (text) |
| ministral-3:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) | PASS (native) | PASS (text) |
| rnj-1:8b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) | FAIL (error) | FAIL (text) |
| gemma3:12b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | PASS (text) | FAIL (native) | PASS (text) |
| gpt-oss:20b | PASS (native) | PASS (native) | FAIL (native) | FAIL (error) | PASS (native) | PASS (native) | PASS (native) | FAIL (text) | FAIL (error) | FAIL (text) |
| ministral-3:14b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) | PASS (native) | PASS (text) |
| devstral-small-2:24b | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (native) | PASS (text) | FAIL (native) | PASS (text) |
| gemma3:27b | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | FAIL (none) | PASS (text) | FAIL (native) | PASS (text) |

## Detailed Results

### ministral-3:3b / test_single_tool — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': []}

### ministral-3:3b / test_multi_tool — PASS
- Format: native
- Parse success: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight']}

### ministral-3:3b / test_parallel_calls — PASS
- Format: native
- Parse success: True
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native'}

### ministral-3:3b / test_multi_step — PASS
- Format: native
- Parse success: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 2, 'city': 'Paris', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': "I currently don't have real-time weather data for Paris, but I can help you check it! Let me fetch the weather for you."}, {'turn': 3, 'city': 'New York', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 4, 'city': 'London', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': "I'm checking the weather for you! Let me find out what it's like in Sydney."}]}

### ministral-3:3b / test_streaming_tools — PASS
- Format: native
- Parse success: True
- Notes: Non-stream: OK (native); Stream: OK (native)
- Details: {'nostream_success': True, 'nostream_format': 'native', 'stream_success': True, 'stream_format': 'native', 'consistent': True}

### ministral-3:3b / test_tool_count_scaling — PASS
- Format: native
- Parse success: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'formats_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:3b / test_thinking_with_tools — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, Thinking: no
- Details: {'has_thinking': False, 'thinking_length': 0, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'corruption_detected': False, 'source': 'native'}

### ministral-3:3b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### ministral-3:3b / test_voxel_tools — PASS
- Format: native
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:3b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:4b / test_single_tool — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:4b / test_multi_tool — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:4b / test_parallel_calls — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:4b / test_multi_step — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': "Okay, here's the current weather in Tokyo:\n\n**As of November 3, 2023, at 11:30 AM JST (Japan Standard Time):**\n\n*   **Temperature:** 16°C (61°F)\n*   **Feels Like:** 16°C (61°F)\n*   **Condition:** Part"}, {'turn': 2, 'city': 'Paris', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'Okay, here’s the weather in Paris as of November 3, 2023, at 11:30 AM CET (Central European Time):\n\n*   **Temperature:** 12°C (54°F)\n*   **Feels Like:** 10°C (50°F)\n*   **Condition:** Overcast\n*   **H'}, {'turn': 3, 'city': 'New York', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'Okay, here’s the weather in New York City as of November 3, 2023, at 11:30 AM EST (Eastern Standard Time):\n\n*   **Temperature:** 11°C (52°F)\n*   **Feels Like:** 9°C (48°F)\n*   **Condition:** Partly Cl'}, {'turn': 4, 'city': 'London', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'Okay, here’s the weather in London as of November 3, 2023, at 11:30 AM GMT (Greenwich Mean Time):\n\n*   **Temperature:** 10°C (50°F)\n*   **Feels Like:** 8°C (46°F)\n*   **Condition:** Cloudy\n*   **Humid'}, {'turn': 5, 'city': 'Sydney', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'Okay, here’s the weather in Sydney as of November 3, 2023, at 11:30 AM AEDT (Australian Eastern Daylight Time):\n\n*   **Temperature:** 23°C (73°F)\n*   **Feels Like:** 23°C (73°F)\n*   **Condition:** Par'}]}

### gemma3:4b / test_streaming_tools — FAIL
- Format: none
- Parse success: False
- Notes: Non-stream: FAIL (none); Stream: FAIL (none)
- Details: {'nostream_success': False, 'nostream_format': 'none', 'stream_success': False, 'stream_format': 'none', 'consistent': None}

### gemma3:4b / test_tool_count_scaling — FAIL
- Format: none
- Parse success: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'formats_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:4b / test_thinking_with_tools — FAIL
- Format: none
- Parse success: False
- Notes: ; No tool_calls in response
- Details: {'has_thinking': False, 'thinking_length': 0}

### gemma3:4b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### gemma3:4b / test_voxel_tools — FAIL
- Format: native
- Parse success: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}}

### gemma3:4b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### ministral-3:8b / test_single_tool — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': []}

### ministral-3:8b / test_multi_tool — PASS
- Format: native
- Parse success: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight']}

### ministral-3:8b / test_parallel_calls — PASS
- Format: native
- Parse success: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native'}

### ministral-3:8b / test_multi_step — PASS
- Format: native
- Parse success: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 2, 'city': 'Paris', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 3, 'city': 'New York', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 4, 'city': 'London', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}]}

### ministral-3:8b / test_streaming_tools — PASS
- Format: native
- Parse success: True
- Notes: Non-stream: OK (native); Stream: OK (native)
- Details: {'nostream_success': True, 'nostream_format': 'native', 'stream_success': True, 'stream_format': 'native', 'consistent': True}

### ministral-3:8b / test_tool_count_scaling — PASS
- Format: native
- Parse success: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'formats_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:8b / test_thinking_with_tools — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, Thinking: no
- Details: {'has_thinking': False, 'thinking_length': 0, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'corruption_detected': False, 'source': 'native'}

### ministral-3:8b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### ministral-3:8b / test_voxel_tools — PASS
- Format: native
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:8b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### rnj-1:8b / test_single_tool — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': []}

### rnj-1:8b / test_multi_tool — PASS
- Format: native
- Parse success: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight']}

### rnj-1:8b / test_parallel_calls — PASS
- Format: native
- Parse success: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native'}

### rnj-1:8b / test_multi_step — PASS
- Format: native
- Parse success: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': 'THOUGHT: You asked for the weather in Tokyo, so I identified that the get_weather function is the right tool for this task and confirmed that it requires only the city name as input. Since you provide'}, {'turn': 2, 'city': 'Paris', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': 'THOUGHT: You asked for the weather in Paris, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you specif'}, {'turn': 3, 'city': 'New York', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': 'THOUGHT: You asked for the weather in New York, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you spe'}, {'turn': 4, 'city': 'London', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': 'THOUGHT: You asked for the weather in London, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}, {'turn': 5, 'city': 'Sydney', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': 'THOUGHT: You asked for the weather in Sydney, so I need to retrieve that information using the available tool. I recall that the get_weather function requires a city name as input, and since you speci'}]}

### rnj-1:8b / test_streaming_tools — PASS
- Format: native
- Parse success: True
- Notes: Non-stream: OK (native); Stream: OK (native)
- Details: {'nostream_success': True, 'nostream_format': 'native', 'stream_success': True, 'stream_format': 'native', 'consistent': True}

### rnj-1:8b / test_tool_count_scaling — PASS
- Format: native
- Parse success: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'formats_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### rnj-1:8b / test_thinking_with_tools — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, Thinking: no
- Details: {'has_thinking': False, 'thinking_length': 0, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'corruption_detected': False, 'source': 'native'}

### rnj-1:8b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### rnj-1:8b / test_voxel_tools — FAIL
- Format: error
- Parse success: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### rnj-1:8b / test_voxel_tools_text — FAIL
- Format: text
- Parse success: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'type': 'gold', 'x': 7, 'y': 1, 'z': 7}) via text"}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:12b / test_single_tool — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:12b / test_multi_tool — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:12b / test_parallel_calls — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:12b / test_multi_step — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': "Okay, let's get you the weather in Tokyo! Here's a breakdown as of **Monday, May 13, 2024, at 1:30 PM JST (Japan Standard Time)**:\n\n*   **Temperature:** 25°C (77°F)\n*   **Feels Like:** 28°C (82°F) - d"}, {'turn': 2, 'city': 'Paris', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': "Okay, let's check the weather in Paris! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM CEST (Central European Summer Time)**:\n\n*   **Temperature:** 18°C (64°F)\n*   **Feels Like:** 18°C "}, {'turn': 3, 'city': 'New York', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': "Alright, let's get you the weather in New York City! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM EDT (Eastern Daylight Time)**:\n\n*   **Temperature:** 22°C (72°F)\n*   **Feels Like:** "}, {'turn': 4, 'city': 'London', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': "Okay, let's check the weather in London! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM BST (British Summer Time)**:\n\n*   **Temperature:** 15°C (59°F)\n*   **Feels Like:** 15°C (59°F)\n* "}, {'turn': 5, 'city': 'Sydney', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': "Alright, let's get you the weather in Sydney, Australia! Here's the breakdown as of **Monday, May 13, 2024, at 1:30 PM AEST (Australian Eastern Standard Time)**:\n\n*   **Temperature:** 17°C (63°F)\n*   "}]}

### gemma3:12b / test_streaming_tools — FAIL
- Format: none
- Parse success: False
- Notes: Non-stream: FAIL (none); Stream: FAIL (none)
- Details: {'nostream_success': False, 'nostream_format': 'none', 'stream_success': False, 'stream_format': 'none', 'consistent': None}

### gemma3:12b / test_tool_count_scaling — FAIL
- Format: none
- Parse success: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'formats_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:12b / test_thinking_with_tools — FAIL
- Format: none
- Parse success: False
- Notes: ; No tool_calls in response
- Details: {'has_thinking': False, 'thinking_length': 0}

### gemma3:12b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### gemma3:12b / test_voxel_tools — FAIL
- Format: native
- Parse success: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}}

### gemma3:12b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gpt-oss:20b / test_single_tool — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': []}

### gpt-oss:20b / test_multi_tool — PASS
- Format: native
- Parse success: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight']}

### gpt-oss:20b / test_parallel_calls — FAIL
- Format: native
- Parse success: True
- Notes: Expected 2+ tool calls, got 1; All calls to same tool: {'get_weather'}
- Details: {'num_tool_calls': 1, 'tool_names': ['get_weather'], 'source': 'native'}

### gpt-oss:20b / test_multi_step — FAIL
- Format: error
- Parse success: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### gpt-oss:20b / test_streaming_tools — PASS
- Format: native
- Parse success: True
- Notes: Non-stream: OK (native); Stream: OK (native)
- Details: {'nostream_success': True, 'nostream_format': 'native', 'stream_success': True, 'stream_format': 'native', 'consistent': True}

### gpt-oss:20b / test_tool_count_scaling — PASS
- Format: native
- Parse success: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'formats_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### gpt-oss:20b / test_thinking_with_tools — PASS
- Format: native
- Parse success: True
- Notes: Thinking: 126 chars
- Details: {'has_thinking': True, 'thinking_length': 126, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'corruption_detected': False, 'source': 'native'}

### gpt-oss:20b / test_text_fallback — FAIL
- Format: text
- Parse success: False
- Notes: Parse rate: 0/3 (0%)
- Details: {'successes': 0, 'failures': 3, 'success_rate': 0.0, 'attempts': [{'attempt': 1, 'parsed': False, 'error': 'No text content to parse', 'raw_preview': ''}, {'attempt': 2, 'parsed': False, 'error': 'No text content to parse', 'raw_preview': ''}, {'attempt': 3, 'parsed': False, 'error': 'No text content to parse', 'raw_preview': ''}]}

### gpt-oss:20b / test_voxel_tools — FAIL
- Format: error
- Parse success: False
- Notes: Exception: ResponseError
- Error: Internal Server Error (status code: 500)

### gpt-oss:20b / test_voxel_tools_text — FAIL
- Format: text
- Parse success: False
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (No text content to parse)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (No text content to parse)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (No text content to parse)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (No text content to parse)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (No text content to parse)'}}

### ministral-3:14b / test_single_tool — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': []}

### ministral-3:14b / test_multi_tool — PASS
- Format: native
- Parse success: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight']}

### ministral-3:14b / test_parallel_calls — PASS
- Format: native
- Parse success: True
- Notes: Tools called: ['get_weather', 'get_population']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_weather', 'get_population'], 'source': 'native'}

### ministral-3:14b / test_multi_step — PASS
- Format: native
- Parse success: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 2, 'city': 'Paris', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 3, 'city': 'New York', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 4, 'city': 'London', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}]}

### ministral-3:14b / test_streaming_tools — PASS
- Format: native
- Parse success: True
- Notes: Non-stream: OK (native); Stream: OK (native)
- Details: {'nostream_success': True, 'nostream_format': 'native', 'stream_success': True, 'stream_format': 'native', 'consistent': True}

### ministral-3:14b / test_tool_count_scaling — PASS
- Format: native
- Parse success: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'formats_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### ministral-3:14b / test_thinking_with_tools — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, Thinking: no
- Details: {'has_thinking': False, 'thinking_length': 0, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'corruption_detected': False, 'source': 'native'}

### ministral-3:14b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### ministral-3:14b / test_voxel_tools — PASS
- Format: native
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via native"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### ministral-3:14b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### devstral-small-2:24b / test_single_tool — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, City: Tokyo
- Details: {'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'source': 'native', 'schema_valid': True, 'schema_issues': []}

### devstral-small-2:24b / test_multi_tool — PASS
- Format: native
- Parse success: True
- Notes: Correctly selected get_weather
- Details: {'num_tool_calls': 1, 'tool_name': 'get_weather', 'arguments': {'city': 'Paris'}, 'source': 'native', 'available_tools': ['get_weather', 'search_restaurants', 'book_flight']}

### devstral-small-2:24b / test_parallel_calls — PASS
- Format: native
- Parse success: True
- Notes: Tools called: ['get_population', 'get_weather']
- Details: {'num_tool_calls': 2, 'tool_names': ['get_population', 'get_weather'], 'source': 'native'}

### devstral-small-2:24b / test_multi_step — PASS
- Format: native
- Parse success: True
- Notes: Successful turns: 5/5; Turn formats: ['native', 'native', 'native', 'native', 'native']
- Details: {'turn_formats': ['native', 'native', 'native', 'native', 'native'], 'format_switched': False, 'successful_turns': 5, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 2, 'city': 'Paris', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 3, 'city': 'New York', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 4, 'city': 'London', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}, {'turn': 5, 'city': 'Sydney', 'format': 'native', 'num_tool_calls': 1, 'tool_names': ['get_weather'], 'raw_content_preview': ''}]}

### devstral-small-2:24b / test_streaming_tools — PASS
- Format: native
- Parse success: True
- Notes: Non-stream: OK (native); Stream: OK (native)
- Details: {'nostream_success': True, 'nostream_format': 'native', 'stream_success': True, 'stream_format': 'native', 'consistent': True}

### devstral-small-2:24b / test_tool_count_scaling — PASS
- Format: native
- Parse success: True
- Notes: Scale: [1:native | 3:native | 5:native | 8:native | 10:native | 15:native]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 3, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 5, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 8, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 10, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}, {'tool_count': 15, 'format': 'native', 'parse_success': True, 'correct_tool': True, 'num_calls': 1, 'tool_names': ['get_weather']}], 'format_switched': False, 'formats_seen': ['native', 'native', 'native', 'native', 'native', 'native']}

### devstral-small-2:24b / test_thinking_with_tools — PASS
- Format: native
- Parse success: True
- Notes: Tool: get_weather, Thinking: no
- Details: {'has_thinking': False, 'thinking_length': 0, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}, 'corruption_detected': False, 'source': 'native'}

### devstral-small-2:24b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### devstral-small-2:24b / test_voxel_tools — FAIL
- Format: native
- Parse success: True
- Notes: Failed: integer_constraints
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via native"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via native"}, 'integer_constraints': {'passed': False, 'notes': 'wrong tool: getWorldState (expected placeBlock)'}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via native'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via native"}}

### devstral-small-2:24b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}

### gemma3:27b / test_single_tool — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:27b / test_multi_tool — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:27b / test_parallel_calls — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls found in text content

### gemma3:27b / test_multi_step — FAIL
- Format: none
- Parse success: False
- Notes: No tool calls in any turn; Successful turns: 0/5; Turn formats: ['none', 'none', 'none', 'none', 'none']
- Details: {'turn_formats': ['none', 'none', 'none', 'none', 'none'], 'format_switched': False, 'successful_turns': 0, 'turns': [{'turn': 1, 'city': 'Tokyo', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'The weather in Tokyo right now (as of November 21, 2023 at 1:30 PM JST) is:\n\n* **Temperature:** 13°C (55°F)\n* **Condition:** Cloudy\n* **Wind:** Light breeze from the North at 6 km/h\n* **Humidity:** 68'}, {'turn': 2, 'city': 'Paris', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'The weather in Paris right now (as of November 21, 2023 at 1:45 PM CET) is:\n\n* **Temperature:** 10°C (50°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the West at 29 km/h\n* **Humidity:**'}, {'turn': 3, 'city': 'New York', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'The weather in New York City right now (as of November 21, 2023 at 1:50 PM EST) is:\n\n* **Temperature:** 8°C (46°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the Northwest at 24 km/h\n* *'}, {'turn': 4, 'city': 'London', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'The weather in London right now (as of November 21, 2023 at 2:00 PM GMT) is:\n\n* **Temperature:** 7°C (45°F)\n* **Condition:** Cloudy\n* **Wind:** Moderate breeze from the West at 26 km/h\n* **Humidity:**'}, {'turn': 5, 'city': 'Sydney', 'format': 'none', 'num_tool_calls': 0, 'tool_names': [], 'raw_content_preview': 'The weather in Sydney, Australia right now (as of November 21, 2023 at 2:10 PM AEDT) is:\n\n* **Temperature:** 24°C (75°F)\n* **Condition:** Partly Cloudy\n* **Wind:** Light breeze from the Northeast at 1'}]}

### gemma3:27b / test_streaming_tools — FAIL
- Format: none
- Parse success: False
- Notes: Non-stream: FAIL (none); Stream: FAIL (none)
- Details: {'nostream_success': False, 'nostream_format': 'none', 'stream_success': False, 'stream_format': 'none', 'consistent': None}

### gemma3:27b / test_tool_count_scaling — FAIL
- Format: none
- Parse success: False
- Notes: Scale: [1:none | 3:none | 5:none | 8:none | 10:none | 15:none]
- Details: {'scale_results': [{'tool_count': 1, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 3, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 5, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 8, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 10, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}, {'tool_count': 15, 'format': 'none', 'parse_success': False, 'correct_tool': False, 'num_calls': 0, 'tool_names': []}], 'format_switched': False, 'formats_seen': ['none', 'none', 'none', 'none', 'none', 'none']}

### gemma3:27b / test_thinking_with_tools — FAIL
- Format: none
- Parse success: False
- Notes: ; No tool_calls in response
- Details: {'has_thinking': False, 'thinking_length': 0}

### gemma3:27b / test_text_fallback — PASS
- Format: text
- Parse success: True
- Notes: Parse rate: 3/3 (100%); Correct tool: 3/3
- Details: {'successes': 3, 'failures': 0, 'success_rate': 1.0, 'attempts': [{'attempt': 1, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 2, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}, {'attempt': 3, 'parsed': True, 'correct_tool': True, 'tool_name': 'get_weather', 'arguments': {'city': 'Tokyo'}}]}

### gemma3:27b / test_voxel_tools — FAIL
- Format: native
- Parse success: True
- Notes: Failed: tool_selection, enum_adherence, integer_constraints, zero_param_tool, tool_discrimination
- Details: {'tool_selection': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'enum_adherence': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'integer_constraints': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'zero_param_tool': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}, 'tool_discrimination': {'passed': False, 'notes': 'no tool calls (No tool calls found in text content)'}}

### gemma3:27b / test_voxel_tools_text — PASS
- Format: text
- Parse success: True
- Notes: All 5 sub-checks passed
- Details: {'tool_selection': {'passed': True, 'notes': "placeBlock({'x': 3, 'y': 0, 'z': 5, 'type': 'stone'}) via text"}, 'enum_adherence': {'passed': True, 'notes': "placeBlock({'x': 7, 'y': 1, 'z': 7, 'type': 'gold'}) via text"}, 'integer_constraints': {'passed': True, 'notes': "placeBlock({'x': 15, 'y': 15, 'z': 15, 'type': 'stone'}) via text"}, 'zero_param_tool': {'passed': True, 'notes': 'getWorldState({}) via text'}, 'tool_discrimination': {'passed': True, 'notes': "removeBlock({'x': 3, 'y': 0, 'z': 5}) via text"}}
