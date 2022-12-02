from enum import Enum, auto
from pathlib import Path


class RPS(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def score(self) -> int:
        """Returns the score for the given shape"""
        match self:
            case RPS.ROCK:
                return 1
            case RPS.PAPER:
                return 2
            case RPS.SCISSORS:
                return 3

    @classmethod
    def from_character(cls, character: str) -> "RPS":
        """Returns a RPS from the given character.
        A, X -> ROCK
        B, Y -> PAPER
        C, Z -> SCISSORS
        """

        match character:
            case "A" | "X":
                return RPS.ROCK
            case "B" | "Y":
                return RPS.PAPER
            case "C" | "Z":
                return RPS.SCISSORS

        raise ValueError("Given character is not a valid input: " + character)


class RPSResult(int, Enum):
    LOST = 0
    DRAW = 3
    WON = 6

    @classmethod
    def round_result(cls, own: RPS, opponent: RPS) -> "RPSResult":
        match (own, opponent):
            case (RPS.ROCK, RPS.PAPER):
                return RPSResult.LOST
            case (RPS.ROCK, RPS.SCISSORS):
                return RPSResult.WON

            case (RPS.PAPER, RPS.ROCK):
                return RPSResult.WON
            case (RPS.PAPER, RPS.SCISSORS):
                return RPSResult.LOST

            case (RPS.SCISSORS, RPS.ROCK):
                return RPSResult.LOST
            case (RPS.SCISSORS, RPS.PAPER):
                return RPSResult.WON
            case (x, y) if x == y:  # pylint:disable=used-before-assignment
                return RPSResult.DRAW

    @classmethod
    def score_from_row(cls, row: str) -> int:
        """
        Parses a coded rock-paper-scissors row and returns the score of the
        resulting game. Row is formatted as
            opponent_choice own_choice
        where opponent_choice is X, Y, Z for rock, paper, scissors
        and own_choice is A, B, C for rock, paper, scissors
        """
        characters = row.strip().split(" ")
        opponent = RPS.from_character(characters[0])
        own = RPS.from_character(characters[1])

        return cls.round_result(own, opponent).value + own.score()


def puzzle1_score() -> int:
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r", encoding="utf-8") as fp:
        rows = fp.readlines()

    print(f"{len(rows)} games.")

    return sum(RPSResult.score_from_row(row) for row in rows)
