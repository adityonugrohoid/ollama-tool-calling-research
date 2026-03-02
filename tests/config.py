"""Shared test configuration: model lists, tool definitions, default options."""

# Reproducible test options
DEFAULT_OPTIONS: dict = {
    "temperature": 0,
    "seed": 42,
    "num_ctx": 4096,
}

# Model priority tiers (based on actual Ollama Cloud availability)
# Source: model-library.json fetched from https://ollama.com/api/tags
# Total: 32 models — 29 with tools, 3 without (gemma3 family)

# P0: Small/fast models, <30B — best for quick iteration
P0_MODELS: list[str] = [
    "ministral-3:3b",        #  3B, tools+vision — Mistral, smallest stress test
    "gemma3:4b",             #  4B, vision only — NO tools, baseline comparison
    "ministral-3:8b",        #  8B, tools+vision — Mistral
    "rnj-1:8b",              #  8B, tools — Gemma3 family
    "gemma3:12b",            # 12B, vision only — NO tools, baseline comparison
    "gpt-oss:20b",           # 20B, tools+thinking — GPT-OSS
    "ministral-3:14b",       # 14B, tools+vision — Mistral mid-size
    "devstral-small-2:24b",  # 24B, tools+vision — Mistral coding model
    "gemma3:27b",            # 27B, vision only — NO tools, baseline comparison
]

# P1: Medium models, 30B–130B — deeper investigation
P1_MODELS: list[str] = [
    "nemotron-3-nano:30b",   # 30B, tools+thinking — Nvidia
    "qwen3-next:80b",        # 80B, tools+thinking — Qwen (key for mid-conv switching)
    "qwen3-coder-next",      # 80B, tools — Qwen coding model
    "gpt-oss:120b",          # 120B, tools+thinking — large GPT-OSS
    "devstral-2:123b",       # 123B, tools — Mistral large coding model
    "gemini-3-flash-preview", # unknown, tools+thinking — Google
]

# P2: Large models, 200B+ — comprehensive coverage
P2_MODELS: list[str] = [
    "minimax-m2",            # 230B, tools
    "minimax-m2.1",          # 230B, tools+thinking
    "minimax-m2.5",          # 230B, tools+thinking
    "qwen3.5:397b",          # 397B, tools+thinking+vision
    "qwen3-vl:235b",         # 235B, tools+thinking+vision
    "qwen3-vl:235b-instruct",# 235B, tools+vision
    "qwen3-coder:480b",      # 480B, tools — Qwen coder
    "mistral-large-3:675b",  # 675B, tools+vision — largest Mistral
    "deepseek-v3.1:671b",    # 671B, tools+thinking
    "cogito-2.1:671b",       # 671B, tools+thinking
    "deepseek-v3.2",         # 671B, tools+thinking
    "glm-4.6",               # 357B, tools+thinking
    "glm-4.7",               # 357B, tools+thinking
    "glm-5",                 # 756B, tools+thinking
    "kimi-k2:1t",            # 1T, tools
    "kimi-k2.5",             # 1T, tools+thinking+vision
    "kimi-k2-thinking",      # 1T, tools+thinking
]

# Models with thinking capability (for test_thinking_with_tools)
THINKING_MODELS: list[str] = [
    "gpt-oss:20b",
    "gpt-oss:120b",
    "nemotron-3-nano:30b",
    "qwen3-next:80b",
    "gemini-3-flash-preview",
    "minimax-m2.1",
    "minimax-m2.5",
    "qwen3.5:397b",
    "qwen3-vl:235b",
    "deepseek-v3.1:671b",
    "cogito-2.1:671b",
    "deepseek-v3.2",
    "glm-4.6",
    "glm-4.7",
    "glm-5",
    "kimi-k2.5",
    "kimi-k2-thinking",
]

# Models WITHOUT native tool support (no "tools" in capabilities)
# These will fail native tool tests but are useful for text-fallback baseline
NO_TOOLS_MODELS: list[str] = [
    "gemma3:4b",
    "gemma3:12b",
    "gemma3:27b",
]

ALL_MODELS: list[str] = P0_MODELS + P1_MODELS + P2_MODELS


# ─── Tool Definitions ──────────────────────────────────────────────

def make_tool(name: str, description: str, properties: dict, required: list[str] | None = None) -> dict:
    """Helper to build an OpenAI-style tool definition."""
    if required is None:
        required = list(properties.keys())
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "required": required,
                "properties": properties,
            },
        },
    }


# Single tool for basic tests
TOOL_GET_WEATHER = make_tool(
    name="get_weather",
    description="Get the current weather for a given city",
    properties={
        "city": {"type": "string", "description": "The city name"},
    },
)

# Multi-tool set (3 tools)
TOOL_GET_TEMPERATURE = make_tool(
    name="get_temperature",
    description="Get the current temperature in Celsius for a city",
    properties={
        "city": {"type": "string", "description": "The city name"},
    },
)

