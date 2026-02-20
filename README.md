# SmartVeriRank

AI-assisted RTL verification log analysis and prioritization system.

## What it does
- Parses RTL simulation logs
- Extracts structured error events
- Uses ML to rank failures by impact
- (Upcoming) Clusters related failures
- (Upcoming) API for frontend integration

## Project structure
- `/ml` — Machine learning pipeline
- `/frontend` — UI (React + auth)
- `/backend` — API + DB

## How to run ML pipeline
```bash
python ml/src/main.py