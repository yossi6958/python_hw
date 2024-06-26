from dataclasses import dataclass


@dataclass
class GameConstants:
    INITIAL_WATER_SUPPLY: int = 5
    MODERATE_SPEED_DISTANCE: int = 10
    FULL_SPEED_DISTANCE: int = 20
    MODERATE_SPEED_TIREDNESS: int = 1
    FULL_SPEED_TIREDNESS: int = 3
    BANDITS_INITIAL_DISTANCE: int = -20
    BANDITS_ADVANCE: int = 7
    CAMEL_THIRST_LIMIT: int = 6
    CAMEL_TIREDNESS_LIMIT: int = 8
    DESERT_LENGTH: int = 200


@dataclass
class GameState:
    WATER_SUPPLY: int
    CAMEL_THIRST: int
    CAMEL_TIREDNESS: int
    DISTANCE_TRAVELED: int
    BANDITS_DISTANCE: int

    def __init__(self, constants: GameConstants):
        self.WATER_SUPPLY = constants.INITIAL_WATER_SUPPLY
        self.CAMEL_THIRST = 0
        self.CAMEL_TIREDNESS = 0
        self.DISTANCE_TRAVELED = 0
        self.BANDITS_DISTANCE = constants.BANDITS_INITIAL_DISTANCE
