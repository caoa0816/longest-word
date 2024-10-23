import random
import string


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False

        random_grid = self.grid
        for letter in word:
            if letter.upper() in random_grid:
                continue
            else:
                return False
        return True
