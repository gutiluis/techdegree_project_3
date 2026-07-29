#!/usr/bin/env python


# file: phrase.py
# descr:



import logging


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses or letter == " ":
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
        print()

    logging.debug('check_ if user guess got the letter not whole phrase correct')
    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        return False

    logging.debug('retun check_complete all letters in phrase')
    def check_complete(self, guesses): # guesses is any variable paramenter argument name
        for all_letters in self.phrase:
            if all_letters not in guesses:
                return False
        return True