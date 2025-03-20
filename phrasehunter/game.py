from phrasehunter.phrase import Phrase
import random



class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def create_phrases(self):
        phrases = [Phrase("Cat in the hat"), Phrase("The early bird gets the worm"), Phrase("The unexamined life is not worth living"), Phrase("You must be the change you wish to see in the world"), Phrase("Look deep into nature, and then you will understand everything better")]
        return phrases

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("WELCOME TO PHRASE HUNTER CHALLENGE!.")

    def start(self):
        self.welcome()

        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)

            user_guess = self.get_guess()
#        print(f"Enter a letter: {user_guess}")
            self.guesses.append(user_guess)
#        self.active_phrase.display(self.guesses)

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()
#            print("YAY")
#       else:
#            print("Bummer!")

    def get_guess(self):
        guess = input("Guess a letter: ")
        return guess

    def game_over(self):
        if self.missed == 5:
            print("Game lost!")
        else:
            print("You won!")


