from hangman import Hangman

class Guess:
    def __init__(self, word):
        self.word = word  # 원래 주어진 코드는 secretWord로 따로 관리하는데 이를 word로 통일
        self.numOfTries = 0
        self.guessedChars = set()
        self.currentStatus = "_" * len(self.word)

    def display(self):
        hangman = Hangman()
        life = hangman.getLife()

        print("Current:", self.currentStatus)
        print("Tries:", self.numOfTries)
        print("Life:", life - self.numOfTries)

    def guess(self, character):
        self.guessedChars.add(character)

        matchedIndexes = [i for i, e in enumerate(self.word) if e == character]
        if len(matchedIndexes) == 0:
            self.numOfTries += 1
            return False

        self.currentStatus = list(self.currentStatus)
        for i in matchedIndexes:
            self.currentStatus[i] = character
        self.currentStatus = ''.join(self.currentStatus)

        if self.currentStatus == self.word:
            return True
        else:
            return False