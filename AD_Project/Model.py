import random


class Unit:
    def __init__(self):
        self.level = 0
        self.unit_class = 0
        self.hp_max = 0
        self.hp_current = 0
        self.mp_max = 0
        self.mp_current = 0
        self.gold = 0
        self.item = {}
        self.skill = []
        self.place = ""
        self.before = ""
        self.x = 0
        self.y = 0

    def setting(self, level=0, unit_class="", hp_max=0, hp_current=0, mp_max=0, mp_current=0,
                gold=0, item={}, skill=[], place="", before="", x=0,y=0):
        self.level = level
        self.unit_class = unit_class
        self.hp_max = hp_max
        self.hp_current = hp_current
        self.mp_max = mp_max
        self.mp_current = mp_current
        self.gold = gold
        self.item = item
        self.skill = skill
        self.place = place
        self.before = before
        self.x = x
        self.y = y


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
        self.map = []
        self.boss = ""

    def setting(self, name="", monster=[], boss="", map=[]):
        self.name = name
        self.monster = monster
        self.boss = boss
        self.map = map

    def map_modify(self, x, y):
        pass