import random
import time
import subprocess

HANGMAN_ART = [
    """
  +---+
      |
      |
      |
     ===""",
    """
  +---+
  O   |
      |
      |
     ===""",
    """
  +---+
  O   |
  |   |
      |
     ===""",
    """
  +---+
  O   |
 /|   |
      |
     ===""",
    """
  +---+
  O   |
 /|\\  |
      |
     ===""",
    """
  +---+
  O   |
 /|\\  |
 /    |
     ===""",
    """
  +---+
  O   |
 /|\\  |
 / \\  |
     ===""",
]
WORDS = [
    "mean",
    "transparent",
    "fair",
    "dressing",
    "theft",
    "powder",
    "teach",
    "manner",
    "rock",
    "convulsion",
]


def main():
    chosen_word = random.choice(WORDS)
    blanks = ["_"] * len(chosen_word)
    guessed_words = []
    wrong_guesses = 0
    while True:
        subprocess.run(["clear"])
        print(HANGMAN_ART[wrong_guesses])
        print("\nYour word to guess is ", " ".join(blanks))
        print(f"Kisiko batana mat: {chosen_word}")
        user_guess = input("\nMake your guess: ").strip().lower()
        if not user_guess.isalpha() or len(user_guess) != 1:
            print("⚠️ Enter a single alphabet only.")
        elif user_guess in guessed_words:
            print("\nYou've already guessed that letter!")
        elif user_guess in chosen_word:
            print("That's a correct guess 🎉")
            guessed_words.append(user_guess)
            for index in range(len(chosen_word)):
                if chosen_word[index] == user_guess:
                    blanks[index] = user_guess
            if "_" not in blanks:
                subprocess.run(["clear"])
                print(f"\n🎉 YOU WIN! The word was '{chosen_word}'")
                break
        else:
            print("That's an incorrect guess. You lose a life ❌")
            print(f"You have {5- wrong_guesses} lives remaining")
            guessed_words.append(user_guess)
            wrong_guesses += 1
            if wrong_guesses >= 6:
                print(HANGMAN_ART[-1])
                print(f"\n💀 GAME OVER. The word was '{chosen_word}'")
                break
        time.sleep(1.5)


if __name__ == "__main__":
    main()
