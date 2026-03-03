from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from .game import WarGame


router = APIRouter()
game = WarGame()


@router.get("/")
def root() -> dict[str, str]:
    return {"message": "Card War API is running"}


@router.post("/game/new")
def new_game() -> dict:
    game.new_game()
    return {"message": "New game created", "state": game.state()}


@router.get("/game/state")
def game_state() -> dict:
    return game.state()


@router.post("/game/play-round")
def play_round() -> dict:
    return game.play_round()


@router.post("/game/play-until-finish")
def play_until_finish(max_rounds: int = Query(default=20000, ge=1, le=200000)) -> dict:
    if game.winner() is not None:
        raise HTTPException(status_code=400, detail="Game is already finished. Reset or start a new game.")
    return game.play_until_finish(max_rounds=max_rounds)


@router.post("/game/reset")
def reset_game() -> dict:
    game.reset()
    return {"message": "Game reset", "state": game.state()}
