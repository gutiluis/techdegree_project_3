word guessing game
select a phrase at random
input individual characters


Flow of the Game

Using Python, you’ll create two Python classes with specific attributes and methods. You'll create a Game class for managing the game, and a Phrase class to help with storing attributes of a phrase with specific methods to help determine how to display the phrase in the game.

Your code will choose a random phrase and use some logic you will implement to display each letter of the phrase as underscore character placeholders, _.

Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase. If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose).

If the player completes the phrase before they run out of guesses, a winning screen appears. If the player guesses incorrectly five times, a losing screen appears.



Understand the rules of the game:

This game will be entirely console/terminal based.

The player’s goal is to guess all the letters in a hidden, random phrase. A phrase is a group of words.

At the beginning of the game, the player only sees the number of letters and words in the phrase, represented by an underscore character _ as a placeholder on the screen for a given letter for that phrase.

The player inputs a guess for a letter in the phrase.

Once a correct letter is guessed, a player cannot guess that letter again.

If the guessed letter is in the phrase at least once, the phrase will replace all positions showing the underscore _ with the appropriate letter. All occurrences of that letter are made visible (so if there are 3 A's, all of the A's in the phrase appear at once).

If the selected letter is not in the phrase, the number missed increases by one.

The player keeps choosing letters until they reveal all the letters in the phrase, or until they make five incorrect guesses.
