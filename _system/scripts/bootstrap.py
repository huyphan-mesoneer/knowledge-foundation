#!/usr/bin/env python3
"""Set up a fresh copy of this template for a person or a team.

Usage:
  python3 _system/scripts/bootstrap.py --owner "Jane Doe" --roles product,engineering [--mode personal|team]

Idempotent: re-running adds new roles' areas and never overwrites existing notes.
"""
import argparse
import datetime as dt
import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from vaultlib import ROOT, SYSTEM, load_schema  # noqa: E402
from new_note import create  # noqa: E402


def main():
    schema = load_schema()
    roles_known = [r for r in schema["roles"] if r != "everyone"]
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--owner", required=True, help="person or team name")
    ap.add_argument("--roles", default="", help=f"comma-separated: {', '.join(roles_known)}")
    ap.add_argument("--mode", choices=["personal", "team"], default="personal")
    a = ap.parse_args()

    roles = [r.strip().lower() for r in a.roles.split(",") if r.strip()]
    unknown = [r for r in roles if r not in schema["roles"]]
    if unknown:
        raise SystemExit(f"Unknown role(s): {unknown}. Known: {roles_known} (add more in _system/schema.json)")

    cfg_path = SYSTEM / "vault.json"
    cfg = json.loads(cfg_path.read_text()) if cfg_path.exists() else {"created": dt.date.today().isoformat()}
    cfg.update({"owner": a.owner, "mode": a.mode,
                "roles": sorted(set(cfg.get("roles", [])) | set(roles))})
    cfg_path.write_text(json.dumps(cfg, indent=2) + "\n")

    made = []
    for role in ["everyone"] + roles:
        for area in schema["roles"][role]["areas"]:
            path, new = create("area", area, quiet=True)
            if new:
                text = path.read_text().replace("roles: []", f"roles: [{role}]")
                path.write_text(text)
                made.append(path.relative_to(ROOT).as_posix())
    path, new = create("daily", quiet=True)
    if new:
        made.append(path.relative_to(ROOT).as_posix())

    if a.mode == "team":
        gi = ROOT / ".gitignore"
        content = gi.read_text() if gi.exists() else ""
        if "10-journal/" not in content:
            gi.write_text(content.rstrip("\n") + "\n\n# team mode: journals stay on each person's machine\n10-journal/*/*.md\n")

    templates = sorted({t for r in ["everyone"] + roles for t in schema["roles"][r]["templates"]})
    print(f"Vault ready for {a.owner} ({a.mode}); roles: {', '.join(cfg['roles']) or 'none'}")
    for m in made:
        print(f"  + {m}")
    print(f"Suggested templates: {', '.join('tpl-' + t for t in templates)}")
    print("Next: open this folder as a vault in Obsidian and start at Home.")


if __name__ == "__main__":
    main()
