from phrasehunter.game import Game
from phrasehunter.phrase import Phrase


if __name__ == "__main__":
    phrase = Phrase()
# Inside Dunder Main:
# Create an instance of your Game class
    game = Game()
#    print(phrase)
 #   print(game)


    for phrase in game.phrases:
        print(phrase.phrase)


# Start your game by calling the instance method that starts the game loop
# create_instance.start()
#    def print_phrase(phrase_object):
#        print(f"The phrase is: {phrase_object.phrase}")

#    game = Game()
#    print_phrase(game.get_random_phrase())
#    print_phrase(game.get_random_phrase())
#    print_phrase(game.get_random_phrase())
#    print_phrase(game.get_random_phrase())
#    print_phrase(game.get_random_phrase())
