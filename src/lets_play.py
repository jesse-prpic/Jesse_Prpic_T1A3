from word_game import Word_game
import sys
from termcolor import colored

# Defining the game play and outputs of the players guesses
def main():
    print("Welcome to Word Game!")
    word_game = Word_game("APPLES")

# The player is only able to guess 6 letter words, if more or less they will be given an error
    while word_game.ongoing_guesses:
            x = input("Guess a word: ")

            if len(x) != word_game.WORD_LEGNTH:
                 print(colored(f"Word must be {word_game.WORD_LEGNTH} letters long!", "red"))
                 continue
            word_game.guess(x)
            result = word_game.tries(x)
            print(result)

# If the guess is correct, you will win the game - if not you lose.
    if word_game.game_won:
        print("Congratulations, you guess is correct!")
    else:
         print("Womp womp, try again!")

if __name__ == "__main__":
    main()