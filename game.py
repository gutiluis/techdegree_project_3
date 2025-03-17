from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = None
        self.guesses = [" "]

    def create_phrases(self):
        Phrase = ["one phrase", "second phrase", "third phrase", "fourth phrase", "fifth phrase"]
        return

