# Requirements — Display Stadium Entries from Persistent Storage

Feature spec date: 2026-08-31
Branch: `feature/display-entries`

## Goal

Detectives can open the dashboard and see all stadium entry records stored in `stadium.db`. The data must come from the persistent SQLite database (seeded with championship-game data), not from in-memory mock data. This is the first roadmap milestone.

## Scope (in)

- Frontend `frontend/index.html` renders entries in a table.
- Frontend `frontend/app.js` fetches from the backend and renders rows.
- Backend exposes `GET /api/entries`.
- Backend supports an optional `?gate=A` query filter.
- Data layer `backend/data_layer.py` owns all SQL queries.
- Reads from the existing `stadium.db` (championship game seed data).

## Scope (out)

- Writing/creating new entries (no POST/PUT endpoints yet).
- Deleting or editing entries.
- Gate status or alerts (removed per updated constitution).
- Authentication and roles.

## Context & Decisions

### Schema in use
The live database and existing code use this table/columns via `seed.sql`:

| Column     | Type    |
|------------|---------|
| id         | INTEGER |
| person_id  | INTEGER |
| gate       | TEXT    |
| hour       | INTEGER |
| bag        | TEXT    |

There is also a `people` table (id, name, phone) but it is **not** required for this feature. The dashboard shows entries only.

### Constitution mismatch (flagged for later)
`SPECS/TECH.md` lists a different schema (`badge_id`, `timestamp`, `entry_status`, `security_level`, `notes`). That schema does **not** match the actual seeded database or the existing code. For this feature we follow the **actual live schema**. A separate task updates the constitution to match reality — noted in the roadmap, not addressed here.

### Architectural boundaries (from SPECS/TECH.md, strictly enforced)
1. **Frontend** — HTTP requests and rendering only. Zero SQL knowledge.
2. **Backend** (`app.py`) — routing, validation, JSON. Never imports `sqlite3`, never writes SQL.
3. **Data layer** (`data_layer.py`) — the only file that imports `sqlite3` and runs SQL. Uses parameterised queries.
4. **Database** (`stadium.db`) — on-disk SQLite.

### Logging
Backend route should log requests (start, success, error) without mixing logging logic into the data layer. Prefer a simple decorator or wrapper on the route handler.

## Acceptance (high level)

- `GET /api/entries` returns all seeded entries as JSON.
- `GET /api/entries?gate=C` returns only Gate C entries.
- Dashboard table shows id, person_id, gate, hour, bag for every entry.
- Filter dropdown and Refresh work.
- Status badge shows backend connected/count.
