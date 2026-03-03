# Card War API Game (Python)

A standalone Python project that implements a classic **War** card game and exposes it via a REST API using FastAPI.

## Features

- Full 52-card deck with shuffle and split between two players
- Round-by-round play with automatic tie resolution (war)
- Game state tracking: round count, pile sizes, winner
- API endpoints to start/reset a game and play rounds
- Drawn cards include `image_url` so you can open real card images

## Project Structure

- `app/game.py` - core game logic
- `app/api.py` - FastAPI routes
- `app/main.py` - app entrypoint

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open: `http://127.0.0.1:8000/docs`

## How to Play (Visual via API)

1. Open `http://127.0.0.1:8000/docs`
2. Run `POST /game/new` (creates a shuffled game)
3. Run `POST /game/play-round`
4. In the response, open:
	- `round_detail.p1_face_up.image_url`
	- `round_detail.p2_face_up.image_url`
5. Keep calling `POST /game/play-round` until `state.winner` is not `null`

Fast play option:
- Run `POST /game/play-until-finish` to complete the whole game automatically.

## Test

```bash
pytest tests/ -v
```

## API Endpoints

- `GET /` - health/info
- `POST /game/new` - create a new game
- `GET /game/state` - current game state
- `POST /game/play-round` - play one round
- `POST /game/play-until-finish` - auto-play until winner
- `POST /game/reset` - reset current game with fresh shuffle

