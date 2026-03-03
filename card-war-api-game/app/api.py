from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse

from .game import WarGame


router = APIRouter()
game = WarGame()


@router.get("/")
def root() -> dict[str, str]:
    return {"message": "Card War API is running"}


@router.get("/play", response_class=HTMLResponse)
def play_page() -> str:
        return """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Card War Game</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }
        .container { max-width: 960px; margin: 0 auto; padding: 24px; }
        h1 { margin-top: 0; }
        .controls { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 18px; }
        button { padding: 10px 14px; border: 0; border-radius: 8px; cursor: pointer; font-weight: 600; }
        button.primary { background: #22c55e; color: #052e16; }
        button.secondary { background: #93c5fd; color: #0c4a6e; }
        button.warn { background: #fbbf24; color: #451a03; }
        .board { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 14px; }
        .card-panel { background: #111827; border-radius: 12px; padding: 16px; text-align: center; }
        .card-panel img { width: 180px; max-width: 100%; min-height: 250px; background: #020617; border-radius: 10px; }
        .status { background: #111827; border-radius: 12px; padding: 16px; margin-top: 16px; }
        .small { color: #94a3b8; font-size: 0.9rem; }
    </style>
</head>
<body>
    <div class=\"container\">
        <h1>Card War Game</h1>
        <p class=\"small\">Click <strong>New Game</strong>, then <strong>Play Round</strong> to see live cards and winner updates.</p>

        <div class=\"controls\">
            <button class=\"primary\" id=\"newBtn\">New Game</button>
            <button class=\"secondary\" id=\"roundBtn\">Play Round</button>
            <button class=\"warn\" id=\"autoBtn\">Auto Finish</button>
            <button id=\"resetBtn\">Reset</button>
        </div>

        <div class=\"board\">
            <div class=\"card-panel\">
                <h3>Player 1</h3>
                <img id=\"p1img\" alt=\"Player 1 card\" />
                <p id=\"p1txt\">No card yet</p>
            </div>
            <div class=\"card-panel\">
                <h3>Player 2</h3>
                <img id=\"p2img\" alt=\"Player 2 card\" />
                <p id=\"p2txt\">No card yet</p>
            </div>
        </div>

        <div class=\"status\">
            <h3>Game Status</h3>
            <p id=\"winner\">Winner: -</p>
            <p id=\"cards\">Cards: P1=26, P2=26</p>
            <p id=\"rounds\">Rounds played: 0</p>
            <p id=\"roundWinner\">Round winner: -</p>
            <p id=\"wars\">Wars in round: 0</p>
        </div>
    </div>

    <script>
        const p1img = document.getElementById('p1img');
        const p2img = document.getElementById('p2img');
        const p1txt = document.getElementById('p1txt');
        const p2txt = document.getElementById('p2txt');
        const winner = document.getElementById('winner');
        const cards = document.getElementById('cards');
        const rounds = document.getElementById('rounds');
        const roundWinner = document.getElementById('roundWinner');
        const wars = document.getElementById('wars');

        function setState(state) {
            winner.textContent = `Winner: ${state.winner ?? '-'}`;
            cards.textContent = `Cards: P1=${state.player1_cards}, P2=${state.player2_cards}`;
            rounds.textContent = `Rounds played: ${state.rounds_played}`;
        }

        function setRound(detail, whoWon) {
            if (!detail) return;
            p1img.src = detail.p1_face_up.image_url;
            p2img.src = detail.p2_face_up.image_url;
            p1txt.textContent = `${detail.p1_face_up.rank} of ${detail.p1_face_up.suit}`;
            p2txt.textContent = `${detail.p2_face_up.rank} of ${detail.p2_face_up.suit}`;
            roundWinner.textContent = `Round winner: ${whoWon ?? '-'}`;
            wars.textContent = `Wars in round: ${detail.wars ?? 0}`;
        }

        async function callApi(path, method = 'GET') {
            const response = await fetch(path, { method });
            if (!response.ok) {
                const err = await response.text();
                alert(`Request failed: ${err}`);
                throw new Error(err);
            }
            return response.json();
        }

        document.getElementById('newBtn').addEventListener('click', async () => {
            const data = await callApi('/game/new', 'POST');
            setState(data.state);
            roundWinner.textContent = 'Round winner: -';
            wars.textContent = 'Wars in round: 0';
            p1img.removeAttribute('src');
            p2img.removeAttribute('src');
            p1txt.textContent = 'No card yet';
            p2txt.textContent = 'No card yet';
        });

        document.getElementById('roundBtn').addEventListener('click', async () => {
            const data = await callApi('/game/play-round', 'POST');
            if (data.round_detail) setRound(data.round_detail, data.round_winner);
            if (data.state) setState(data.state);
            if (data.status === 'game_over') roundWinner.textContent = `Round winner: game_over (${data.winner})`;
        });

        document.getElementById('autoBtn').addEventListener('click', async () => {
            const data = await callApi('/game/play-until-finish', 'POST');
            setState(data.state);
            roundWinner.textContent = 'Round winner: auto-finish complete';
        });

        document.getElementById('resetBtn').addEventListener('click', async () => {
            const data = await callApi('/game/reset', 'POST');
            setState(data.state);
            roundWinner.textContent = 'Round winner: -';
            wars.textContent = 'Wars in round: 0';
            p1img.removeAttribute('src');
            p2img.removeAttribute('src');
            p1txt.textContent = 'No card yet';
            p2txt.textContent = 'No card yet';
        });

        callApi('/game/state').then(setState).catch(() => {});
    </script>
</body>
</html>
"""


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
