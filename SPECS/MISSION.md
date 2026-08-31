# Mission

## What is this?

A stadium security dashboard that helps detectives track entry logs. When someone badges into the stadium through a gate, the system records who they are, which gate they used, and when — so investigators can look it up later.

## Why does it exist?

During investigations, detectives need reliable entry records. If the server crashes, that data must still be there. Persistence is non-negotiable — we don't lose evidence.

## Who is it for?

Detectives and security staff who need to search and review stadium entry logs quickly.

## What are we building?

A web app with:
- A frontend dashboard to view and search entry logs
- A Flask backend that serves the data
- An SQLite database that keeps records on disk so they survive crashes

## What is NOT in scope?

- Real-time gate status monitoring
- Suspicious activity alerts or flagging
- User authentication or roles
- Complex analytics or charts

## Non-negotiables

- **Data must persist.** If the server restarts, every entry log is still there.
- **Beginner-friendly.** Simple code that students can understand and modify.
- **Clean boundaries.** Frontend never touches the database directly.
