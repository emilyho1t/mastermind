import unittest
from unittest.mock import patch, MagicMock
from src.mastermind import Game

valid_input = "red green cyan blue"
invalid_input = "pink orange blue yellow"

class TestMastermindGame(unittest.TestCase):
    @patch.object(Game, '__init__', return_value=None)
    @patch.object(Game, 'validate_input')
    def test_valid_input(self, mock_validate_input, mock_init):
        mock_solution_generator = MagicMock()
        game = Game(mock_solution_generator)
        mock_validate_input.side_effect = [valid_input, None]

        result_valid_input = game.validate_input(valid_input)
        result_invalid_input = game.validate_input(invalid_input)

        self.assertEqual(result_valid_input, valid_input)
        self.assertIsNone(result_invalid_input)

    @patch.object(Game, '__init__', return_value=None)
    @patch.object(Game, 'validate_input')
    def test_invalid_input(self, mock_validate_input, mock_init):
        mock_solution_generator = MagicMock()
        game = Game(mock_solution_generator)

        mock_validate_input.side_effect = [None]
        result_invalid_input = game.validate_input(invalid_input)

        self.assertIsNone(result_invalid_input)

    @patch('builtins.input', side_effect=['q'])
    @patch.object(Game, 'play', return_value='finished')
    def test_quit_game(self, mock_play, mock_input):
        game = Game(solution_generator=MagicMock())
        result = game.play()

        self.assertEqual(result, "finished")


if __name__ == "__main__":
    unittest.main()


