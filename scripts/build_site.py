#!/usr/bin/env python3
"""
build_site.py
--------------
data/categories/*.yml + data/status.json को मिलाकर:
  1. docs/data.json          -> स्टैटिक साइट (docs/index.html) के लिए एक consolidated फाइल
  2. docs/badges/total.json  -> shields.io endpoint badge (कुल APIs)
  3. docs/badges/active.json -> shields.io endpoint badge (Active/reachable APIs)
  4. docs/badges/uptime.json -> shields.io endpoint badge (औसत uptime %)

shields.io endpoint badge फॉर्मेट: https://shields.io/badges/endpoint-badge
इन्हें README में इस्तेमाल किया जा सकता है:
  https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<user>/<repo>/main/docs/badges/total.json
"""

import json
import os
import glob
import yaml
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES_DIR = os.path.join(ROOT, "data", "categories")
STATUS_FILE = os.path.join(ROOT, "data", "status.json")
DOCS_DIR = os.path.join(ROOT, "docs")
BADGES_DIR = os.path.join(DOCS_DIR, "badges")


def load_categories():
    apis = []
    for path in sorted(glob.glob(os.path.join(CATEGORIES_DIR, "*.yml"))):
        with open(path, "r", encoding="utf-8") as f:
            entries = yaml.safe_load(f) or []
        apis.extend(entries)
    return apis


def load_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"apis": {}, "last_updated": None}


def badge_color(pct):
    if pct is None:
        return "lightgrey"
    if pct >= 90:
        return "brightgreen"
    if pct >= 70:
        return "yellow"
    return "red"


def main():
    os.makedirs(BADGES_DIR, exist_ok=True)

    apis = load_categories()
    status = load_status()
    status_map = status.get("apis", {})

    merged = []
    reachable_count = 0
    uptime_values = []

    for e in apis:
        rec = status_map.get(e["name"], {})
        skip = bool(e.get("skip_health_check"))
        state = "skipped" if skip else rec.get("state", "unknown")
        uptime_pct = None if skip else rec.get("uptime_pct")

        if state in ("active", "key_required"):
            reachable_count += 1
        if uptime_pct is not None:
            uptime_values.append(uptime_pct)

        merged.append(
            {
                "name": e["name"],
                "description": e["description"],
                "url": e["url"],
                "test_endpoint": e.get("test_endpoint"),
                "category": e.get("category", "Uncategorized"),
                "auth": e.get("auth", "-"),
                "https": bool(e.get("https")),
                "cors": bool(e.get("cors")),
                "rate_limit": e.get("rate_limit", "-"),
                "note": e.get("note"),
                "skip_health_check": skip,
                "state": state,
                "uptime_pct": uptime_pct,
                "latency_ms": rec.get("latency_ms"),
            }
        )

    site_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "last_health_check": status.get("last_updated"),
        "total": len(merged),
        "reachable": reachable_count,
        "apis": merged,
    }

    with open(os.path.join(DOCS_DIR, "data.json"), "w", encoding="utf-8") as f:
        json.dump(site_data, f, ensure_ascii=False, indent=2)

    avg_uptime = round(sum(uptime_values) / len(uptime_values), 1) if uptime_values else None

    badges = {
        "total.json": {
            "schemaVersion": 1,
            "label": "APIs",
            "message": str(len(merged)),
            "color": "blue",
        },
        "active.json": {
            "schemaVersion": 1,
            "label": "reachable",
            "message": f"{reachable_count}/{len(merged)}",
            "color": badge_color(100 * reachable_count / len(merged) if merged else None),
        },
        "uptime.json": {
            "schemaVersion": 1,
            "label": "avg uptime",
            "message": f"{avg_uptime}%" if avg_uptime is not None else "n/a",
            "color": badge_color(avg_uptime),
        },
    }

    for filename, payload in badges.items():
        with open(os.path.join(BADGES_DIR, filename), "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"✅ docs/data.json और badges बन गए ({len(merged)} APIs, {reachable_count} reachable)")


if __name__ == "__main__":
    main()
