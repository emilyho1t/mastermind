import unittest
from unittest.mock import MagicMock
from src.mastermind import Game

class FakeSolutionGenerator:
    def generate_solution(self):
        return ['red', 'green', 'blue', 'yellow']

class TestGame(unittest.TestCase):
    def test_play_game(self):
        mock_input = MagicMock(side_effect=['easy', 'q'])
        game = Game(FakeSolutionGenerator())
        with unittest.mock.patch('builtins.input', mock_input):
            result = game.play()

        self.assertIsNone(result)

    def test_check_guess_correct(self):
        fake_solution_generator = FakeSolutionGenerator()
        game = Game(fake_solution_generator)

        solution = ['red', 'green', 'blue', 'yellow']
        guess = ['red', 'green', 'blue', 'yellow']
        black_matches, white_matches = game.check_guess(guess, solution)
        self.assertCountEqual(black_matches, guess)
        self.assertCountEqual(white_matches, [])

    def test_check_guess_no_matches(self):
        fake_solution_generator = FakeSolutionGenerator()
        game = Game(fake_solution_generator)

        solution = ['red', 'green', 'blue', 'yellow']
        guess = ['purple', 'orange', 'cyan', 'pink']
        black_matches, white_matches = game.check_guess(guess, solution)
        self.assertCountEqual(black_matches, [])
        self.assertCountEqual(white_matches, [])

    def test_check_guess_partial_matches(self):
        fake_solution_generator = FakeSolutionGenerator()
        game = Game(fake_solution_generator)

        solution = ['red', 'green', 'blue', 'yellow']
        guess = ['red', 'orange', 'blue', 'purple']
        black_matches, white_matches = game.check_guess(guess, solution)
        self.assertCountEqual(black_matches, ['red', 'blue'])
        self.assertCountEqual(white_matches, [])

    def test_check_guess_mixed_matches(self):
        fake_solution_generator = FakeSolutionGenerator()
        game = Game(fake_solution_generator)

        solution = ['red', 'green', 'blue', 'yellow']
        guess = ['green', 'blue', 'red', 'orange']
        black_matches, white_matches = game.check_guess(guess, solution)
        self.assertCountEqual(black_matches, [])
        self.assertCountEqual(white_matches, ['green', 'blue', 'red'])

if __name__ == "__main__":
    unittest.main()
