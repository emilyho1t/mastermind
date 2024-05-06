from abc import ABC, abstractmethod
import random
from colorama import Fore, Back

# colourful colours
colourDictionary = {
    "red": Fore.RED,
    "yellow": Fore.YELLOW,
    "green": Fore.GREEN,
    "cyan": Fore.CYAN,
    "blue": Fore.LIGHTBLUE_EX,
    "purple": Fore.LIGHTMAGENTA_EX,
}

# Define response and reset colours
blackText = Fore.LIGHTBLACK_EX + Back.RESET
whiteText = Fore.LIGHTWHITE_EX + Back.RESET
black = Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX
white = Fore.LIGHTBLACK_EX + Back.LIGHTWHITE_EX
reset = Fore.RESET + Back.RESET

blackResponse = f"{black} b {blackText}  black: right colour, right place"
whiteResponse = f"{white} w {whiteText}  white: right colour, wrong place"

instructionText = """
Mastermind Game Instructions: Try to guess the correct combination of colours. 

Guessing: Each combination consists of four colours from the list shown. (There can be multiple of the same colour!)
Guess Format: Input your guess as four colors separated by spaces. For example: "red green cyan blue".
Feedback: After each guess, you'll receive feedback in the form of black (b) and white (w) markers as shown.
Levels: You can choose what level you'd like to play at. You get 12 guesses at easy level, 10 at medium and 8 at hard.
To begin, enter your guess below as indicated, good luck!

At any time during the game:
    enter 'c' to see colours list
    enter 'i' to view instructions
    enter 'r' to see black and white response definitions
    enter 'q' to quit
"""

class SolutionGenerator(ABC):
    @abstractmethod
    def generate_solution(self):
        pass

class RandomSolutionGenerator(SolutionGenerator):
    def generate_solution(self):
        return random.sample(list(colourDictionary.keys()), 4)

class Game:
    def __init__(self, solution_generator):
        self.solution_generator = solution_generator

    def play(self):
        self.print_instructions()
        solution = self.solution_generator.generate_solution()
        mode = self.choose_difficulty()
        print("Try to guess the solution! You have a maximum of {} guesses.".format(mode))
        self.guess(solution, mode)

    def print_instructions(self):
        print(instructionText)
        print(blackResponse, "\t", whiteResponse, reset)
        self.colours()
        print(reset)

    def colours(self):
        print("You can use the following colours: ", end="")
        for colourName, colourCode in colourDictionary.items():
            print(colourCode, colourName, end=" ")
        print(reset)

    def choose_difficulty(self):
        valid_difficulties = {"easy": 12, "medium": 10, "hard": 8}
        while True:
            difficulty_level = input("Enter the difficulty level (easy/medium/hard): ").lower()
            if difficulty_level in valid_difficulties:
                return valid_difficulties[difficulty_level]
            else:
                print("Invalid difficulty level. Please choose from easy, medium, or hard.")

    def ending(self, guess_count):
        if guess_count == 1:
            return "1st"
        elif guess_count == 2:
            return "2nd"
        elif guess_count == 3:
            return "3rd"
        else:
            return str(guess_count) + "th"

    def validate_input(self, input_str):
        if input_str in ['q', 'c', 'i', 'r']:
            return input_str
        guess = input_str.lower().split()
        if all(colour.lower() in colourDictionary for colour in guess) and len(guess) == 4:
            return guess
        print("Invalid input. Please enter 4 valid colours from the list.")
        self.colours()
        return None

    def check_guess(self, guess, solution):
        black_matches = []
        white_matches = []

        for i in range(len(guess)):
            if guess[i] == solution[i]:
                black_matches.append(guess[i])

        for colour in guess:
            if colour in solution and colour not in black_matches and colour not in white_matches:
                white_matches.append(colour)

        return black_matches, white_matches

    def print_guesses(self, guesses):
        print("Previous guesses:")
        for i, (prev_guess, black_resp, white_resp) in enumerate(guesses, 1):
            print("Guess", i, ":", end=" ")
            for colour in prev_guess:
                print(colourDictionary[colour], colour, reset, end=" ")
            for _ in range(len(black_resp)):
                print(black, "b", reset, end=" ")
            for _ in range(len(white_resp)):
                print(white, "w", reset, end=" ")
            print(reset)

    def guess(self, solution, mode):
        guesses = []
        guess_count = 1

        while guess_count <= mode:
            print(reset, "Enter your", self.ending(guess_count), "guess ", end="")
            user_input = self.validate_input(input("(separate colours by spaces): "))
            if not user_input:
                continue

            if user_input == 'q':
                print("Quitting the game.")
                return "finished"
            elif user_input == 'c':
                self.colours()
                continue
            elif user_input == 'i':
                print(instructionText)
                print(blackResponse, whiteResponse)
                continue
            elif user_input == 'r':
                print(blackResponse, "\t", whiteResponse, reset)
                continue

            guess = user_input
            if guess == solution:
                print("Congratulations! You guessed the correct combination.")
                return "finished"

            black_matches, white_matches = self.check_guess(guess, solution)
            guesses.append((guess, black_matches, white_matches))
            self.print_guesses(guesses)
            guess_count += 1

        print("Sorry, you have used up all your guesses. The correct combination was:", end="")
        for colour in solution:
            print(colourDictionary[colour], colour, reset, end=" ")
        return "finished"


def main():
    solution_generator = RandomSolutionGenerator()
    game = Game(solution_generator)
    game.play()

if __name__ == "__main__":
    main()


