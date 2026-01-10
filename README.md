## How it works:

To run within the terminal:
- python3 app.py

Create a word guessing game: "Phrase Hunter." Using Python and OOP (Object-Oriented Programming) to select a phrase at random, hidden from the player. 
A player tries to guess the phrase by inputting individual characters within a determined amount of attempts.


This game will be entirely console/terminal based.
The player’s goal is to guess all the letters in a hidden, random phrase. A phrase is a group of words.
At the beginning of the game, the player only sees the number of letters and words in the phrase, represented by an underscore character _ as a placeholder on the screen for a given letter for that phrase.
The player inputs a guess for a letter in the phrase.
Once a correct letter is guessed, a player cannot guess that letter again.
If the guessed letter is in the phrase at least once, the phrase will replace all positions showing the underscore _ with the appropriate letter. All occurrences of that letter are made visible (so if there are 3 A's, all of the A's in the phrase appear at once).
If the selected letter is not in the phrase, the number missed increases by one.
The player keeps choosing letters until they reveal all the letters in the phrase, or until they make five incorrect guesses.

A random phrase will be selected and displayed with underscores for each letter.
Guess letters one at a time.
Correct guesses reveal the letter in the phrase.
Incorrect guesses increase the "missed" counter.
The game ends when:
   - All letters are guessed correctly → **You win!**
   - Five incorrect guesses are made → **You lose!**


## Classes

### `Phrase`

Handles the phrase logic.

## Attributes ##
- phrase: the phrase string (lowercase)
- guessed_letters: list of letters already guessed correctly

## Methods ##
- display(): returns the phrase with underscores for unguessed letters
- check_guess(guess): returns `True` if the letter is in the phrase
- add_guess(guess): adds the guessed letter to the list
- is_complete(): returns `True` if all letters have been guessed


Manages the game loop and player interactions.

## Attributes ##
- phrases: a list of Phrase objects
- active_phrase: the current Phrase being guessed
- missed: number of incorrect guesses

-----

#####

## Features:

- Randomly selects a phrase from a predefined list.
- Displays each letter as an underscore `_` until it is guessed.
- Tracks correct and incorrect guesses.
- Reveals all occurrences of a correctly guessed letter.
- Limits the number of incorrect guesses to 5.
- Console/terminal-based gameplay.
- start(): begins the game
- get_guess(): prompts the player for a letter
- handle_guess(guess): updates game state based on the guess
- check_complete(): checks if the phrase has been completely guessed
- game_over(): displays win/loss message

-----

#####

## Technologies Used:

- Python

-----

###

## Skills Learned:

- importing modules

-----

#####

Clone repo:

```bash
git clone https://github.com/gutiluis/Techdegree-project-3.git
```
