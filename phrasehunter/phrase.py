class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses or letter == " ":
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def check_guess(self, user_guess):
        return user_guess in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses and letter != " ":
                return False
        return True
