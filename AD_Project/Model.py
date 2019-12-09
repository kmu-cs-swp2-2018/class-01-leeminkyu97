import random


class Unit:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.unit_class = 0
        self.hp_max = 0
        self.hp_current = 0
        self.mp_max = 0
        self.mp_current = 0
        self.str = 0
        self.int = 0
        self.gold = 0
        self.item = {}
        self.skill = []
        self.place = ""
        self.before = ""

    def setting(self, name="", level=0, unit_class="", hp_max=0, hp_current=0, mp_max=0, mp_current=0, str=0, int=0, gold=0, item={}, skill=[], place="", before=""):
        self.name = name
        self.level = level
        self.unit_class = unit_class
        self.hp_max = hp_max
        self.hp_current = hp_current
        self.mp_max = mp_max
        self.mp_current = mp_current
        self.str = str
        self.int = int
        self.gold = gold
        self.item = item
        self.skill = skill
        self.place = place
        self.before = before


class Village:
    def __init__(self):
        self.name = ""
        self.linked = []

    def setting(self, name="", linked=[]):
        self.name = name
        self.linked = linked


class Dungeon:
    def __init__(self):
        self.name = ""
        self.monster = []
        self.boss = ""

    def setting(self, name="", monster=[], boss=""):
        self.name = name
        self.monster = monster
        self.boss = boss
