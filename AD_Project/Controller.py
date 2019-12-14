import sys
from UI import MainUI
from Model import Unit, Village, Dungeon
import MapData
import random


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QApplication, QWidget


class Controller:
    def __init__(self):
        self.UI = MainUI()
        self.UI.moveButton_1.clicked.connect(self.event_moveButton1)
        self.UI.moveButton_2.clicked.connect(self.event_moveButton2)
        self.UI.moveButton_3.clicked.connect(self.event_moveButton3)
        self.UI.moveButton_4.clicked.connect(self.event_moveButton4)
        self.UI.actionButton_1.clicked.connect(self.event_actionButton1)
        self.UI.actionButton_2.clicked.connect(self.event_actionButton2)
        self.UI.actionButton_3.clicked.connect(self.event_actionButton3)
        self.UI.actionButton_4.clicked.connect(self.event_actionButton4)

        self.player = Unit()
        self.player.place="메인 화면"

        self.v1 = Village()
        self.v1.name="마을1"
        self.v1.linked_vil=["마을2", "마을3"]
        self.v1.linked_dun=["던전1-1","던전1-2","던전1-3"]
        self.v1.npc = ["npc1", "npc2", "npc3"]

        self.v2 = Village()
        self.v2.name="마을2"
        self.v2.linked_vil = ["마을1", "마을3"]
        self.v2.linked_dun = ["던전2-1", "던전2-2", "던전2-3"]
        self.v2.npc = ["npc4", "npc5", "npc6"]

        self.v3 = Village()
        self.v3.name="마을3"
        self.v3.linked_vil = ["마을1", "마을2"]
        self.v3.linked_dun = ["던전3-1", "던전3-2", "던전3-3"]
        self.v3.npc = ["npc7", "npc8", "npc9"]

        self.d11 = Dungeon()
        self.d11.map = MapData.maps[0]
        self.d11.monster = ['a11','b11']
        self.d11.boss = "boss11"
        self.d11.initX = 3
        self.d11.initY = 3

        self.d12 = Dungeon()
        self.d12.map = MapData.maps[1]
        self.d12.monster = ['a12', 'b12']
        self.d12.boss = "boss12"
        self.d12.initX = 3
        self.d12.initY = 3

        self.d13 = Dungeon()
        self.d13.map = MapData.maps[2]
        self.d13.monster = ['a13', 'b13']
        self.d13.boss = "boss13"
        self.d13.initX = 3
        self.d13.initY = 3

        self.d21 = Dungeon()
        self.d21.map = MapData.maps[3]
        self.d21.monster = ['a21', 'b21']
        self.d21.boss = "boss21"
        self.d21.initX = 3
        self.d21.initY = 3

        self.d22 = Dungeon()
        self.d22.map = MapData.maps[4]
        self.d22.monster = ['a22', 'b22']
        self.d22.boss = "boss22"
        self.d22.initX = 3
        self.d22.initY = 3

        self.d23 = Dungeon()
        self.d23.map = MapData.maps[5]
        self.d23.monster = ['a23', 'b23']
        self.d23.boss = "boss23"
        self.d23.initX = 3
        self.d23.initY = 3

        self.d31 = Dungeon()
        self.d31.map = MapData.maps[6]
        self.d31.monster = ['a31', 'b31']
        self.d31.boss = "boss31"
        self.d31.initX = 3
        self.d31.initY = 3

        self.d32 = Dungeon()
        self.d32.map = MapData.maps[7]
        self.d32.monster = ['a32', 'b32']
        self.d32.boss = "boss32"
        self.d32.initX = 3
        self.d32.initY = 3

        self.d33 = Dungeon()
        self.d33.map = MapData.maps[8]
        self.d33.monster = ['a33', 'b33']
        self.d33.boss = "boss33"
        self.d33.initX = 3
        self.d33.initY = 3

        self.dun = Dungeon()  #현재 던전
        self.mon = Unit()  #현재 몬스터

    # game start
    def start(self, app):
        self.UI.screen_main()
        self.UI.show()
        sys.exit(app.exec_())

    # back control
    def back(self):
        if self.player.before == "메인 화면":
            self.player.place=self.player.before
            self.UI.screen_main()
        elif "마을" in self.player.before:
            self.player.place=self.player.before
            self.UI.screen_village_square(self.player.before)

    # attack
    def attack(self, str):
        damage = str
        return damage

    # 직업 1
    def job1(self):
        self.player.level = 1
        self.player.unit_class = "직업1"
        self.player.hp_max = 100
        self.player.hp_current = 100
        self.player.mp_max = 100
        self.player.mp_current = 100
        self.player.gold = 50
        self.player.str = 10

    # move button_1 event
    def event_moveButton1(self):
        mb1 = self.UI.moveButton_1

        x = self.player.x
        y = self.player.y

        if not ("던전" in self.player.place):
            return
        if x == 0:
            return
        if self.player.flag == False:
            return

        if self.dun.map[x-1][y] == 1:   # 몬스터
            self.player.flag = False
            self.player.place = "던전몬스터"
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            self.mon.hp_current=100
            self.mon.mp_current=100
            self.UI.screen_dungeon_monster(self.mon.hp_current, self.mon.mp_current)

        if self.dun.map[x-1][y] == 3:   # 이미 깬 길
            self.player.flag = True
            self.dun.map[x][y] = 3
            self.dun.map[x - 1][y] = 2
            self.player.x = x - 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move()

        if self.dun.map[x-1][y] == 4:   # 보물상자
            self.player.flag = True
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_box()

        if self.dun.map[x-1][y] == 5:   # 보스
            self.player.flag = False
            self.player.place = "던전보스"
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            self.mon.hp_current=100
            self.mon.mp_current=100
            self.UI.screen_dungeon_boss()


    # move button_2 event
    def event_moveButton2(self):
        mb2 = self.UI.moveButton_2

    # move button_3 event
    def event_moveButton3(self):
        mb3 = self.UI.moveButton_3

    # move button_4 event
    def event_moveButton4(self):
        mb4 = self.UI.moveButton_4



    # action button_1 event
    def event_actionButton1(self):
        ab1 = self.UI.actionButton_1

        if ab1.text() == "New Game":
            self.player.place = "마을1"
            self.UI.text_load("Prolog.txt")
        elif ab1.text() == "Next":
            self.UI.text_next()
        elif ab1.text() == "Continue":
            self.UI.text_end()
        elif ab1.text() == "직업1":
            self.job1()
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.UI.screen_village_square(self.player.place)
        elif ab1.text() == "상점":
            self.player.before=self.player.place
            self.UI.screen_village_shop()
        elif ab1.text() == "마을1":
            self.player.place = "마을1"
            self.UI.screen_village_square(self.player.place)
        elif ab1.text() == "마을2":
            self.player.place = "마을2"
            self.UI.screen_village_square(self.player.place)
        elif ab1.text() == "마을3":
            self.player.place = "마을3"
            self.UI.screen_village_square(self.player.place)
        elif ab1.text() == "던전1-1":
            self.player.before = self.player.place
            self.player.place = "던전1-1"
            self.dun.map = self.d11.map
            self.dun.monster = self.d11.monster
            self.dun.boss = self.d11.boss
            self.player.x = self.d11.initX
            self.player.y = self.d11.initY
            self.UI.screen_dungeon_start()
        elif ab1.text() == "공격":
            if "몬스터" in self.player.place:
                self.mon.hp_current -= self.attack(10)
                self.UI.screen_dungeon_monster(self.mon.hp_current, self.mon.mp_current)
                if self.mon.hp_current <= 0:    # 몬스터의 체력이 0 이하이면 이동 화면
                    self.player.flag=True
                    self.UI.screen_dungeon_move()
            elif "보스" in self.player.place:
                self.mon.hp_current -= self.attack(10)
                self.UI.screen_dungeon_boss_battle(self.mon.hp_current, self.mon.mp_current)
                if self.mon.hp_current <= 0:  # 몬스터의 체력이 0 이하이면 이동 화면
                    self.UI.screen_dungeon_clear()


    # action button_2 event
    def event_actionButton2(self):
        ab2 = self.UI.actionButton_2

        if ab2.text() == "Skip":
            self.UI.text_end()
        elif ab2.text() == "How To Play":
            self.player.before=self.player.place
            self.UI.screen_howtoplay()
        elif ab2.text() == "대화":
            self.player.before = self.player.place
            if self.player.place == "마을1":
                self.UI.screen_village_npc(self.v1.npc)
            elif self.player.place == "마을2":
                self.UI.screen_village_npc(self.v2.npc)
            elif self.player.place == "마을3":
                self.UI.screen_village_npc(self.v3.npc)
        elif ab2.text() == "마을1":
            self.player.place = "마을1"
            self.UI.screen_village_square(self.player.place)
        elif ab2.text() == "마을2":
            self.player.place = "마을2"
            self.UI.screen_village_square(self.player.place)
        elif ab2.text() == "마을3":
            self.player.place = "마을3"
            self.UI.screen_village_square(self.player.place)



    # action button_3 event
    def event_actionButton3(self):
        ab3 = self.UI.actionButton_3

        if ab3.text() == "Credit":
            self.player.before=self.player.place
            self.UI.screen_credit()
        elif ab3.text() == "던전 선택":
            self.player.before = self.player.place
            if self.player.place == "마을1":
                self.UI.screen_village_dungeonChoice(self.v1.linked_dun)
            elif self.player.place == "마을2":
                self.UI.screen_village_dungeonChoice(self.v2.linked_dun)
            elif self.player.place == "마을3":
                self.UI.screen_village_dungeonChoice(self.v3.linked_dun)
        elif ab3.text() == "입장":
            self.player.flag = True
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move()
        elif ab3.text() == "열기":
            self.player.flag = True
            self.UI.map_draw(self.dun.map)
            self.player.gold += 500
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.UI.screen_dungeon_box_open(500)
        elif ab3.text() == "싸우자":
            self.UI.screen_dungeon_boss_battle(self.mon.hp_current, self.mon.mp_current)
        elif ab3.text() == "둘러보기":
            self.UI.screen_dungeon_move()

    # action button_4 event
    def event_actionButton4(self):
        ab4 = self.UI.actionButton_4

        if ab4.text() == "Exit":
            self.UI.close()
        elif ab4.text() == "뒤로":
            self.back()
        elif ab4.text() == "탈출":
            self.UI.mapWindow.clear()
            if self.player.place == "던전1-1":
                self.dun.map[self.player.x][self.player.y] = self.d11.map[self.player.x][self.player.y]
                self.dun.map[self.d11.initX][self.d11.initY] = 2
                self.d11.map = self.dun.map
            self.player.hp_current=self.player.hp_current-1
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.back()
        elif ab4.text() == "계속하기":
            self.UI.screen_dungeon_move()
        elif ab4.text() == "돌아가기": # 보스방 깼을 때 마을로
            self.UI.mapWindow.clear()
            if self.player.place == "던전1-1":
                self.d11.map = self.dun.map
            self.back()
        elif ab4.text() == "마을 선택":
            self.player.before = self.player.place
            if self.player.place == "마을1":
                self.UI.screen_village_villageChoice(self.v1.linked_vil)
            elif self.player.place == "마을2":
                self.UI.screen_village_villageChoice(self.v2.linked_vil)
            elif self.player.place == "마을3":
                self.UI.screen_village_villageChoice(self.v3.linked_vil)


if __name__ == '__main__':
    a = Controller()
    a.start()