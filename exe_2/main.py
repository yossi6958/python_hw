import random

from consts import GameConsts


def display_welcome_message() -> None:
    print(f"""
Welcome to The Guessing Game!
I have chosen a number between {GameConsts.MIN_RANGE} and {GameConsts.MAX_RANGE}.
    """)


def get_user_guess() -> int:
    while True:
        guess = input("Please make a guess: ")
        if guess.isdigit() and int(guess) in range(GameConsts.MAX_RANGE + 1):
            return int(guess)
        print("Invalid input. Please enter a number in the correct range.")


def evaluate_guess(guess: int, secret_number: int, remaining_guesses: int) -> bool:
    if guess == secret_number:
        print(f"Congratulations! You guessed the number correctly.")
        return True
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Too low.")
    print(f"You have {remaining_guesses} guesses remaining.")
    return False


def play_guessing_game() -> None:
    display_welcome_message()
    secret_number = random.randint(GameConsts.MIN_RANGE, GameConsts.MAX_RANGE)
    total_guesses = 0

    while total_guesses < GameConsts.MAX_GUESSES:
        guess = get_user_guess()
        total_guesses += 1
        remaining_guesses = GameConsts.MAX_GUESSES - total_guesses
        if evaluate_guess(guess, secret_number, remaining_guesses):
            return

    print(f"Game over! The secret number was {secret_number}.")


def ask_to_play_again() -> bool:
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ['y', 'yes']:
            return True
        elif play_again in ['n', 'no']:
            print("Thank you for playing!")
            return False
        print("Invalid input. Please enter 'y' or 'n'.")


def main() -> None:
    while True:
        play_guessing_game()
        if not ask_to_play_again():
            break


if __name__ == "__main__":
    main()