TOOL_SEARCH_RESTAURANTS = make_tool(
    name="search_restaurants",
    description="Search for restaurants in a city",
    properties={
        "city": {"type": "string", "description": "The city name"},
        "cuisine": {"type": "string", "description": "Type of cuisine (optional)"},
    },
    required=["city"],
)

TOOL_BOOK_FLIGHT = make_tool(
    name="book_flight",
    description="Book a flight between two cities",
    properties={
        "origin": {"type": "string", "description": "Departure city"},
        "destination": {"type": "string", "description": "Arrival city"},
        "date": {"type": "string", "description": "Travel date in YYYY-MM-DD format"},
    },
)

MULTI_TOOLS = [TOOL_GET_WEATHER, TOOL_SEARCH_RESTAURANTS, TOOL_BOOK_FLIGHT]

# Tools for parallel call testing
TOOL_GET_POPULATION = make_tool(
    name="get_population",
    description="Get the population of a city",
    properties={
        "city": {"type": "string", "description": "The city name"},
    },
)

PARALLEL_TOOLS = [TOOL_GET_WEATHER, TOOL_GET_TEMPERATURE, TOOL_GET_POPULATION]


# ─── Scaling Test Tools ─────────────────────────────────────────────

def generate_dummy_tools(count: int) -> list[dict]:
    """Generate N unique tool definitions for scaling tests.

    Always includes get_weather as the first tool (the target tool).
    Remaining tools are dummy tools that shouldn't be selected.
    """
    tools = [TOOL_GET_WEATHER]

    dummy_actions = [
        ("calculate_tax", "Calculate tax for a given amount", {"amount": {"type": "number", "description": "The amount"}, "rate": {"type": "number", "description": "Tax rate"}}),
        ("translate_text", "Translate text to another language", {"text": {"type": "string", "description": "Text to translate"}, "language": {"type": "string", "description": "Target language"}}),
        ("send_email", "Send an email", {"to": {"type": "string", "description": "Recipient"}, "subject": {"type": "string", "description": "Subject"}, "body": {"type": "string", "description": "Email body"}}),
        ("create_reminder", "Set a reminder", {"message": {"type": "string", "description": "Reminder text"}, "time": {"type": "string", "description": "When to remind"}}),
        ("search_news", "Search news articles", {"query": {"type": "string", "description": "Search query"}, "category": {"type": "string", "description": "News category"}}),
        ("get_stock_price", "Get current stock price", {"symbol": {"type": "string", "description": "Stock ticker symbol"}}),
        ("convert_currency", "Convert between currencies", {"amount": {"type": "number", "description": "Amount"}, "from_currency": {"type": "string", "description": "From"}, "to_currency": {"type": "string", "description": "To"}}),
        ("get_directions", "Get driving directions", {"origin": {"type": "string", "description": "Start"}, "destination": {"type": "string", "description": "End"}}),
        ("set_alarm", "Set an alarm", {"time": {"type": "string", "description": "Alarm time"}, "label": {"type": "string", "description": "Label"}}),
        ("play_music", "Play a song", {"song": {"type": "string", "description": "Song name"}, "artist": {"type": "string", "description": "Artist"}}),
        ("order_food", "Order food delivery", {"restaurant": {"type": "string", "description": "Restaurant"}, "items": {"type": "string", "description": "Items to order"}}),
        ("check_calendar", "Check calendar events", {"date": {"type": "string", "description": "Date to check"}}),
        ("add_contact", "Add a new contact", {"name": {"type": "string", "description": "Contact name"}, "phone": {"type": "string", "description": "Phone number"}}),
        ("get_recipe", "Get a recipe", {"dish": {"type": "string", "description": "Dish name"}}),
    ]

    for i in range(min(count - 1, len(dummy_actions))):
        name, desc, props = dummy_actions[i]
        tools.append(make_tool(name, desc, props))

    return tools[:count]


# ─── Text-Based Tool Calling Prompts ────────────────────────────────

TEXT_TOOL_SYSTEM_PROMPT = """You have access to the following tools. When you need to use a tool, output your tool call in XML format:

<tool_call>
{"name": "TOOL_NAME", "arguments": {"arg1": "value1"}}
</tool_call>

Available tools:
{tool_descriptions}

Important: Always use the exact XML format shown above for tool calls. Do not use any other format."""


def format_text_tool_descriptions(tools: list[dict]) -> str:
    """Format tool definitions for inclusion in a system prompt."""
    lines: list[str] = []
    for tool in tools:
        func = tool["function"]
        params = func["parameters"]
        props = params.get("properties", {})
        required = params.get("required", [])

        param_strs: list[str] = []
        for pname, pdef in props.items():
            req = " (required)" if pname in required else " (optional)"
            param_strs.append(f"    - {pname}: {pdef.get('type', 'any')} — {pdef.get('description', '')}{req}")

        lines.append(f"- {func['name']}: {func['description']}")
        if param_strs:
            lines.append("  Parameters:")
            lines.extend(param_strs)

    return "\n".join(lines)
