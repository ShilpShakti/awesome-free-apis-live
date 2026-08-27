#!/usr/bin/env python3
"""
validate_pr.py
---------------
PR में बदले गए data/categories/*.yml फाइलों को पढ़ता है, हर एंट्री के
test_endpoint को टेस्ट करता है, और नतीजा GITHUB_STEP_SUMMARY + एक
markdown फाइल (pr_result.md) में लिख देता है ताकि वर्कफ़्लो उसे PR पर
कमेंट कर सके। अगर कोई एंडपॉइंट 200 नहीं देता, तो exit code 1 के साथ फेल
होता है जिससे PR ऑटोमेटिकली ब्लॉक/फ्लैग हो जाता है।
"""

import glob
import os
import subprocess
import sys

import requests
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES_DIR = os.path.join(ROOT, "data", "categories")
TIMEOUT_SECONDS = 10


def changed_yml_files():
    """main branch से डिफ करके सिर्फ बदली/नई yml फाइलें निकालता है।"""
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "origin/main...HEAD"], text=True
        )
    except subprocess.CalledProcessError:
        out = ""
    files = [
        line
        for line in out.splitlines()
        if line.startswith("data/categories/") and line.endswith(".yml")
    ]
    # अगर diff न मिले (जैसे लोकल टेस्ट), तो सभी फाइलें चेक कर लो
    if not files:
        files = [
            os.path.relpath(p, ROOT)
            for p in glob.glob(os.path.join(CATEGORIES_DIR, "*.yml"))
        ]
    return files


def validate_entry(entry):
    required = ["name", "description", "url", "test_endpoint", "category"]
    missing = [f for f in required if not entry.get(f)]
    if missing:
        return False, f"❌ जरूरी फील्ड्स गायब हैं: {', '.join(missing)}"

    try:
        resp = requests.get(
            entry["test_endpoint"],
            timeout=TIMEOUT_SECONDS,
            headers={"User-Agent": "api-directory-pr-validator/1.0"},
        )
        if resp.status_code == 200:
            return True, f"✅ 200 OK ({resp.elapsed.total_seconds():.2f}s)"
        if resp.status_code in (401, 403):
            return True, f"🟡 {resp.status_code} — लगता है Auth चाहिए, डोमेन जिंदा है"
        return False, f"❌ HTTP {resp.status_code}"
    except requests.RequestException as exc:
        return False, f"❌ रिक्वेस्ट फेल: {exc}"


def main():
    files = changed_yml_files()
    all_ok = True
    lines = ["## 🔍 PR Validator नतीजे\n"]

    for path in files:
        full_path = os.path.join(ROOT, path)
        if not os.path.exists(full_path):
            continue  # फाइल डिलीट हुई होगी
        with open(full_path, "r", encoding="utf-8") as f:
            entries = yaml.safe_load(f) or []

        lines.append(f"### `{path}`\n")
        for entry in entries:
            ok, msg = validate_entry(entry)
            all_ok = all_ok and ok
            lines.append(f"- **{entry.get('name', '(no name)')}**: {msg}")
        lines.append("")

    result_md = "\n".join(lines)
    print(result_md)

    with open(os.path.join(ROOT, "pr_result.md"), "w", encoding="utf-8") as f:
        f.write(result_md)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(result_md)

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
