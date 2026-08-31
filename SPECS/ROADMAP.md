# Roadmap

## Current Focus: Persistent Entry Log Storage

We have a working Flask backend with mock data. The next step is wiring it up to SQLite so entry logs survive server crashes.

---

## Milestones

### Phase 1: Baseline Architecture `[COMPLETED]`
- [x] Flask backend with REST API routes
- [x] HTML/CSS/JS frontend skeleton
- [x] Mock entry log data
- [x] Entry log schema defined

### Phase 2: SQLite Data Layer `[IN PROGRESS]`
- [ ] Initialize SQLite database (`stadium.db`)
- [ ] Implement `backend/data_layer.py` — the only file that touches SQL
- [ ] Create `stadium_entries` table
- [ ] Refactor API routes to use the Data Layer
- [ ] Verify data persists across server restarts

### Phase 3: Frontend Integration `[UPCOMING]`
- [ ] Connect dashboard to live SQLite backend
- [ ] Display entry logs in a table
- [ ] Add search/filter by gate, badge ID, and time
- [ ] Handle loading and error states in the UI

### Phase 4: Polish & Validation `[PLANNED]`
- [ ] Write validation tests (data survives restart, filters work, etc.)
- [ ] Clean up UI styling
- [ ] Final review of architectural boundaries

---

## Architectural Rules

1. **Frontend** — Renders the dashboard. Sends HTTP requests. Never sees SQL.
2. **Backend** — Handles requests, validates input, returns JSON. Never writes SQL directly.
3. **Data Layer** (`data_layer.py`) — The only place that runs SQL queries.
4. **Database** (`stadium.db`) — On-disk SQLite file. Data survives crashes.
