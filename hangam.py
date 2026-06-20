import random

def hangman_game():
    words = ["python", "computer", "programming", "developer", "keyboard"]

    secret_word = random.choice(words)
    guessed_letter = []
    attempts_left = 6

    print("\n======= HANGMAN GAME =======")

    while attempts_left > 0:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letter:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts_left}")

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly.")
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letter:
            print("You already guessed this letter.")
            continue

        guessed_letter.append(guess)

        if guess not in secret_word:
            attempts_left -= 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")

    print(f"\nGame Over! The word was '{secret_word}'")


if __name__ == "__main__":
    hangman_game()