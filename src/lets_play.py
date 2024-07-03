from typing import List
from word_game import Word_game
from letter_response import Responsiveness
# import sys
from colorama import Fore, Back

# Defining the game play and outputs of the players guesses
def main():
    print("Welcome to Word Game!")
    word_game = Word_game("APPLES")

# The player is only able to guess 6 letter words, if more or less they will be given an error
    while word_game.ongoing_guesses:
            x = input("\n Guess a word: ")

            if len(x) != word_game.WORD_LEGNTH:
                print(Back.RED + f"Word must be {word_game.WORD_LEGNTH} characters long! " + Back.RESET)
                continue

            word_game.guess(x)
            show_results(word_game)

# If the guess is correct, you will win the game - if not you lose.
    if word_game.game_won:
        print("Congratulations, you guess is correct!")
    else:
         print("Womp womp, try again!")

# function to show the letters as the respective colors with each guess
def show_results(word_game: Word_game):
    print(f"\n You have {word_game.numbered_guesses} chances left\n")
    
    lines = []

    for word in word_game.guesses:
        result = word_game.tries(word)
        colored_results_str = letters_to_colors (result)
        lines.append(colored_results_str)
    
    for _ in range(word_game.numbered_guesses):
         lines.append("  ".join(["_"] * word_game.WORD_LEGNTH))

    box_border(lines)

# Function to convert letters into colors - green, yellow and white
def letters_to_colors (result: List[Responsiveness]):
    colored_results = []
    for character in result:
        if character.in_position:
            color = Back.GREEN
        elif character.in_word:
            color = Back.YELLOW
        else:
            color = Back.LIGHTWHITE_EX
        colored_character = color + character.letter + Back.RESET
        colored_results.append(colored_character)
    return "  ".join(colored_results)   

def box_border(lines: List[str], size:int=16, pad=2):

    content_length = size + pad * 2
    top_border = "┏" + "═" * content_length + "┓"
    bottom_border = "┗" + "═" * content_length + "┛"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("║" + space + line + space + "║")

    print(bottom_border)

if __name__ == "__main__":
    main()