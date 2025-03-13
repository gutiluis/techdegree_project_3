from phrasehunter.game import Game
# from phrasehunter.phrase import Phrase


if __name__ == "__main__":
#    phrase = Phrase()
# Inside Dunder Main:
# Create an instance of your Game class
    game = Game()

    for phrase in game.phrases:
        print(phrase.phrase)

# Start your game by calling the instance method that starts the game loop
# create_instance.start()
