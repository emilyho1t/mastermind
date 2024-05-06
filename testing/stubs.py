from unittest.mock import MagicMock
import unittest
from src.mastermind import Game, RandomSolutionGenerator

mode = 2

class StubGame(Game):
    def __init__(self, solution, mode):
        super().__init__(RandomSolutionGenerator())
        self.solution = solution
        self.guess_count = 1
        self.mode = mode

    def guess(self, solution):
        self.guess_count += 1

        if solution == self.solution:
            return "finished"

        if self.guess_count > self.mode:
            return "finished"

        return "ongoing"



class TestStubbedGame(unittest.TestCase):
    def test_guess_correct_solution(self):
        correct_solution = ["red", "green", "blue", "yellow"]
        game = StubGame(correct_solution, mode)

        game.validate_input = MagicMock(return_value=["red", "green", "blue", "yellow"])
        guess_count = game.guess(["red", "green", "blue", "yellow"])

        self.assertEqual(guess_count, "finished")

    def test_guess_incorrect_solution(self):
        correct_solution = ["red", "green", "blue", "yellow"]
        game = StubGame(correct_solution, mode)

        game.validate_input = MagicMock(return_value=["red", "green", "blue", "red"])
        guess_count = game.guess(["red", "green", "blue", "red"])

        self.assertEqual(guess_count, "ongoing")

    def test_guess_finishes_when_guess_count_exceeds_mode_with_incorrect_guess(self):
        correct_solution = ["red", "green", "blue", "yellow"]

        game = StubGame(correct_solution, mode)
        game.validate_input = MagicMock(return_value=["red", "green", "blue", "red"])

        guess_count = game.guess(["red", "green", "blue", "red"])
        guess_count = game.guess(["red", "green", "blue", "red"])
        guess_count = game.guess(["red", "green", "blue", "red"])

        self.assertEqual(guess_count, "finished")


if __name__ == "__main__":
    unittest.main()
