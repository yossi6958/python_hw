from dataclasses import dataclass


@dataclass
class GameConsts:
    MIN_RANGE: int = 0
    MAX_RANGE: int = 10
    MAX_GUESSES: int = 10
