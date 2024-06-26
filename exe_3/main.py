from exe_3.commands import drink_water, move_moderate_speed, move_full_speed, rest, check_status
from exe_3.consts import GameState, GameConstants


def print_instructions():
    print("""
Welcome to the Camel Game!

In this game, you are a rider on a camel trying to escape across the desert while being chased by bandits.
You need to manage your resources carefully to survive and win.

You can choose one of the following actions each turn:
A. Drink water from your canteen.
B. Move at moderate speed.
C. Move at full speed.
D. Stop and rest.
E. Check status.
Q. Quit the game.

Beware of your camel's thirst and tiredness, and keep an eye on the bandits chasing you. Good luck!
""")


def get_choice():
    choice = input("Choose your action (A/B/C/D/E/Q): ").upper()
    while choice not in ['A', 'B', 'C', 'D', 'E', 'Q']:
        print("Invalid choice. Please choose again.")
        choice = input("Choose your action (A/B/C/D/E/Q): ").upper()
    return choice


def check_game_over(state: GameState, constants: GameConstants):
    if state.CAMEL_THIRST > constants.CAMEL_THIRST_LIMIT:
        print("Your camel has died of thirst. Game over.")
        return True
    if state.CAMEL_TIREDNESS > constants.CAMEL_TIREDNESS_LIMIT:
        print("Your camel has died of exhaustion. Game over.")
        return True
    if state.BANDITS_DISTANCE >= state.DISTANCE_TRAVELED:
        print("The bandits have caught you. Game over.")
        return True
    if state.DISTANCE_TRAVELED >= constants.DESERT_LENGTH:
        print("Congratulations! You have successfully crossed the desert and escaped the bandits.")
        return True
    return False


def main():
    constants = GameConstants()
    state = GameState(constants)

    print_instructions()
    game_over = False

    while not game_over:
        choice = get_choice()

        if choice == 'A':
            drink_water(state)
        elif choice == 'B':
            move_moderate_speed(state, constants)
        elif choice == 'C':
            move_full_speed(state, constants)
        elif choice == 'D':
            rest(state, constants)
        elif choice == 'E':
            check_status(state, constants)
        elif choice == 'Q':
            game_over = True
            print("You quit the game.")

        if not game_over:
            game_over = check_game_over(state, constants)


if __name__ == "__main__":
    main()
