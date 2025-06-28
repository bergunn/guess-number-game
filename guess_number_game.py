import random


def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have a maximum of 8 attempts to guess it correctly.")

    number_to_guess = random.randint(1, 50)
    max_attempts = 8
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))

            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"🎉 Correct! The number was {number_to_guess}. You guessed it in {attempts} attempts.")
                print("🏆 You win!")
                break
        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"❌ You've used all {max_attempts} attempts. The number was {number_to_guess}.")
        print("💔 You lose. Better luck next time!")


if __name__ == "__main__":
    guess_the_number()