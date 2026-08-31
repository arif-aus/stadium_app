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

| Column        | Type     | Description                          |
|---------------|----------|--------------------------------------|
| id            | INTEGER  | Auto-incrementing record ID          |
| timestamp     | DATETIME | When the badge was scanned (UTC)     |
| badge_id      | TEXT     | The person's badge identifier        |
| gate          | TEXT     | Which gate (A, B, C, D)             |
| entry_status  | TEXT     | GRANTED, DENIED, or FLAGGED          |
| security_level| INTEGER  | Clearance level required for gate    |
| notes         | TEXT     | Optional guard notes                 |

### Table: `gates`

| Column        | Type    | Description                       |
|---------------|---------|-----------------------------------|
| id            | INTEGER | Auto-incrementing gate ID         |
| name          | TEXT    | Gate label (A, B, C, D)          |
| security_level| INTEGER | Minimum clearance to enter        |
| status        | TEXT    | ACTIVE or LOCKED                  |

## Sensible Defaults

- **Red/Green TDD** — Write a failing test first, then make it pass with minimal code.
- **Spec-driven development** — Every feature starts with a written spec before code.
- **Walking skeleton** — Build the thinnest end-to-end slice first, then grow features.
- **Simplicity over complexity** — If a solution feels complicated, it probably is.
