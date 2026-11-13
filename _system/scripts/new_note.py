#!/usr/bin/env python3
"""Create a note from a template in the right folder with the right name.

Usage:
  python3 _system/scripts/new_note.py <type> ["Title"] [--project NAME] [--author agent:NAME]
                                       [--date YYYY-MM-DD] [--related "[[X]]" ...]
  python3 _system/scripts/new_note.py --list          # show available types

Prints the vault-relative path. If the note already exists it is left untouched
and the path is printed with status "exists" (safe to call repeatedly).
"""
import argparse
import datetime as dt
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from vaultlib import ROOT, TEMPLATES, load_schema, render, safe_name, set_frontmatter_value  # noqa: E402


def create(note_type, title="", project="", author="", date=None, related=None, quiet=False):
    schema = load_schema()
    types = schema["types"]
    if note_type not in types:
        raise SystemExit(f"Unknown type '{note_type}'. Known: {', '.join(types)}")
    spec = types[note_type]
    when = dt.datetime.combine(date, dt.datetime.now().time()) if date else dt.datetime.now()
    title = safe_name(title)
    project = safe_name(project)
    if "{{title}}" in spec["filename"] + spec["folder"] and not title:
        raise SystemExit(f"Type '{note_type}' needs a title.")

    folder_tpl = spec["folder"]
    if spec.get("project_bound"):
        if project:
            if not (ROOT / "20-projects" / project).is_dir():
                raise SystemExit(f"Project folder 20-projects/{project} not found. Create it first: new_note.py project \"{project}\"")
        else:
            print(f"warning: no --project given; '{note_type}' goes to 00-inbox for now", file=sys.stderr)
            folder_tpl = "00-inbox"

    stem = render(spec["filename"], when, title=title, project=project).strip()
    folder = ROOT / render(folder_tpl, when, title=title, project=project)
    path = folder / f"{stem}.md"
    rel = path.relative_to(ROOT).as_posix()
    if path.exists():
        if not quiet:
            print(f"exists\t{rel}")
        return path, False

    tpl = TEMPLATES / f"{spec['template']}.md"
    text = render(tpl.read_text(encoding="utf-8"), when, title=stem, project=project)
    if author:
        text = set_frontmatter_value(text, "author", author)
    links = list(related or [])
    if project and note_type != "project":
        links.insert(0, f"[[{project}]]")
        if "\nproject:" in text.split("\n---", 1)[0] + "\n":
            text = set_frontmatter_value(text, "project", f'"[[{project}]]"')
    if links:
        text = set_frontmatter_value(text, "related", "[" + ", ".join(f'"{l}"' for l in links) + "]")

    folder.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if not quiet:
        print(f"created\t{rel}")
    return path, True


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("type", nargs="?")
    p.add_argument("title", nargs="?", default="")
    p.add_argument("--project", default="")
    p.add_argument("--author", default="", help="e.g. agent:claude (default keeps template's 'human')")
    p.add_argument("--date", type=lambda s: dt.date.fromisoformat(s))
    p.add_argument("--related", nargs="*", default=[], help='extra links, e.g. "[[Payments]]"')
    p.add_argument("--list", action="store_true")
    a = p.parse_args()
    if a.list or not a.type:
        for name, spec in load_schema()["types"].items():
            print(f"{name:10} {spec['folder']:28} {spec.get('purpose', '')}")
        return
    create(a.type, a.title, a.project, a.author, a.date, a.related)


if __name__ == "__main__":
    main()
