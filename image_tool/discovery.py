from pathlib import Path
from .config import INPUT_EXTENSIONS

def discover_inputs(paths, recursive=False):
    found = []
    seen = set()
    for raw in paths:
        p = Path(raw).expanduser()
        if p.is_file():
            candidates = [p]
        elif p.is_dir():
            pattern = "**/*" if recursive else "*"
            candidates = [x for x in p.glob(pattern) if x.is_file()]
        else:
            continue
        for item in candidates:
            if item.suffix.lower() not in INPUT_EXTENSIONS:
                continue
            key = item.resolve()
            if key not in seen:
                seen.add(key)
                found.append(item)
    return sorted(found, key=lambda x: str(x).lower())

def common_root(paths):
    if not paths:
        return Path.cwd()
    try:
        return Path(__import__("os").path.commonpath([str(p.resolve()) for p in paths]))
    except ValueError:
        return paths[0].parent.resolve()
