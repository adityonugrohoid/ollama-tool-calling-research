"""Generate expanded sub-check tables from sweep results.

Reads p0/p1/p2 v3_flagmatrix.md files and outputs markdown tables
where voxel tests show all 5 sub-check P/F/T values instead of a single P/F.

Values: P=pass, F=fail (model error), T=transient (server 500/503/-1 error)

Table format per flag combo:
| Model | single | multi | parallel | step | scale | voxel (5 sub) | voxel_text (5 sub) | Total |

Sub-checks: sel=tool_selection, enum=enum_adherence, int=integer_constraints,
            zero=zero_param_tool, disc=tool_discrimination
"""

import re
import sys
from pathlib import Path

SUMMARY_DIR = Path(__file__).parent.parent / "observations" / "summaries"

SINGLE_TESTS = ["single_tool", "multi_tool", "parallel_calls", "multi_step", "tool_count_scaling"]
VOXEL_TESTS = ["voxel_tools", "voxel_tools_text"]
SUB_CHECK_ORDER = ["tool_selection", "enum_adherence", "integer_constraints", "zero_param_tool", "tool_discrimination"]
SUB_CHECK_SHORT = ["sel", "enum", "int", "zero", "disc"]
FLAG_ORDER = ["S0T0", "S0T1", "S1T0", "S1T1"]


def _is_transient_error(notes: str) -> bool:
    """Check if failure notes indicate a transient server error."""
    transient_patterns = [
        "Exception: ResponseError",
        "status code: 500",
        "status code: 503",
        "status code: -1",
    ]
    return any(p in notes for p in transient_patterns)


def _sub_check_is_transient(details_str: str, sc_name: str) -> bool:
    """Check if a specific sub-check failed due to a transient server error."""
    # Find the sub-check's notes in the details string
    sc_pattern = re.compile(
        rf"'{sc_name}':\s*\{{\s*'passed':\s*False,\s*'notes':\s*'(.*?)'\}}"
    )
    sc_match = sc_pattern.search(details_str)
    if sc_match:
        return _is_transient_error(sc_match.group(1))
    return False


def parse_report(filepath: Path) -> dict:
    """Parse a v3_flagmatrix report into structured data.

    Returns: {(model, test, flag): {
        "result": "P" | "F" | "T",
        "sub_checks": {name: "P" | "F" | "T"} or None
    }}
    """
    text = filepath.read_text()
    results: dict = {}

    # Parse each detailed result section
    pattern = re.compile(
        r"### (.+?) / (.+?) \[(.+?)\] — (PASS|FAIL)\n"
        r"(.*?)(?=\n### |\Z)",
        re.DOTALL,
    )

    for match in pattern.finditer(text):
        model = match.group(1).strip()
        test = match.group(2).strip()
        flag = match.group(3).strip()
        passed = match.group(4) == "PASS"
        body = match.group(5)

        # Extract notes line
        notes_match = re.search(r"- Notes: (.+)", body)
        notes = notes_match.group(1) if notes_match else ""

        # Determine single-test result: P, F, or T
        if passed:
            result = "P"
        elif _is_transient_error(body):
            result = "T"
        else:
            result = "F"

        entry: dict = {"result": result, "sub_checks": None}

        # Extract sub-check results for voxel tests
        if test in VOXEL_TESTS:
            sub_checks: dict[str, str] = {}
            details_match = re.search(r"- Details: ({.*})", body)
            if details_match:
                details_str = details_match.group(1)
                for sc_name in SUB_CHECK_ORDER:
                    sc_pattern_re = re.compile(
                        rf"'{sc_name}':\s*\{{\s*'passed':\s*(True|False)"
                    )
                    sc_match = sc_pattern_re.search(details_str)
                    if sc_match:
                        if sc_match.group(1) == "True":
                            sub_checks[sc_name] = "P"
                        elif _sub_check_is_transient(details_str, sc_name):
                            sub_checks[sc_name] = "T"
                        else:
                            sub_checks[sc_name] = "F"
                    else:
                        sub_checks[sc_name] = "F"
            else:
                # Top-level exception — check if transient
                if _is_transient_error(body):
                    for sc_name in SUB_CHECK_ORDER:
                        sub_checks[sc_name] = "T"
                else:
                    for sc_name in SUB_CHECK_ORDER:
                        sub_checks[sc_name] = "F"
            entry["sub_checks"] = sub_checks

        results[(model, test, flag)] = entry

    return results


def extract_models(results: dict) -> list[str]:
    """Get ordered list of models from results."""
    seen: dict[str, None] = {}
    for model, _, _ in results:
        if model not in seen:
            seen[model] = None
    return list(seen.keys())


