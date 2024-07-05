
from typing import List
from word_game import Word_game
from letter_response import Responsiveness
from colorama import Fore, Back, init
import random


def main():
    players = {}  # Dictionary to store player data

    while True:
        print("\nMenu:")
        print("1. Start New Game")
        print("2. Add Player")
        print("3. Scoreboard")
        print("4. Exit")
        choice = input("Make your selection: ")

        if choice == "1":
            print("\nStarting new game...\n")
            player_name = select_player(players)
            if player_name:
                game_introduction()  # Display game instructions after confirming new game
                # Pass players dictionary to play_game
                game_won = play_game(players, player_name)
                update_scoreboard(players, player_name, game_won)

        elif choice == "2":
            add_player(players)
        elif choice == "3":
            display_scoreboard(players)
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def add_player(players):
    player_name = input("Enter the name of the new player: ").strip()
    if player_name == "":
        print("Invalid player name. Please enter a valid name.")
        return

    if player_name in players:
        print(f"{player_name} already exists in the players list.")
    else:
        players[player_name] = {
            'score': 0,
            'game_won': 0,
            'games_lost': 0,
            'total_games': 0}
        print(f"{player_name} added to the players list.")


def select_player(players):
    if not players:
        print("No players found. Please add players first.")
        return None

    print("Select a player:")
    player_list = list(players.keys())
    for i, player in enumerate(player_list, start=1):
        print(f"{i}. {player}")

    player_choice = input("Enter the number of the player: ")
    try:
        player_index = int(player_choice) - 1
        if 0 <= player_index < len(player_list):
            player_name = player_list[player_index]
            return player_name
        else:
            print("Invalid player selection. Please enter a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def play_game(players, player_name):
    six_letter_set = six_letter_word_library("data/sixletterwords.txt")
    hidden_word = random.choice(list(six_letter_set))
    word_game = Word_game(hidden_word)

    while word_game.ongoing_guesses:
        x = input("\nGuess a word (type 'exit' to quit): ")

        if x.lower() == 'exit':
            print("Exiting the game. Goodbye!")
            return False  # Return game_won=False if player exits

        if len(x) != len(hidden_word):  # Check against the length of hidden_word
            print(
                Back.RED +
                f"Word must be {len(hidden_word)} characters long! " +
                Back.RESET)
            continue

        if x not in six_letter_set:
            print(Back.RED + f"{x} is not a valid option!" + Back.RESET)
            continue

        word_game.guess(x)
        show_results(word_game)

        if word_game.game_won:
            print("Congratulations, your guess is correct!")
            return True

    # If loop ends and game_won is not True, then player lost
    print("Womp womp, try again!")
    print(f"The hidden word was: {word_game.hidden_word}")
    return False  # Return game_won=False if player did not win


def game_introduction():
    print("Welcome to six-letter word game")
    print("Game Play:\nThe aim of the game is to guess the six letter word in the least amount of attempts - 8 being the final guess ")
    print(
        Back.GREEN +
        f"- Green: To display that the letter of the word that you have chosen is in the correct position. " +
        Back.RESET)
    print(
        Back.YELLOW +
        f"- Yellow: To display that the letter of the word that you have chosen is in the word, however not in the correct position. " +
        Back.RESET)
    print(
        Back.WHITE +
        f"- White: To display the letter is not in the word. " +
        Back.RESET)

    print(
        Back.RED +
        f"\nPlease play using CAPS LOCK on as all guesses are in uppercase. " +
        Back.RESET)


def show_results(word_game: Word_game):
    print(f"\n You have {word_game.numbered_guesses} chances left\n")

    lines = []

    for word in word_game.guesses:
        result = word_game.tries(word)
        colored_results_str = letters_to_colors(result)
        lines.append(colored_results_str)

    for _ in range(word_game.numbered_guesses):
        lines.append("    ".join([" _"] * len(word_game.hidden_word)))

    box_border(lines)


def display_scoreboard(players):
    if not players:
        print("No players found. Please add players first.")
        return

    # Sort scoreboard by score descending
    scoreboard_sorted = sorted(
        players.items(),
        key=lambda x: x[1]['game_won'],
        reverse=True)

    # Display scoreboard
    print("\nScoreboard:")
    print(
        Back.LIGHTBLACK_EX + 
        "{:<15} {:<10} {:<10} {:<10}".format(
            "Player",
            "Games Won",
            "Games Lost",
            "Win %     " + Back.RESET))
    print("-" * 45)
    for player, data in scoreboard_sorted:
        games_won = data['game_won']
        games_lost = data['games_lost']
        total_games = data['total_games']
        win_percent = (games_won / total_games) * 100 if total_games > 0 else 0
        print(
            Back.BLUE +
            "{:<15} {:<10} {:<10} {:<10.2f}".format(
                player,
                games_won,
                games_lost,
                win_percent) +
            Back.RESET)


def update_scoreboard(players, player_name, game_won):
    if player_name not in players:
        # Initialize the player if not exists
        players[player_name] = {
            'game_won': 0,
            'games_lost': 0,
            'total_games': 0}
    elif 'games_lost' not in players[player_name]:
        # Ensure games_lost is initialized if missing
        players[player_name]['games_lost'] = 0

    if game_won:
        players[player_name]['game_won'] += 1
    else:
        players[player_name]['games_lost'] += 1

    players[player_name]['total_games'] += 1

    print(
        f"Updating scoreboard for {player_name}: {'Won' if game_won else 'Lost'}")


def six_letter_word_library(path: str):
    six_letter_set = set()
    try:
        with open(path, "r") as f:
            for line in f.readlines():
                word = line.strip().upper()
                if len(word) == 6:  # Ensure words are exactly six letters long
                    six_letter_set.add(word)
                else:
                    print(
                        f"Ignoring word: {word}. Only six-letter words are allowed.")
    except FileNotFoundError:
        print(f"File not found: {path}")
    return six_letter_set


def letters_to_colors(result: List[Responsiveness]):
    colored_results = []
    for character in result:
        if character.in_position:
            color = Back.GREEN + " "
        elif character.in_word:
            color = Back.YELLOW + " "
        else:
            color = Back.LIGHTWHITE_EX + " "
        colored_character = color + character.letter + Back.RESET
        colored_results.append(colored_character)
    return "    ".join(colored_results)


def box_border(lines: List[str], size: int = 29, pad=3):
    content_length = size + pad * 3
    top_border = Fore.MAGENTA + "┏" + "═" * content_length + "┓" + Fore.RESET
    bottom_border = Fore.MAGENTA + "┗" + "═" * content_length + "┛" + Fore.RESET
    space = " " * pad
    print(top_border)

    for line in lines:
        print(Fore.MAGENTA + "║" + space + line + space + "║" + Fore.RESET)

    print(bottom_border)


if __name__ == "__main__":
    main()
