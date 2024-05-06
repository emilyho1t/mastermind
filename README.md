You may need to install colorama in order to run this program

installing colorama
/opt/homebrew/bin/python3.10 -m pip install --user --force-reinstall colorama

I have created doubling mocks, stubs and fakes to test my mastermind.py file which contains the main game. 

Mocks:
    test_valid_input
        tests whether the validate_input method of the Game class behaves correctly when given valid and invalid inputs
    test_invalid_input
        tests if the validate_input method of the Game class behaves correctly when given an invalid input
    test_quit_game
        tests for a scenario where a player quits the game by entering 'q', ensuring that the play method of the Game class returns 'finished'


Stubs:
    test_guess_correct_solution
        tests if a game correctly recognises that the player has guessed the solution correctly, ending the game when the guessed colours match the correct sequence
    test_guess_incorrect_solution
        tests if the game continues when the player's guessed solution does not match the correct sequence of colours, indicating that the game is still in progress
    test_guess_finishes_when_guess_count_exceeds_mode_with_incorrect_guess
        tests if the game finishes when the number of guesses exceeds a certain mode, even if the guessed solution is incorrect


Fakes:
    test_play_game
        simulates playing a game, providing the inputs 'easy' and 'q' to the game, and verifies that the game's play method returns None
    test_check_guess_correct
        checks if the check_guess method of the game correctly identifies all black matchesand no white matches when the guess matches the solution exactly
    test_check_guess_no_matches
        checks if the check_guess method of the game correctly identifies that there are no black or white matches when the guess does not match the solution at all
    test_check_guess_partial_matches
        checks if the check_guess method of the game correctly identifies partial matches when some of the colours in the guess match the solution in the correct positions, but not all of them (some black, some white)
    test_check_guess_mixed_matches
        checks if the check_guess method of the game correctly identifies mixed matches (correct colours in incorrect positions) when some of the colours in the guess match the solution but are in the wrong positions
