from src.LogIn import LogIn
from mastermind import Game, RandomSolutionGenerator

class Main:
    def main():
        log_in = LogIn()
        log_in.log_in()
        # After logging in, initiate the game
        solution_generator = RandomSolutionGenerator()  # Instantiate the strategy object
        game = Game(solution_generator)  # Inject the strategy into the context
        game.play()

if __name__ == '__main__':
    Main.main()
