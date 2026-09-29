import random

words = ["python", "computer", "programming", "developer", "internet"]

hints = {
    "python": "A popular programming language",
    "computer": "An electronic machine used for computing",
    "programming": "Writing instructions for a computer",
    "developer": "A person who creates software",
    "internet": "A worldwide network"
}

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def play_game():
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\nWelcome to Hangman!")
    print("Hint:", hints[word])

    while incorrect_guesses < max_attempts:
        print(hangman[incorrect_guesses])

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    print(hangman[incorrect_guesses])
    print("Game Over!")
    print("The word was:", word)


while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes" and again != "y":
        print("Thanks for playing!")
        break