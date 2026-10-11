# Starter issues for Friday

Create these as GitHub issues (or with the `gh issue create` commands at the bottom).
Then delete this file from the repo.

---

## 1. `word_count` miscounts with repeated whitespace and newlines

`word_count("hello  world")` returns 3 and `word_count("hello\nworld")` returns 1.
Both should return 2. Leading/trailing whitespace and whitespace-only input should also
behave sensibly (`"   "` → 0).

**Done when:** new tests cover these cases, they pass, ruff is clean, and `reading_time_minutes`
still passes its tests.

---

## 2. Add `slugify(title: str) -> str`

Turn a title into a URL slug: lowercase, ASCII letters/digits only, words joined by `-`,
no leading/trailing or repeated dashes. Danish letters should map sensibly
(`æ`→`ae`, `ø`→`oe`, `å`→`aa`). Example: `"Smørrebrød & Øl: Top 10!"` → `"smoerrebroed-oel-top-10"`.

**Done when:** `slugify` is exported from `playground`, has tests including the example above and
empty input, everything passes and ruff is clean.

---

## 3. (Language switch) Port `textstats` to a Rust crate

Create a Rust crate in `rust/textstats/` implementing `word_count`, `top_words` and
`reading_time_minutes` with the same behaviour as the Python version (including the fix from #1),
with `cargo test` coverage. Pin the toolchain in `mise.toml` (`rust = "stable"`).
Do NOT edit CI workflows; describe in the PR what CI job should be added.

**Done when:** `cargo test` and `cargo clippy -- -D warnings` pass in `rust/textstats/`,
and the Python tests still pass.

---

```bash
gh issue create -R <you>/friday-playground -t "word_count miscounts with repeated whitespace and newlines" -F - <<'X'
(paste issue 1 body)
X
```