def generate_table(results: dict, models: list[str], flag: str) -> list[str]:
    """Generate markdown table for a single flag combo."""
    lines: list[str] = []

    # Header
    lines.append(
        f"| Model | single | multi | parallel | step | scale "
        f"| voxel ({'/'.join(SUB_CHECK_SHORT)}) "
        f"| voxel_text ({'/'.join(SUB_CHECK_SHORT)}) "
        f"| Total |"
    )
    lines.append("|-------|--------|-------|----------|------|-------|" + "------|" * 3)

    for model in models:
        row_parts: list[str] = [model]
        total_pass = 0
        total_transient = 0
        total_checks = 0

        # Single-check tests
        for test in SINGLE_TESTS:
            key = (model, test, flag)
            if key in results:
                r = results[key]["result"]
                row_parts.append(r)
                if r == "P":
                    total_pass += 1
                elif r == "T":
                    total_transient += 1
                total_checks += 1
            else:
                row_parts.append("-")
                total_checks += 1

        # Voxel tests with sub-checks
        for test in VOXEL_TESTS:
            key = (model, test, flag)
            if key in results and results[key]["sub_checks"]:
                sc = results[key]["sub_checks"]
                sc_str = ""
                for sc_name in SUB_CHECK_ORDER:
                    r = sc.get(sc_name, "F")
                    sc_str += r
                    if r == "P":
                        total_pass += 1
                    elif r == "T":
                        total_transient += 1
                    total_checks += 1
                row_parts.append(sc_str)
            else:
                row_parts.append("-----")
                total_checks += 5

        total_str = f"{total_pass}/{total_checks}"
        if total_transient > 0:
            total_str += f" ({total_transient}T)"
        row_parts.append(total_str)
        lines.append("| " + " | ".join(row_parts) + " |")

    return lines


def generate_cumulative_table(results: dict, models: list[str]) -> list[str]:
    """Generate cumulative table across all 4 flag combos.

    Single checks show PPPP (4 flags), voxel sub-checks show PPPP per sub-check.
    Total shows X/60.
    """
    lines: list[str] = []

    lines.append(
        f"| Model | single | multi | parallel | step | scale "
        f"| v_sel | v_enum | v_int | v_zero | v_disc "
        f"| vt_sel | vt_enum | vt_int | vt_zero | vt_disc "
        f"| Total |"
    )
    lines.append("|-------|" + "------|" * 16)

    for model in models:
        row_parts: list[str] = [model]
        total_pass = 0
        total_transient = 0
        total_checks = 0

        # Single-check tests: PPPP across 4 flags
        for test in SINGLE_TESTS:
            combo_str = ""
            for flag in FLAG_ORDER:
                key = (model, test, flag)
                if key in results:
                    r = results[key]["result"]
                    combo_str += r
                    if r == "P":
                        total_pass += 1
                    elif r == "T":
                        total_transient += 1
                else:
                    combo_str += "-"
                total_checks += 1
            row_parts.append(combo_str)

        # Voxel sub-checks: PPPP per sub-check across 4 flags
        for test in VOXEL_TESTS:
            for sc_name in SUB_CHECK_ORDER:
                combo_str = ""
                for flag in FLAG_ORDER:
                    key = (model, test, flag)
                    if key in results and results[key]["sub_checks"]:
                        r = results[key]["sub_checks"].get(sc_name, "F")
                        combo_str += r
                        if r == "P":
                            total_pass += 1
                        elif r == "T":
                            total_transient += 1
                    else:
                        combo_str += "-"
                    total_checks += 1
                row_parts.append(combo_str)

        total_str = f"{total_pass}/{total_checks}"
        if total_transient > 0:
            total_str += f" ({total_transient}T)"
        row_parts.append(total_str)
        lines.append("| " + " | ".join(row_parts) + " |")

    return lines


def process_sweep(name: str, filepath: Path) -> str:
    """Process one sweep file and return full markdown output."""
    results = parse_report(filepath)
    models = extract_models(results)

    output_lines: list[str] = []
    output_lines.append(f"# {name} — Expanded Sub-check Results\n")

    # Per-flag tables
    for flag in FLAG_ORDER:
        flag_desc = {
            "S0T0": "stream=False, think=False",
            "S0T1": "stream=False, think=True",
            "S1T0": "stream=True, think=False",
            "S1T1": "stream=True, think=True",
        }[flag]
        output_lines.append(f"## {flag} ({flag_desc})\n")
        table = generate_table(results, models, flag)
        output_lines.extend(table)
        output_lines.append("")

    # Cumulative table
    output_lines.append("## Cumulative (all flag combos)\n")
    output_lines.append("Each cell = 4 chars for S0T0/S0T1/S1T0/S1T1. Total out of 60.\n")
    table = generate_cumulative_table(results, models)
    output_lines.extend(table)
    output_lines.append("")

    return "\n".join(output_lines)


def main() -> None:
    sweeps = [
        ("GA", SUMMARY_DIR / "ga_v4_flagmatrix.md"),
        ("GB", SUMMARY_DIR / "gb_v4_flagmatrix.md"),
        ("GC", SUMMARY_DIR / "gc_v4_flagmatrix.md"),
        ("GD", SUMMARY_DIR / "gd_v4_flagmatrix.md"),
    ]

    output_path = SUMMARY_DIR / "gagbgcgd_subcheck_tables.md"
    sections: list[str] = []

    for name, filepath in sweeps:
        if not filepath.exists():
            print(f"Skipping {name}: {filepath} not found")
            continue
        print(f"Processing {name}...")
        sections.append(process_sweep(name, filepath))

    full_output = "\n---\n\n".join(sections)
    output_path.write_text(full_output)
    print(f"\nSaved to {output_path}")

    # Also print to stdout
    print("\n" + full_output)


if __name__ == "__main__":
    main()
