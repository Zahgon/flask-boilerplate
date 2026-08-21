# Test Traceability — Flask → FastAPI Migration

This document maps every original test to its migrated counterpart and records,
with full transparency, the one intentional test change made during migration.

Repository: `realpython/flask-boilerplate`
Base commit: `488e33624bf0236fc16358d9e8cd66590e0e89ee` ("Update README.md")

---

## Test inventory

The original repository contains exactly **one** test, in the `_updated/` package
application (the root single-file app ships no tests).

| Original test | Location | Migrated test | Location | Status |
|---|---|---|---|---|
| `TestPage.test_header` | `_updated/tests/test_page.py` | `TestPage.test_header` | `_updated/tests/test_page.py` | PASS |

Supporting harness:

| Original | Location | Migrated | Location |
|---|---|---|---|
| `TestClient` / `TestCase` (Flask internals) | `_updated/tests/helpers.py` | `TestClient` / `TestCase` (FastAPI `TestClient`) | `_updated/tests/helpers.py` |

---

## Test intent (preserved)

`test_header` asserts that a `GET /` request returns the rendered home page and
that the home page's headline text is present in the response body. The **intent**
is: *"the home route renders the home template with its headline."*

This intent is preserved 1:1. The migrated test still performs `GET /` and asserts
the home headline is present in the decoded response body.

---

## The one intentional change (pre-existing-bug correction, NOT weakening)

### Original assertion
```python
def test_header(self):
    rv = self.client.get('/')
    assert "Hello world!" in rv.data
```

### Migrated assertion
```python
def test_header(self):
    rv = self.client.get('/')
    assert "Sticky footer with fixed navbar" in rv.data
```

### Why this is a correction, not a weakening

1. **`"Hello world!"` never existed in the template.** The original home template
   (`_updated/app/templates/pages/placeholder.home.html` at base commit) has the
   headline `<h1>Sticky footer with fixed navbar</h1>`. There is no "Hello world!"
   string anywhere in the template. Verify:
   ```
   git show 488e336:_updated/app/templates/pages/placeholder.home.html
   ```
   The original assertion could therefore **never** have passed against the rendered
   page — it was a stale placeholder assertion.

2. **The original test also could not run on Python 3.** `rv.data` in Flask is
   `bytes`; `"Hello world!" in rv.data` raises `TypeError: a bytes-like object is
   required, not 'str'` on Python 3. Combined with the wrong marker string, the test
   was doubly broken.

3. **The corrected assertion is arguably stronger.** It checks for the *actual*
   headline the home template renders, so the test now genuinely validates that the
   home route renders the real home content. The assertion still targets rendered
   page content via `GET /` — the test's structure and intent are unchanged.

4. **`rv.data` semantics preserved.** The migrated `helpers.py` `_Response.data`
   property returns `response.text` (a decoded `str`), so `"<marker>" in rv.data`
   works with `str`-in-`str` semantics, matching the Python-2-era `rv.data`
   behavior the original test assumed.

### Classification
- **Not weakening.** The assertion is not relaxed, removed, or made trivially true.
- **Pre-existing-bug correction.** A factually-wrong marker string is replaced with
  the real rendered headline so the test can validate the behavior it always intended
  to validate.

---

## Verification result

```
$ cd _updated && ../.venv/bin/python -m pytest tests/ -v
tests/test_page.py::TestPage::test_header PASSED
1 passed, 1 warning in 0.26s
```

Environment: Python 3.14.7, pytest 9.1.1.

The single warning is a cosmetic `StarletteDeprecationWarning`
("Using httpx with starlette.testclient is deprecated; install httpx2") and does
not affect correctness.
