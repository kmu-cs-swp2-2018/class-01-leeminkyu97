import sys
from UI import MainUI
from Model import Unit, Village, Dungeon
import MapData


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
        self.player.setting(place="메인 화면")

        self.v1 = Village()
        self.v1.setting(name="마을1", linked=["마을2"])
        self.v2 = Village()
        self.v2.setting(name="마을2")
        self.v3 = Village()
        self.v3.setting(name="마을3")

        self.dun = Dungeon()
        self.mon = Unit()



    # game start
    def start(self, app):
        self.UI.screen_main()
        self.UI.show()
        sys.exit(app.exec_())

    # back control
    def back(self):
        if self.player.before == "메인 화면":
            self.player.setting(place=self.player.before)
            self.UI.screen_main()
        elif "마을" in self.player.before:
            self.player.setting(place=self.player.before)
            self.UI.screen_village_square(self.player.before)

    # move button_1 event
    def event_moveButton1(self):
        mb1 = self.UI.moveButton_1

        x = self.player.x
        y = self.player.y

        if not ("던전" in self.player.place):
            print("던전" in self.player.place)
            print("place: ", self.player.place)
            print("not dungeon")
            return
        if x == 0:
            print("upper")
            return

        print(x,y,"here")

        if self.dun.map[x-1][y] == 1:
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            self.mon.setting(hp_current=100,mp_current=100)
            self.UI.screen_dungeon_monster(self.mon.hp_current, self.mon.mp_current)


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
            self.UI.text_load("Prolog.txt")
        elif ab1.text() == "Next":
            self.UI.text_next()
        elif ab1.text() == "Continue":
            self.UI.text_end()
        elif ab1.text() == "직업1":
            self.player.setting(level=1, unit_class="직업1", hp_max=100, hp_current=100, mp_max=100, mp_current=100, gold=50, place="마을1")
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max, self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.UI.screen_village_square(self.player.place)
        elif ab1.text() == "상점":
            self.player.setting(before=self.player.place)
            self.UI.screen_village_shop()
        elif ab1.text() == "던전1-1":
            self.dun.setting(name="던전1-1", map=MapData.maps[0])
            self.player.setting(before=self.player.place, place="던전1-1",x=3,y=3)
            print(self.player.x, self.player.y, self.player.place, self.player.before)
            self.UI.screen_dungeon_start()

    # action button_2 event
    def event_actionButton2(self):
        ab2 = self.UI.actionButton_2

        if ab2.text() == "Skip":
            self.UI.text_end()
        elif ab2.text() == "How To Play":
            self.player.setting(before=self.player.place)
            self.UI.screen_howtoplay()

    # action button_3 event
    def event_actionButton3(self):
        ab3 = self.UI.actionButton_3

        if ab3.text() == "Credit":
            self.player.setting(before=self.player.place)
            self.UI.screen_credit()
        elif ab3.text() == "던전 선택":
            self.player.setting(before=self.player.place)
            self.UI.screen_village_dungeonChoice(self.player.place)
        elif ab3.text() == "입장":
            self.UI.map_draw(self.dun.map)
            print("map:", self.dun.map)
            print("pos:", self.player.x, self.player.y)
            self.UI.screen_dungeon_move()

    # action button_4 event
    def event_actionButton4(self):
        ab4 = self.UI.actionButton_4

        if ab4.text() == "Exit":
            self.UI.close()
        elif ab4.text() == "뒤로":
            self.back()
        elif ab4.text() == "탈출":
            self.player.setting(hp_current=self.player.hp-1)
            self.back()


if __name__ == '__main__':
    a = Controller()
    a.start()