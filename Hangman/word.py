import random


class Word:
    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)
        self.word = self.words[random.randrange(self.count)]
        self.guessed_characters = set()
        self.current_status = len(self.word) * '_'

    def get_word(self):
        return self.word

    def get_guessed_characters(self):
        return self.guessed_characters

    def guess(self, character):
        self.guessed_characters.add(character)

        matched_indexes = [i for i, e in enumerate(
            self.word) if e == character]

        if len(matched_indexes) == 0:
            return -1

        current_status = list(self.current_status)
        for i in matched_indexes:
            current_status[i] = character
        self.current_status = ''.join(current_status)

        if self.current_status == self.word:
            return 1