import random

def play_game():
    number = random.randint(1, 100)
    tries = 0
    max_tries = 7

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_tries} tries to guess it.\n")

    while tries < max_tries:
        try:
            guess = int(input(f"Attempt {tries + 1}: Enter your guess → "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        tries += 1

        if guess < number:
            print("🔼 Too low!")
        elif guess > number:
            print("🔽 Too high!")
        else:
            print(f"🎉 Correct! You guessed the number in {tries} tries.")
            return tries  # return score

    print(f"😢 Sorry! The number was {number}. Better luck next time.")
    return 0  # no score

# Run the game multiple times and track score
total_score = 0
games_played = 0

while True:
    score = play_game()
    games_played += 1
    total_score += score

    again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        break

print("\n🧾 Game Summary:")
print(f"Games played: {games_played}")
print(f"Total correct guesses: {total_score}")
print("Thanks for playing!")

