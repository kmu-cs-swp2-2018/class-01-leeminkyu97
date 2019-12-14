import random


class Unit:
    def __init__(self):
        self.level = 0
        self.unit_class = ""
        self.hp_max = 0
        self.hp_current = 0
        self.mp_max = 0
        self.mp_current = 0
        self.str = 1
        self.skill = []

        self.gold = 0
        self.item = [0,0,0]

        self.place = ""     # 현재 위치 기억해서 placeWindow에 사용
        self.before = ""    # 이전 위치 기억해서 뒤로, 탈출에 사용

        self.enemyType = ""
        self.x = 0  # 던전에서의 플레이어의 현재 위치 (맵 그리기 등 이동에 필요)
        self.y = 0
        self.flag = False   # True일때만 이동가능하게해서 전투중에 이동 불가
        #self.quest_flag = False


class Village:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.npc = []
        self.linked_vil = []
        self.linked_dun = []


class Dungeon:
    def __init__(self):
        self.map = []
        self.monster = []
        self.boss = ""
        self.initX = 0
        self.initY = 0
