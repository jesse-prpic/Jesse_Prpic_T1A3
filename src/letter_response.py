# How the game is responsive between correct letters or correct
# positioning of those letters
class Responsiveness:
    def __init__(self, letter: str):
        self.letter: str = letter
        self.in_word: bool = False
        self.in_position: bool = False

    # Representation of how the letters should work in each guess, whether the
    # letter is in position or in the word - or false otherwise
    def __repr__(self):
        return f"[{self.letter} in_word:{self.in_word} in_position:{self.in_position}]"
