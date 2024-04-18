import random

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def draw_hangman(attempts):
    hangman_parts = [
        """
           ____
          |    |
          |
          |
          |
          |
        __|__
        """,
        """
           ____
          |    |
          |    O
          |
          |
          |
        __|__
        """,
        """
           ____
          |    |
          |    O
          |    |
          |
          |
        __|__
        """,
        """
           ____
          |    |
          |    O
          |   /|
          |
          |
        __|__
        """,
        """
           ____
          |    |
          |    O
          |   /|\\
          |
          |
        __|__
        """,
        """
           ____
          |    |
          |    O
          |   /|\\
          |   /
          |
        __|__
        """,
        """
           ____
          |    |
          |    O
          |   /|\\
          |   / \\
          |
        __|__
        """
    ]

    print(hangman_parts[attempts])

def hangman():
    word = input("Player 1, enter a word: ").lower()
    guessed_letters = []
    attempts = 6

    print("Player 2, start guessing. You have 6 attempts.")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
            draw_hangman(6 - attempts)

        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! Player 2 guessed the word:", word)
            break

        if attempts == 0:
            print("Sorry, Player 2 ran out of attempts. The word was:", word)
            draw_hangman(6)
            break

if __name__ == "__main__":
    hangman()
