class Life:
    def __init__(self):
        self.max_life = 6
        self.remaining_life = self.max_life

    def decrease(self):
        self.remaining_life -= 1

    def is_alive(self):
        return self.remaining_life > 0

    def display_life_state(self):
        return [
            '             ____\n\
            |    |\n\
            |\n\
            |\n\
            |\n\
            |\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|',
            '             ____\n\
            |    |\n\
            |    o\n\
            |\n\
            |\n\
            |\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|',
            '             ____\n\
            |    |\n\
            |    o\n\
            |    |\n\
            |    |\n\
            |\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|',
            '             ____\n\
            |    |\n\
            |    o\n\
            |   /|\n\
            |    |\n\
            |\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|',
            '             ____\n\
            |    |\n\
            |    o\n\
            |   /|\n\\n\\n\
            |    |\n\
            |\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|',
            '             ____\n\
            |    |\n\
            |    o\n\
            |   /|\n\\n\\n\
            |    |\n\
            |   /\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|',
            '             ____\n\
            |    |\n\
            |    o\n\
            |   /|\n\\n\\n\
            |    |\n\
            |   / \n\\n\\n\
           _|_\n\
          |   |______\n\
          |          |\n\
          |__________|'][self.max_life - self.remaining_life]


print(Life().display_life_state())