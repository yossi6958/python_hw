from exe_3.consts import GameState, GameConstants


def drink_water(state: GameState):
    if state.WATER_SUPPLY > 0:
        state.WATER_SUPPLY -= 1
        state.CAMEL_THIRST = 0
        print("You drank water. Your camel is no longer thirsty.")
    else:
        print("No water left!")


def move_moderate_speed(state: GameState, constants: GameConstants):
    state.DISTANCE_TRAVELED += constants.MODERATE_SPEED_DISTANCE
    state.CAMEL_THIRST += 1
    state.CAMEL_TIREDNESS += constants.MODERATE_SPEED_TIREDNESS
    state.BANDITS_DISTANCE += constants.BANDITS_ADVANCE
    print(f"You traveled {constants.MODERATE_SPEED_DISTANCE} km at moderate speed.")


def move_full_speed(state: GameState, constants: GameConstants):
    state.DISTANCE_TRAVELED += constants.FULL_SPEED_DISTANCE
    state.CAMEL_THIRST += 1
    state.CAMEL_TIREDNESS += constants.FULL_SPEED_TIREDNESS
    state.BANDITS_DISTANCE += constants.BANDITS_ADVANCE
    print(f"You traveled {constants.FULL_SPEED_DISTANCE} km at full speed.")


def rest(state: GameState, constants: GameConstants):
    state.CAMEL_TIREDNESS = 0
    state.BANDITS_DISTANCE += constants.BANDITS_ADVANCE
    print("You rested. Your camel is no longer tired.")


def check_status(state: GameState, constants: GameConstants):
    print(f"Distance traveled: {state.DISTANCE_TRAVELED} km")
    print(f"Water left: {state.WATER_SUPPLY}")
    print(f"Camel thirst level: {state.CAMEL_THIRST}")
    print(f"Camel tiredness level: {state.CAMEL_TIREDNESS}")
    print(f"Bandits' distance: {state.DISTANCE_TRAVELED - state.BANDITS_DISTANCE} km behind")
