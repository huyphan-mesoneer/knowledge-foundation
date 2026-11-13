#!/usr/bin/env python3
"""Validate the vault against _system/schema.json.

Checks: frontmatter present, required keys, known type, allowed status, ISO dates,
note in the expected folder, broken [[wikilinks]], stale inbox items, orphan
knowledge notes (no link to a hub).

Usage: python3 _system/scripts/lint.py [--json] [--strict]
Exit code 1 if any error (or any warning with --strict).
"""
import argparse
import datetime as dt
import json
import re
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from vaultlib import ROOT, load_schema, parse_frontmatter  # noqa: E402

SKIP_DIRS = {".git", ".obsidian", ".trash", ".claude", ".github", "node_modules", "__pycache__"}
NO_LINK_CHECK = ("_system/templates/",)
NO_FOLDER_CHECK = ("90-archive/", "_private/")
NEEDS_HUB = {"note", "howto", "reference", "runbook", "prd", "story", "spec", "decision", "incident", "debug-log", "meeting"}
HUB_TYPES = {"project", "area", "moc"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK = re.compile(r"!?\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    schema = load_schema()
    types = schema["types"]
    issues = []

    def add(level, path, msg):
        issues.append({"level": level, "path": path, "message": msg})

    files = [p for p in ROOT.rglob("*") if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]
    names = set()
    for p in files:
        rel = p.relative_to(ROOT).as_posix()
        names.add(p.name.lower())
        names.add(rel.lower())
        if p.suffix == ".md":
            names.add(p.stem.lower())
            names.add(rel[:-3].lower())

    notes, aliases = {}, set()
    for p in files:
        if p.suffix != ".md":
            continue
        rel = p.relative_to(ROOT).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        notes[rel] = (fm, body, text)
        if fm and isinstance(fm.get("aliases"), list):
            aliases.update(x.lower() for x in fm["aliases"])
    names |= aliases
    hubs = {rel.rsplit("/", 1)[-1][:-3].lower() for rel, (fm, _, _) in notes.items() if fm and fm.get("type") in HUB_TYPES}

    today = dt.date.today()
    for rel, (fm, body, text) in sorted(notes.items()):
        in_typed_folder = re.match(r"^\d\d-", rel) and not rel.startswith("90-archive/")
        if rel.startswith("_system/templates/"):
            continue

        # links
        links = [m.group(1).strip() for m in WIKILINK.finditer(strip_code(text))]
        for target in links:
            t = target.lower()
            if t not in names and t + ".md" not in names:
                add("error", rel, f"broken link [[{target}]]")

        if not in_typed_folder:
            continue
        if fm is None:
            add("error", rel, "missing YAML frontmatter")
            continue
        for key in schema["required"]:
            if not fm.get(key):
                add("error", rel, f"missing required '{key}'")
        t = fm.get("type")
        if t and t not in types:
            add("error", rel, f"unknown type '{t}'")
            continue
        if not t:
            continue
        spec = types[t]
        for key in spec.get("required", []):
            if not fm.get(key):
                add("error", rel, f"missing '{key}' (required for type {t})")
        if spec.get("status") and fm.get("status") and fm["status"] not in spec["status"]:
            add("error", rel, f"status '{fm['status']}' not in {spec['status']}")
        for key in ("created", "updated"):
            if fm.get(key) and not DATE.match(str(fm[key])):
                add("error", rel, f"'{key}' must be YYYY-MM-DD")
        # folder
        if not rel.startswith(NO_FOLDER_CHECK):
            prefix = "20-projects/" if spec.get("project_bound") else spec["folder"].split("{{")[0]
            ok = rel.startswith(prefix.rstrip("/") + "/") or (spec.get("project_bound") and rel.startswith("00-inbox/"))
            if not ok:
                add("warning", rel, f"type '{t}' belongs in {spec['folder']}/")
        # inbox age
        if t == "inbox" and fm.get("created") and DATE.match(fm["created"]):
            age = (today - dt.date.fromisoformat(fm["created"])).days
            if age > schema.get("inbox_max_age_days", 7):
                add("warning", rel, f"inbox item is {age} days old — process it")
        # orphan
        if t in NEEDS_HUB:
            if not ({l.lower().rsplit("/", 1)[-1] for l in links} & hubs) and not rel.startswith("20-projects/"):
                add("warning", rel, "not linked to any project/area/MOC (add to 'related')")

    errors = sum(i["level"] == "error" for i in issues)
    warnings = len(issues) - errors
    if a.json:
        print(json.dumps({"errors": errors, "warnings": warnings, "notes": len(notes), "issues": issues}, indent=2))
    else:
        for i in issues:
            print(f"{i['level'].upper():7} {i['path']}: {i['message']}")
        print(f"\n{len(notes)} notes · {errors} errors · {warnings} warnings")
    sys.exit(1 if errors or (a.strict and warnings) else 0)


if __name__ == "__main__":
    main()
