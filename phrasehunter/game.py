class Game:
    def __init__(self):
# track the number of missed guesses by the player
# initial value is 0
# 0 is no guesses at the start of the game
        self.missed = 0
        self.phrases = self.create_phrases()
   #     currently in play
        self.active_phrase = None
# list with all guesses
# list with a string for a space
        self.guesses = [" "]

    def create_phrases(self):
        return ["one value", "two values", "three", "four", "five"]


    #def start(self):
    # property set to the phrase object returned from a call to the get_random_phrase()
    #    self.active_phrase

    #def get_random_phrase(self):


    #def welcome(self):
     #   print("Welcome message user!")

    # get the guess from the user and record it in the guess attribute
   # def get_guess(self):
    #    self.guesses = guesses

   # def game_over(self):
    #    print("win or loss")


# the game instance can be responsible for starting the game loop:
# getting player's input()
# guesses to pass to a phrase object to perform its responsabilities against, 
# determining if a win/ loss happens after the player run out of turns
# phrase is completely guessed
