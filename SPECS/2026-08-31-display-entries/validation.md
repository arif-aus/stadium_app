# Validation — Display Stadium Entries from Persistent Storage

How we know this feature is complete and safe to merge.

## Must pass

1. **Persistence check**
   - All 22 championship-game entries appear in the dashboard table.
   - Data comes from `stadium.db`, not in-memory mock data. Reader can confirm by inspecting the DB / data layer.
2. **Automated tests (TDD)**
   - `pytest` suite runs green: data layer (`get_all_entries`, `get_entries_by_gate`) and backend routes (`GET /api/entries`, `?gate=C`, 500-on-error).
   - Tests use an isolated temporary DB — **no test writes** to `stadium.db`.
3. **Architectural boundaries**
   - `app.py` does not import `sqlite3` and contains no SQL strings.
   - All SQL lives in `data_layer.py` and uses parameterised queries (`?` placeholders). No string-formatted SQL.
   - Frontend contains zero SQL.
4. **Frontend behaviour**
   - Table renders all columns (id, person_id, gate, hour, bag).
   - Gate filter and Refresh work and update the row count + status badge.

## Merge gates

- [ ] All pytest tests green.
- [ ] Manual run via `./run.sh` shows 22 rows on load.
- [ ] Logging present on backend route without leaking into data layer.
- [ ] `stadium.db` unchanged / not corrupted.

## Post-merge follow-up (surfaced, not actioned here)

- [ ] Flag to user: `SPECS/TECH.md` schema (badge_id/timestamp/entry_status/security_level/notes) does **not** match the live schema (person_id/hour/bag). Get user approval to update the constitution on `main` to match reality.
- [ ] Remove the outdated `SPECS/DATA_LAYER/` references in ROADMAP if they reference the old schema.
