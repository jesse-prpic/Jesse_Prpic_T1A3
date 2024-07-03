from word_game import Word_game

# Defining the game play and outputs of the players guesses
def main():
    print("Welcome to Word Game!")
    word_game = Word_game("APPLES")

    while word_game.ongoing_guesses:
            x = input("Guess a word: ")
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