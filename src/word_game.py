class Word_game:

    MAXIMUM_GUESS = 8
    WORD_LEGNTH = 6

    def __init__(self, hidden_word: str):
        self.hidden_word: str = hidden_word
        self.guesses = []
        pass

    def guess(self, word: str):
        self.guesses.append(word)

    @property
    def game_won(self):
        return len(self.guesses) > 0 and self.guesses[-1] == self.hidden_word
    
    @property
    def numbered_guesses(self) -> int:
        return self.MAXIMUM_GUESS - len(self.guesses)

    @property
    def ongoing_guesses(self):
        return self.numbered_guesses > 0 and not self.game_won