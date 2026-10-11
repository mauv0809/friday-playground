"""Basic text statistics."""

from collections import Counter


def word_count(text: str) -> int:
    """Return the number of words in ``text``."""
    return len(text.split())


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the ``n`` most common words (lowercased) with their counts."""
    words = [w.strip(".,!?;:").lower() for w in text.split()]
    return Counter(w for w in words if w).most_common(n)


def reading_time_minutes(text: str, wpm: int = 200) -> float:
    """Estimated reading time in minutes, rounded to one decimal."""
    if wpm <= 0:
        raise ValueError("wpm must be positive")
    return round(word_count(text) / wpm, 1)
