class Guess:

    def __init__(self, word):
        self.word = word  # 원래 주어진 코드는 secretWord로 따로 관리하는데 이를 word로 통일
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = "_" * len(self.word)


    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", self.numTries)


    def guess(self, character):
        self.guessedChars.append(character)

        idx = self.word.find(character)
        if idx == -1:
            self.numTries += 1
            return False

        temp_currentStatus = ""
        for i in range(0, len(self.currentStatus)):
            if character != self.word[i]:
                temp_currentStatus += self.currentStatus[i]
            else:
                temp_currentStatus += character
        self.currentStatus = temp_currentStatus

        for i in range(0, len(self.currentStatus)):
            if self.currentStatus[i] != self.word[i]:
                return False

        return True
