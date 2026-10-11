import pytest

from playground import reading_time_minutes, top_words, word_count


def test_word_count_simple():
    assert word_count("hello brave new world") == 4


def test_word_count_empty():
    assert word_count("") == 0


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello  world", 2),
        ("hello\nworld", 2),
        ("hello\t\r\n world", 2),
        ("  hello world  ", 2),
        ("\nhello world\n", 2),
        ("   ", 0),
        ("\n\t ", 0),
    ],
)
def test_word_count_whitespace(text, expected):
    assert word_count(text) == expected


def test_top_words():
    assert top_words("the cat and the hat. The end!", n=1) == [("the", 3)]


def test_reading_time():
    assert reading_time_minutes("word " * 400) == 2.0


def test_reading_time_rejects_bad_wpm():
    with pytest.raises(ValueError):
        reading_time_minutes("hi", wpm=0)
