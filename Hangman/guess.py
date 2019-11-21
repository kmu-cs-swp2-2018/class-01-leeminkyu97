class Guess:

    def __init__(self, word):
        self.word = word
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = ""
        self.currentStatus = "_" * len(self.word)
        pass


    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", self.numTries)


    def guess(self, character):
        self.guessedChars.append(character)

        flag = self.word.find(character)
        if flag == -1:
            self.numTries += 1
            return False

        self.currentStatus[flag] = character
        return True
