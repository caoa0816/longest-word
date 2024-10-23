from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):

            new_game = Game()
            grid = new_game.grid
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_empty_word(self):
        game= Game()
        test_grid = list("OQUWRBAZE")
        game.grid = test_grid
        assert game.grid == test_grid
        test_word_one = ""
        assert game.is_valid(test_word_one.upper()) is False

    def test_word_validity(self):

        game= Game()
        test_grid = list("OQUWRBAZE")
        game.grid = test_grid
        assert game.grid == test_grid

        #edge case 1: not all letters within a word are in the grid
        test_word_two = "samantha"
        assert game.is_valid(test_word_two.upper()) is False

        #edge case 2: all letters within the word are in the grid
        test_word_three = "baroque"
        test_word_four = "bower"
        assert game.is_valid(test_word_three.upper()) is True
        assert game.is_valid(test_word_four.upper()) is True

    def test_unknown_word_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW')
        assert new_game.is_valid('FEUN') is False
