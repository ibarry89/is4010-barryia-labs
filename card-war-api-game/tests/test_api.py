from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Card War API is running"


def test_play_page_serves_html():
    response = client.get("/play")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Card War Game" in response.text


def test_game_state_and_round_flow():
    new_game = client.post("/game/new")
    assert new_game.status_code == 200

    state = client.get("/game/state")
    assert state.status_code == 200
    payload = state.json()
    assert payload["player1_cards"] == 26
    assert payload["player2_cards"] == 26

    play_round = client.post("/game/play-round")
    assert play_round.status_code == 200
    round_payload = play_round.json()
    assert round_payload["status"] in {"ok", "game_over"}
