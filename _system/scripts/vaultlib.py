"""Shared helpers for vault scripts. Python 3.8+, standard library only."""
import datetime as _dt
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SYSTEM = ROOT / "_system"
TEMPLATES = SYSTEM / "templates"
FORBIDDEN = re.compile(r'[\\/:*?"<>|#^\[\]]')

# Moment.js tokens used by Obsidian's core Templates plugin -> strftime
_TOKENS = [("YYYY", "%Y"), ("GGGG", "%G"), ("MMMM", "%B"), ("MM", "%m"),
           ("dddd", "%A"), ("DD", "%d"), ("WW", "%V"), ("HH", "%H"), ("mm", "%M")]


def load_schema():
    return json.loads((SYSTEM / "schema.json").read_text(encoding="utf-8"))


def moment(fmt, dt):
    out, i = "", 0
    while i < len(fmt):
        if fmt[i] == "[":
            j = fmt.index("]", i)
            out += fmt[i + 1:j]
            i = j + 1
            continue
        for tok, py in _TOKENS:
            if fmt.startswith(tok, i):
                out += dt.strftime(py)
                i += len(tok)
                break
        else:
            out += fmt[i]
            i += 1
    return out


def render(text, dt, **vars_):
    """Replace Obsidian core-template variables plus our own ({{project}})."""
    def sub(m):
        name, fmt = m.group(1), m.group(2)
        if name == "date":
            return moment(fmt or "YYYY-MM-DD", dt)
        if name == "time":
            return moment(fmt or "HH:mm", dt)
        return str(vars_.get(name, m.group(0)))
    return re.sub(r"\{\{\s*(\w+)(?::([^}]*))?\s*\}\}", sub, text)


def safe_name(name):
    return re.sub(r"\s+", " ", FORBIDDEN.sub("-", name)).strip(" .-")


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser for this vault's flat schema.
    Returns (dict, body) or (None, text) when there is no frontmatter."""
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return None, text
    data, key = {}, None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = [v.strip().strip("'\"") for v in _split_list(inner)] if inner else []
            elif val == "":
                data[key] = ""
            else:
                data[key] = val.strip("'\"")
        elif key and re.match(r"^\s*-\s+", line):
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(re.sub(r"^\s*-\s+", "", line).strip().strip("'\""))
    return data, "\n".join(lines[end + 1:])


def _split_list(s):
    parts, depth, cur, quote = [], 0, "", None
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "'\"":
            quote = ch
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
            continue
        cur += ch
    if cur.strip():
        parts.append(cur)
    return parts


def set_frontmatter_value(text, key, value):
    """Set `key: value` inside existing frontmatter (adds it if missing)."""
    lines = text.split("\n")
    end = lines[1:].index("---") + 1
    for i in range(1, end):
        if re.match(rf"^{re.escape(key)}:", lines[i]):
            lines[i] = f"{key}: {value}"
            return "\n".join(lines)
    lines.insert(end, f"{key}: {value}")
    return "\n".join(lines)


def today():
    return _dt.datetime.now()
