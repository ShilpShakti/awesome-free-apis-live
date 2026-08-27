#!/usr/bin/env python3
"""
build_readme.py
----------------
data/categories/*.yml + data/status.json को मिलाकर README.md बनाता है।
templates/README.template.md में {{GENERATED_CONTENT}} placeholder को
जनरेट की गई Markdown टेबल्स से बदल देता है।

inactive: true वाले APIs को मुख्य टेबल से हटा दिया जाता है और
फाइल के नीचे एक छोटी "Inactive APIs" लिस्ट में डाल दिया जाता है।
"""

import json
import os
import glob
import yaml
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES_DIR = os.path.join(ROOT, "data", "categories")
STATUS_FILE = os.path.join(ROOT, "data", "status.json")
TEMPLATE_FILE = os.path.join(ROOT, "templates", "README.template.md")
OUTPUT_FILE = os.path.join(ROOT, "README.md")

STATE_ICON = {"active": "🟢", "key_required": "🟡", "down": "🔴"}
STATE_LABEL = {
    "active": "Up",
    "key_required": "Key Reqd",
    "down": "Down",
}


def load_categories():
    categories = {}
    for path in sorted(glob.glob(os.path.join(CATEGORIES_DIR, "*.yml"))):
        with open(path, "r", encoding="utf-8") as f:
            entries = yaml.safe_load(f) or []
        for entry in entries:
            cat = entry.get("category", "Uncategorized")
            categories.setdefault(cat, []).append(entry)
    return categories


def load_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"apis": {}}


def bool_icon(v):
    return "✅" if v else "❌"


def render_table(entries, status_map):
    header = (
        "| API नाम | विवरण | ऑथेंटिकेशन | HTTPS | CORS | स्थिति |\n"
        "|---|---|---|---|---|---|\n"
    )
    rows = []
    for e in entries:
        if e.get("skip_health_check"):
            status_cell = "ℹ️ Self-hosted (not checked)"
        else:
            rec = status_map.get(e["name"], {})
            state = rec.get("state", "unknown")
            uptime = rec.get("uptime_pct")
            if state in STATE_ICON:
                status_cell = f"{STATE_ICON[state]} {uptime}% {STATE_LABEL[state]}" if uptime is not None else STATE_ICON[state]
            else:
                status_cell = "⚪ Not checked yet"

        name_cell = f"[{e['name']}]({e['url']})"
        if e.get("note"):
            name_cell += f" ⓘ"

        rows.append(
            f"| {name_cell} | {e['description']} | {e.get('auth', '-')} "
            f"| {bool_icon(e.get('https'))} | {bool_icon(e.get('cors'))} | {status_cell} |"
        )

    notes = [f"- **{e['name']}**: {e['note']}" for e in entries if e.get("note")]
    footnote = ""
    if notes:
        footnote = "\n\n<details><summary>ⓘ नोट्स देखें</summary>\n\n" + "\n".join(notes) + "\n\n</details>\n"

    return header + "\n".join(rows) + "\n" + footnote


def render_inactive_list(status_map):
    inactive_names = [name for name, rec in status_map.items() if rec.get("inactive")]
    if not inactive_names:
        return ""
    lines = ["\n## ⚠️ Inactive APIs (लगातार 7+ रन से डाउन)\n"]
    for name in sorted(inactive_names):
        lines.append(f"- {name}")
    return "\n".join(lines) + "\n"


def main():
    categories = load_categories()
    status = load_status()
    status_map = status.get("apis", {})

    sections = []
    for cat_name, entries in sorted(categories.items()):
        # inactive APIs को मुख्य टेबल से हटाना
        visible = [e for e in entries if not status_map.get(e["name"], {}).get("inactive")]
        if not visible:
            continue
        sections.append(f"### {cat_name}\n\n" + render_table(visible, status_map))

    generated_content = "\n".join(sections)
    generated_content += render_inactive_list(status_map)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    last_updated = status.get("last_updated") or datetime.now(timezone.utc).isoformat()
    total_apis = sum(len(v) for v in categories.values())
    active_apis = sum(1 for r in status_map.values() if r.get("state") in ("active", "key_required"))

    output = (
        template.replace("{{GENERATED_CONTENT}}", generated_content)
        .replace("{{LAST_UPDATED}}", last_updated)
        .replace("{{TOTAL_APIS}}", str(total_apis))
        .replace("{{ACTIVE_APIS}}", str(active_apis))
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ README.md बन गया ({total_apis} APIs, {active_apis} active/reachable)")


if __name__ == "__main__":
    main()
