from app.game import WarGame


def test_new_game_deals_evenly():
    game = WarGame()

    assert game.state()["player1_cards"] == 26
    assert game.state()["player2_cards"] == 26
    assert game.state()["winner"] is None


def test_play_round_updates_counts_and_round_number():
    game = WarGame()
    before_total = game.state()["player1_cards"] + game.state()["player2_cards"]

    result = game.play_round()

    assert result["status"] == "ok"
    assert result["state"]["rounds_played"] == 1

    after_total = result["state"]["player1_cards"] + result["state"]["player2_cards"]
    assert before_total == 52
    assert after_total == 52


def test_play_until_finish_returns_terminal_status():
    game = WarGame()
    outcome = game.play_until_finish(max_rounds=20000)

    assert outcome["status"] in {"finished", "stopped_at_limit"}
    assert "state" in outcome
