from letter_response import Responsiveness
from colorama import Fore


class Word_game:

    # Game Play of the terminal application, a game where we have 8 attempts
    # for a 6 letter word
    MAXIMUM_GUESS = 8
    WORD_LEGNTH = 6

    def __init__(self, hidden_word: str):
        self.hidden_word: str = hidden_word.upper()
        self.guesses = []

    def guess(self, word: str):
        word = word.upper()
        self.guesses.append(word)

    def tries(self, word: str):
        result = []

        for index in range(self.WORD_LEGNTH):
            character = word[index]
            letter = Responsiveness(character)
            letter.in_word = character in self.hidden_word
            letter.in_position = character == self.hidden_word[index]
            result.append(letter)
        return result


    # Property function when the game has been won
    @property
    def game_won(self):
        return len(self.guesses) > 0 and self.guesses[-1] == self.hidden_word

    # Demonstrating how many guesses we have done, 1-8
    @property
    def numbered_guesses(self) -> int:
        return self.MAXIMUM_GUESS - len(self.guesses)

    # Demonstrating how many guesses can be continued to be done
    @property
    def ongoing_guesses(self):
        return self.numbered_guesses > 0 and not self.game_won
