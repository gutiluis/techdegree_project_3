#!/usr/bin/env python3


# file: game.py
# descr:



import pdb
#pdb.set_trace()
from .phrase import Phrase
import random
import datetime
import shutil
import time
import logging
import sys


logger = logging.getLogger(__name__)


class Game:
    def __init__(self): # without instance attribute. does only behaviour 
        self.missed = 0
        # classes are not subscriptable
        self.phrases = [
            Phrase("ewe"),
            Phrase("sec"),
            Phrase("inst"),
            Phrase("min"),
            Phrase("hour"),
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = []

        
    def get_random_phrase(self):
        if not self.phrases:
            print("no")
            return None
        return random.choice(self.phrases)
    
    def welcome(self):
        after_wel = "=" * 70
        center = shutil.get_terminal_size().columns
        print(after_wel.center(center))
        welcome = "WElCOME PLAYER"
        center_welcome_message = shutil.get_terminal_size().columns
        print(welcome.center(center_welcome_message))
        after_wel = "=" * 70
        center = shutil.get_terminal_size().columns
        print(after_wel.center(center))

        
    def start(self):
        self.welcome() 
        
        
        '''
        Inside start call the `welcome()` method. 
        Add a print statement to print out “Number missed: “
        followed by `self.missed`, then call the `display()` 
        method on the `active_phrase` attribute. Don’t
        forget to pass in `self.guesses` to the `display()` 
        method.
        '''
        
        
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print("Number of guesses the users has had missed:", self.missed)

            self.active_phrase.display(self.guesses)

            user_guess = self.get_guess() # calls def get_guess(self):
            self.guesses.append(user_guess)

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            else:
                self.missed

        self.game_over() # calling a method on the current instance
       
        
        
    def get_guess(self):
        while True:
            guess = input("\nEnter a letter: ").lower()
            if len(guess) == 1 and True:
                return guess
            print("Invalid input. Please enter a gingle letter.")

#parameters are for outside input # missed instance attribute is inside the game already
    def game_over(self): # self is the instance itself of the function. also called argument
        if self.active_phrase.check_complete(self.guesses) and self.missed < 5:
            print("won")
            return "won"
        
        else:
            if self.missed == 5:
                print('lost')
                return "lost"
