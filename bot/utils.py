def normalize_link(raw: str) -> str:
    if not raw:
        return raw
    s = raw.strip()
    if s.startswith("@https://") or s.startswith("@http://"):
        s = s[1:]
    if s.startswith("@"):
        return f"https://t.me/{s[1:]}"
    return s


