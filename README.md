## How it works:

To run within the terminal:
- python3 app.py
2. A random phrase will be selected and displayed with underscores for each letter.
3. Guess letters one at a time.
4. Correct guesses reveal the letter in the phrase.
5. Incorrect guesses increase the "missed" counter.
6. The game ends when:
   - All letters are guessed correctly → **You win!**
   - Five incorrect guesses are made → **You lose!**


A console-based word guessing game written in Python. The player tries to guess a hidden phrase by selecting letters. The game continues until the player either guesses all the letters in the phrase (wins) or makes five incorrect guesses (loses).

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
