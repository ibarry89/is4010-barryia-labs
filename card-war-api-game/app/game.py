from __future__ import annotations

from dataclasses import dataclass
from random import shuffle
from typing import Any


RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANK_VALUE = {rank: value for value, rank in enumerate(RANKS, start=2)}


@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    @property
    def value(self) -> int:
        return RANK_VALUE[self.rank]

    def to_dict(self) -> dict[str, Any]:
        return {"rank": self.rank, "suit": self.suit, "value": self.value}


class WarGame:
    def __init__(self) -> None:
        self.player1: list[Card] = []
        self.player2: list[Card] = []
        self.rounds_played: int = 0
        self.last_result: dict[str, Any] | None = None
        self.new_game()

    def _build_deck(self) -> list[Card]:
        deck = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        shuffle(deck)
        return deck

    def new_game(self) -> None:
        deck = self._build_deck()
        self.player1 = deck[:26]
        self.player2 = deck[26:]
        self.rounds_played = 0
        self.last_result = None

    def reset(self) -> None:
        self.new_game()

    def winner(self) -> str | None:
        if not self.player1 and not self.player2:
            return "draw"
        if not self.player1:
            return "player2"
        if not self.player2:
            return "player1"
        return None

    def state(self) -> dict[str, Any]:
        return {
            "rounds_played": self.rounds_played,
            "player1_cards": len(self.player1),
            "player2_cards": len(self.player2),
            "winner": self.winner(),
            "last_result": self.last_result,
        }

    def play_round(self) -> dict[str, Any]:
        if self.winner() is not None:
            result = {
                "status": "game_over",
                "winner": self.winner(),
                "message": "Game is already finished.",
            }
            self.last_result = result
            return result

        table: list[Card] = []
        p1_up = self.player1.pop(0)
        p2_up = self.player2.pop(0)
        table.extend([p1_up, p2_up])

        round_detail = {
            "p1_face_up": p1_up.to_dict(),
            "p2_face_up": p2_up.to_dict(),
            "wars": 0,
            "cards_on_table": len(table),
        }

        winner = self._resolve_battle(p1_up, p2_up, table, round_detail)

        if winner == "player1":
            self.player1.extend(table)
        elif winner == "player2":
            self.player2.extend(table)

        self.rounds_played += 1
        result = {
            "status": "ok",
            "round_winner": winner,
            "round_detail": round_detail,
            "state": self.state(),
        }
        self.last_result = result
        return result

    def _resolve_battle(
        self,
        p1_card: Card,
        p2_card: Card,
        table: list[Card],
        round_detail: dict[str, Any],
    ) -> str:
        if p1_card.value > p2_card.value:
            return "player1"
        if p2_card.value > p1_card.value:
            return "player2"

        while True:
            round_detail["wars"] += 1

            if len(self.player1) < 2:
                table.extend(self.player1)
                self.player1.clear()
                return "player2"
            if len(self.player2) < 2:
                table.extend(self.player2)
                self.player2.clear()
                return "player1"

            p1_face_down = self.player1.pop(0)
            p2_face_down = self.player2.pop(0)
            p1_face_up = self.player1.pop(0)
            p2_face_up = self.player2.pop(0)
            table.extend([p1_face_down, p2_face_down, p1_face_up, p2_face_up])

            round_detail["cards_on_table"] = len(table)
            round_detail["p1_face_up"] = p1_face_up.to_dict()
            round_detail["p2_face_up"] = p2_face_up.to_dict()

            if p1_face_up.value > p2_face_up.value:
                return "player1"
            if p2_face_up.value > p1_face_up.value:
                return "player2"

    def play_until_finish(self, max_rounds: int = 20000) -> dict[str, Any]:
        played = 0
        while self.winner() is None and played < max_rounds:
            self.play_round()
            played += 1

        status = "finished" if self.winner() is not None else "stopped_at_limit"
        return {
            "status": status,
            "rounds_played_in_call": played,
            "state": self.state(),
        }
