"""URL slug helpers."""

import re
import unicodedata

_DANISH = str.maketrans({"æ": "ae", "ø": "oe", "å": "aa"})
_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(title: str) -> str:
    """Turn ``title`` into a lowercase ASCII URL slug with words joined by ``-``."""
    text = title.lower().translate(_DANISH)
    # Strip accents (é -> e); characters with no ASCII base are dropped.
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return _NON_ALNUM.sub("-", text).strip("-")
