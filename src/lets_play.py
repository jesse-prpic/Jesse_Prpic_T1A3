from word_game import Word_game

def main():
    print("Welcome to Word Game!")
    word_game = Word_game("APPLES")

    while word_game.ongoing_guesses:
            x = input("Guess a word: ")
            word_game.guess(x)

    if word_game.game_won:
        print("Congratulations, you guess is correct!")
    else:
         print("Womp womp, try again!")

if __name__ == "__main__":
    main()