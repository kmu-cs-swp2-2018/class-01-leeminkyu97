import random


class Unit:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.unit_class = 0
        self.hp = 0
        self.mp = 0
        self.gold = 0
        self.item = {}
        self.skill = []
        self.place = ""

    def setting(self, name="", level=0, unit_class="", hp=0, mp=0, gold=0, item={}, skill=[], place=""):
        self.name = name
        self.level = level
        self.unit_class = unit_class
        self.hp = hp
        self.mp = mp
        self.gold = gold
        self.item = item
        self.skill = skill
        self.place = place
