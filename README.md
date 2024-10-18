# Number Guessing Game

This is a simple number guessing game written in Python. The player guesses a randomly generated number within a range they specify. The game provides feedback on each guess, indicating whether the guess is too high or too low.

## How to Play

1. Enter a range: The player is asked to provide a maximum number (positive integer) that will define the range for the game (from 0 to the number you specify).

2. Make guesses: The player keeps guessing until they find the correct number.

3. Feedback: The game tells the player if their guess is too high or too low.

4. Win: Once the player guesses the number correctly, the game congratulates them and displays the number of guesses it took.

## Prerequisites

. Python 3.x

## How to Run

1. Clone or download this repository.

2. Open a terminal/command prompt.

3. Navigate to the folder where the guessing_game.py script is located.

4. Run the script with the following command:

 bash
python guessing_game.py

5. Follow the prompts in the terminal to play the game.

## Features

. Dynamic range: The user can set a custom range by providing a maximum number.

. Input validation: The game ensures that the input is a valid positive integer, prompting the user to try again if the input is invalid.

. Feedback on guesses: The game gives hints on whether the guess was too high or too low.

. Guess count: The game keeps track of how many guesses were made.

## Sample Gameplay

less

Type a number: 50
Make a guess: 25
You are below the number
Make a guess: 40
You were above the number!
Make a guess: 35
You got it!
You got it in 3 guesses.

## Edge Cases
.The game will prompt you to enter a number if you enter a non-numeric value.

.The game will not accept zero or negative numbers for the range.

## License
This project is open-source and free to use for educational purposes.
