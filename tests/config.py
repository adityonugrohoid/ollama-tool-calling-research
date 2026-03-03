"""Shared test configuration: model lists, tool definitions, default options."""

from dataclasses import dataclass

# Reproducible test options
DEFAULT_OPTIONS: dict = {
    "temperature": 0,
    "seed": 42,
    "num_ctx": 4096,
}


# ─── Flag Matrix ───────────────────────────────────────────────────

@dataclass(frozen=True)
class FlagCombo:
    """A combination of stream and think flags for a test run."""
    stream: bool
    think: bool
    label: str  # "S0T0", "S0T1", "S1T0", "S1T1"


ALL_FLAG_COMBOS: list[FlagCombo] = [
    FlagCombo(stream=False, think=False, label="S0T0"),
    FlagCombo(stream=False, think=True, label="S0T1"),
    FlagCombo(stream=True, think=False, label="S1T0"),
    FlagCombo(stream=True, think=True, label="S1T1"),
]

# Model groups (based on flag matrix sweep + rerun results)
# Source: observations/summaries/model_groups.md
# Total: 32 models — grouped by native/text layer pass patterns

# Group A: All P (60/60) — native 40/40 P, text 20/20 P
GA_MODELS: list[str] = [
    "ministral-3:3b",        #  3B, tools+vision — Mistral
    "ministral-3:8b",        #  8B, tools+vision — Mistral
    "ministral-3:14b",       # 14B, tools+vision — Mistral
    "devstral-2:123b",       # 123B, tools — Mistral coding model
    "gemini-3-flash-preview", # unknown, tools+thinking — Google
    "cogito-2.1:671b",       # 671B, tools+thinking
    "kimi-k2.5",             # 1T, tools+thinking+vision
    "kimi-k2-thinking",      # 1T, tools+thinking
    "minimax-m2",            # 230B, tools — migrated from B after rerun
    "kimi-k2:1t",            # 1T, tools — migrated from B after rerun
]

# Group B: All native P (40/40), text varies — native perfect, text has confirmed F
GB_MODELS: list[str] = [
    "minimax-m2.1",          # 230B, tools+thinking — vt_zero PFFF
    "minimax-m2.5",          # 230B, tools+thinking — vt_zero FFPF
    "glm-4.6",              # 357B, tools+thinking — text 9/20
    "nemotron-3-nano:30b",   # 30B, tools+thinking — text 7/20
    "glm-5",                 # 756B, tools+thinking — text 3/20
    "glm-4.7",              # 357B, tools+thinking — text 2/20
    "qwen3-coder-next",      # 80B, tools — text 0/20 (confirmed F after rerun)
    "qwen3-coder:480b",      # 480B, tools — text 0/20 (confirmed F after rerun)
]

# Group C: All text P (20/20), native varies — text perfect, native has confirmed F
GC_MODELS: list[str] = [
    "qwen3-vl:235b-instruct",# 235B, tools+vision — native 37/40
    "devstral-small-2:24b",  # 24B, tools+vision — native 36/40 (v_int FFFF)
    "mistral-large-3:675b",  # 675B, tools+vision — native 36/40 (v_int FFFF)
    "gpt-oss:120b",          # 120B, tools+thinking — native 32/40
    "qwen3-vl:235b",         # 235B, tools+thinking+vision — native 0/40 (server blocked, confirmed F)
    "gemma3:4b",             #  4B, vision only — NO tools, native 0/40
    "gemma3:12b",            # 12B, vision only — NO tools, native 0/40
    "gemma3:27b",            # 27B, vision only — NO tools, native 0/40
]

# Group D: Remaining — both layers have confirmed F
GD_MODELS: list[str] = [
    "qwen3-next:80b",        # 80B, tools+thinking — native 35/40, text 19/20
    "rnj-1:8b",              #  8B, tools — native 36/40 (v_zero FFFF confirmed), text 16/20
    "qwen3.5:397b",          # 397B, tools+thinking+vision — native 39/40, text 17/20 (worse on rerun)
    "gpt-oss:20b",           # 20B, tools+thinking — native 29/40, text 15/20
    "deepseek-v3.1:671b",    # 671B, tools+thinking — native 25/40 (think=true breaks), text 19/20
    "deepseek-v3.2",         # 671B, tools+thinking — native 0/40, text 5/20
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

ALL_MODELS: list[str] = GA_MODELS + GB_MODELS + GC_MODELS + GD_MODELS


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


# ─── Voxel Arena Tools ───────────────────────────────────────────────

BLOCK_TYPES: list[str] = [
    "stone", "dirt", "grass", "wood", "sand", "water",
    "glass", "brick", "iron", "gold", "diamond", "obsidian",
]

TOOL_PLACE_BLOCK = make_tool(
    name="placeBlock",
    description="Place a block at the specified position in the voxel world",
    properties={
        "x": {"type": "integer", "description": "X coordinate (0-15)", "minimum": 0, "maximum": 15},
        "y": {"type": "integer", "description": "Y coordinate (0-15)", "minimum": 0, "maximum": 15},
        "z": {"type": "integer", "description": "Z coordinate (0-15)", "minimum": 0, "maximum": 15},
        "type": {"type": "string", "description": "Block type to place", "enum": BLOCK_TYPES},
    },
)

TOOL_REMOVE_BLOCK = make_tool(
    name="removeBlock",
    description="Remove the block at the specified position in the voxel world",
    properties={
        "x": {"type": "integer", "description": "X coordinate (0-15)", "minimum": 0, "maximum": 15},
        "y": {"type": "integer", "description": "Y coordinate (0-15)", "minimum": 0, "maximum": 15},
        "z": {"type": "integer", "description": "Z coordinate (0-15)", "minimum": 0, "maximum": 15},
    },
)

TOOL_GET_WORLD_STATE = make_tool(
    name="getWorldState",
    description="Get the current state of the voxel world",
    properties={},
    required=[],
)

TOOL_DONE = make_tool(
    name="done",
    description="Signal that the task is complete with a summary description",
    properties={
        "description": {"type": "string", "description": "Summary of what was accomplished"},
    },
)

VOXEL_TOOLS = [TOOL_PLACE_BLOCK, TOOL_REMOVE_BLOCK, TOOL_GET_WORLD_STATE, TOOL_DONE]


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

_TEXT_TOOL_SYSTEM_TEMPLATE = """You have access to the following tools. When you need to use a tool, output your tool call in XML format:

<tool_call>
{"name": "TOOL_NAME", "arguments": {"arg1": "value1"}}
</tool_call>

Available tools:
$TOOL_DESCRIPTIONS

Important: Always use the exact XML format shown above for tool calls. Do not use any other format."""


def build_text_tool_system_prompt(tools: list[dict]) -> str:
    """Build the system prompt for text-based tool calling."""
    descriptions = format_text_tool_descriptions(tools)
    return _TEXT_TOOL_SYSTEM_TEMPLATE.replace("$TOOL_DESCRIPTIONS", descriptions)


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
            constraints: list[str] = []
            if "enum" in pdef:
                constraints.append(f"values: {pdef['enum']}")
            if "minimum" in pdef:
                constraints.append(f"min: {pdef['minimum']}")
            if "maximum" in pdef:
                constraints.append(f"max: {pdef['maximum']}")
            constraint_str = f" [{', '.join(constraints)}]" if constraints else ""
            param_strs.append(f"    - {pname}: {pdef.get('type', 'any')} — {pdef.get('description', '')}{constraint_str}{req}")

        lines.append(f"- {func['name']}: {func['description']}")
        if param_strs:
            lines.append("  Parameters:")
            lines.extend(param_strs)

    return "\n".join(lines)
