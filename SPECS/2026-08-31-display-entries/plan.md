# Plan — Display Stadium Entries from Persistent Storage

Branch: `feature/display-entries`
Feature spec: `SPECS/2026-08-31-display-entries/`

This is a Red/Green TDD repo. Tests are written **before** feature code and run until they pass. The existing files already contain a working implementation, so the first task is to lock in the current behaviour with failing-then-passing tests, then close any gaps.

## Task Group 1 — Test harness setup

- [ ] 1.1 Install Flask (`pip install flask`) for local runs.
- [ ] 1.2 Create `backend/tests/` directory and a `tests/` runner at repo root or `backend/` (decide one consistent location).
- [ ] 1.3 Add `conftest.py` that builds a **temporary** SQLite DB (in `tempfile`) and seeds it with a small known sample (mirror of `seed.sql` structure) so tests never touch `stadium.db`.
- [ ] 1.4 Add a way to point `data_layer.DB_PATH` at the temp DB for tests (e.g. a setter/module attribute override).

## Task Group 2 — Data layer tests (Red)

- [ ] 2.1 Write failing test: `get_all_entries()` returns all seeded rows, newest-first ordering by `hour DESC`.
- [ ] 2.2 Write failing test: `get_entries_by_gate('C')` returns only Gate C rows.
- [ ] 2.3 Write failing test: each returned row is a plain dict with keys `id, person_id, gate, hour, bag`.
- [ ] 2.4 Run tests → observe failures (Red), then confirm existing `data_layer.py` already satisfies them (Green).

## Task Group 3 — Backend route tests (Red → Green)

- [ ] 3.1 Write failing test using Flask test client:
  - `GET /api/entries` → 200, JSON array length matches seeded count.
  - `GET /api/entries?gate=C` → 200, only gate C.
  - `GET /api/entries` with a forced DB error → 500 with `{"error": ...}`.
- [ ] 3.2 Implement/add any route logic needed to pass (app.py already has the route; confirm boundary: no `import sqlite3` in app.py).
- [ ] 3.3 Assert `app.py` does **not** import `sqlite3` (boundary check — lint by inspection or a test).

## Task Group 4 — Logging

- [ ] 4.1 Add a lightweight logging decorator (e.g. `@log_route`) applied to `get_entries`, logging request start, success (count), and errors — without putting logging logic in `data_layer.py`.
- [ ] 4.2 Update/verify tests still pass.

## Task Group 5 — Frontend verification

- [ ] 5.1 Confirm `frontend/index.html` table headers match the live schema columns (`id, person_id, gate, hour, bag`).
- [ ] 5.2 Confirm `frontend/app.js` `fetchEntries()` and `renderTable()` match those columns; adjust if needed.
- [ ] 5.3 Verify gate filter dropdown + refresh + status badge wiring.
- [ ] 5.4 Manual check: run backend, load dashboard, see 22 seeded entries.

## Task Group 6 — Spec sync (post-validation)

- [ ] 6.1 Confirm `SPECS/TECH.md` schema mismatch is flagged to user; update constitution only after user approval (do **not** change it in this feature branch unilaterally).

## Checks to run

- [ ] `python3 -m pytest backend/tests -v` (or wherever tests live)
- [ ] Inspect `app.py` imports — no `sqlite3`
- [ ] Manual run via `./run.sh` and load the dashboard
