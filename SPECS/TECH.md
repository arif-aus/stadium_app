# Technical Stack & Architecture

## Stack

| Layer       | Technology              |
|-------------|------------------------|
| Frontend    | HTML, CSS, vanilla JS  |
| Backend     | Python, Flask          |
| Database    | SQLite (stadium.db)    |

No frameworks, no libraries beyond Flask. Keep it simple.

## Architecture: Four Layers

```
Frontend (HTML/CSS/JS)
    |
    | HTTP / JSON
    v
Backend (Flask routes)
    |
    | Python function calls
    v
Data Layer (data_layer.py)
    |
    | SQL (parameterized)
    v
SQLite Database (stadium.db)
```

Each layer has one job:

1. **Frontend** — Displays the dashboard. Sends HTTP requests to the backend. Never sees SQL.
2. **Backend** — Handles HTTP requests, validates input, returns JSON. Never writes SQL directly.
3. **Data Layer** — The only place that touches the database. All SQL lives here.
4. **Database** — Stores entry logs on disk so they survive server crashes.

## Engineering Rules

### SQL Injection Prevention
- **Never** build SQL with string formatting: `f"SELECT * FROM entries WHERE gate = '{gate}'"` — this is dangerous.
- **Always** use parameterized queries: `cursor.execute("SELECT * FROM entries WHERE gate = ?", (gate,))` — this is safe.

### Boundary Enforcement
- Backend routes must **never** import `sqlite3`. They call Data Layer methods instead.
- Frontend must **never** know about the database file path or schema.

### Data Integrity
- Database writes use transactions. If something fails, we roll back — no half-written records.

## Data Schema

### Table: `stadium_entries`

The live database (see `seed.sql`) uses this schema:

| Column     | Type    | Description                              |
|------------|---------|------------------------------------------|
| id         | INTEGER | Auto-incrementing record ID              |
| person_id  | INTEGER | Foreign key to `people(id)`              |
| gate       | TEXT    | Which gate (A, B, C, D)                  |
| hour       | INTEGER | Hour of day the person entered           |
| bag        | TEXT    | Bag type (`none`, `bag`, `backpack`, etc.) |

### Table: `people`

Holds attendee details, referenced by `stadium_entries.person_id`.

| Column | Type    | Description              |
|--------|---------|--------------------------|
| id     | INTEGER | Person's unique ID       |
| name   | TEXT    | Attendee name            |
| phone  | TEXT    | Contact phone            |

> Note: an earlier draft of this document listed a different schema
> (`timestamp`, `badge_id`, `entry_status`, `security_level`, `notes`).
> It was corrected to match the actual seeded database and the code.

## Sensible Defaults

- **Red/Green TDD** — Write a failing test first, then make it pass with minimal code.
- **Spec-driven development** — Every feature starts with a written spec before code.
- **Walking skeleton** — Build the thinnest end-to-end slice first, then grow features.
- **Simplicity over complexity** — If a solution feels complicated, it probably is.
