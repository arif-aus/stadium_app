# Stadium Security Dashboard

A web app that helps detectives track stadium entry logs. Records who badged in, which gate they used, and when — and keeps that data safe even if the server crashes.

## Stack

- **Frontend**: HTML, CSS, vanilla JavaScript
- **Backend**: Python, Flask
- **Database**: SQLite (stadium.db)

## Quick Start

```bash
# Install Flask (if not already installed)
pip install flask

# Run the app
python backend/app.py
```

Then open `frontend/index.html` in your browser.

## Project Structure

```
stadium_app/
├── backend/
│   ├── app.py            # Flask routes (HTTP layer)
│   └── data_layer.py     # Database access (only place with SQL)
├── frontend/
│   ├── index.html         # Dashboard page
│   └── app.js             # Frontend logic
├── stadium.db             # SQLite database (auto-created)
├── seed.sql               # Sample data
├── SPECS/
│   ├── MISSION.md         # Why this project exists
│   ├── TECH.md            # Stack, architecture, rules
│   └── ROADMAP.md         # What's done, what's next
└── README.md              # This file
```

## Architecture

Data flows one way through four layers:

```
Frontend → Backend (Flask) → Data Layer (data_layer.py) → SQLite (stadium.db)
```

- The **frontend** never touches the database.
- The **backend** never writes SQL — it calls the Data Layer.
- The **Data Layer** is the only file that runs SQL queries.

## Learn More

Read the constitution in `SPECS/` for the full mission, technical rules, and roadmap.
