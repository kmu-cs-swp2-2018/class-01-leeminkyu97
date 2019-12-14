from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


class MainUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # place Window
        self.placeWindow = QLineEdit()
        self.placeWindow.setFixedWidth(120)
        self.placeWindow.setReadOnly(True)

        # place Layout
        placeLayout = QVBoxLayout()
        placeLayout.addWidget(self.placeWindow)
        placeLayout.addStretch(1)

        # game Window
        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)
        self.gameWindow.setFixedHeight(400)

        # map Window
        self.mapWindow = QTextEdit()
        self.mapWindow.setReadOnly(True)
        self.mapWindow.setFixedHeight(200)

        # enemy Window
        self.questWindow = QTextEdit()
        self.questWindow.setReadOnly(True)
        self.questWindow.setFixedHeight(90)
        self.questWindow.setFontPointSize(8)

        # player Window
        self.playerWindow = QTextEdit()
        self.playerWindow.setReadOnly(True)
        self.playerWindow.setFixedHeight(90)
        self.playerWindow.setFontPointSize(8)

        # upper Layout
        upperLayout = QGridLayout()
        upperLayout.addWidget(self.gameWindow, 0, 0)


        # down Layout
        downLayout = QGridLayout()
        downLayout.addWidget(self.mapWindow, 0, 0)
        downLayout.addWidget(self.questWindow, 1, 0)
        downLayout.addWidget(self.playerWindow, 2, 0)


        # button
        self.moveButton_1 = QToolButton()
        self.moveButton_1.setFixedSize(50, 80)
        self.moveButton_1.setText("▲")
        self.moveButton_2 = QToolButton()
        self.moveButton_2.setFixedSize(80, 50)
        self.moveButton_2.setText("◀")
        self.moveButton_3 = QToolButton()
        self.moveButton_3.setFixedSize(80, 50)
        self.moveButton_3.setText("▶")
        self.moveButton_4 = QToolButton()
        self.moveButton_4.setFixedSize(50, 80)
        self.moveButton_4.setText("▼")


        self.actionButton_1 = QToolButton()
        self.actionButton_1.setFixedSize(100, 100)
        self.actionButton_2 = QToolButton()
        self.actionButton_2.setFixedSize(100, 100)
        self.actionButton_3 = QToolButton()
        self.actionButton_3.setFixedSize(100, 100)
        self.actionButton_4 = QToolButton()
        self.actionButton_4.setFixedSize(100, 100)


        # move button Layout
        moveButtonLayout = QGridLayout()
        moveButtonLayout.addWidget(self.moveButton_1, 0, 1)
        moveButtonLayout.addWidget(self.moveButton_2, 1, 0)
        moveButtonLayout.addWidget(self.moveButton_3, 1, 2)
        moveButtonLayout.addWidget(self.moveButton_4, 2, 1)


        # action button Layout
        actionButtonLayout = QGridLayout()
        actionButtonLayout.addWidget(self.actionButton_1, 0, 0)
        actionButtonLayout.addWidget(self.actionButton_2, 0, 1)
        actionButtonLayout.addWidget(self.actionButton_3, 1, 0)
        actionButtonLayout.addWidget(self.actionButton_4, 1, 1)

        # main Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(placeLayout, 0, 0)
        mainLayout.addLayout(upperLayout,1,0)
        mainLayout.addLayout(downLayout,1,1)
        mainLayout.addLayout(moveButtonLayout,2,0)
        mainLayout.addLayout(actionButtonLayout,2,1)

        self.setLayout(mainLayout)

        self.setWindowTitle("title")

        self.setGeometry(500,500,1000,2000)

    # 버튼 문자 변경
    def button_setText(self, text_1="", text_2="", text_3="", text_4=""):
        self.actionButton_1.setText(text_1)
        self.actionButton_2.setText(text_2)
        self.actionButton_3.setText(text_3)
        self.actionButton_4.setText(text_4)

    # 텍스트 파일 불러오기
    def text_load(self, filename):
        f = open(filename, "r", encoding="utf-8")
        self.current_text = filename
        self.lines = f.readlines()
        f.close()
        self.placeWindow.setText(filename[:-4])
        self.questWindow.clear()
        self.gameWindow.clear()
        self.button_setText("Next", "Skip")
        self.gameWindow.append(self.lines[0])
        self.cnt_textline = 1

    # 다음 문장
    def text_next(self):
        self.gameWindow.append(self.lines[self.cnt_textline])
        self.cnt_textline += 1
        if self.cnt_textline == len(self.lines):
            self.button_setText("Continue")

    # 텍스트 종료
    def text_end(self):
        if self.current_text == "Prolog.txt":
            self.screen_class()
        elif self.current_text == "Ending.txt":
            self.screen_main()

    # 맵 그리기
    def map_draw(self, map):
        tmp = ""
        for i in range(0, len(map)):
            for j in range(0, len(map[0])):
                if map[i][j] == 0: #벽
                    tmp += "□"
                elif map[i][j] == 1: #길 (안깬, 몬스터)
                    tmp += "■"
                elif map[i][j] == 2: #플레이어
                    tmp += "★"
                elif map[i][j] == 3: #길 (깬)
                    tmp += "○"
                elif map[i][j] == 4: #길 (안깬, 보물상자)
                    tmp += "■"
                elif map[i][j] == 5: #길 (안깬, 보스)
                    tmp += "■"
            tmp += "\n"

        self.mapWindow.setFontPointSize(12)
        self.mapWindow.setText(tmp)

    # 유저 상태창
    def status_player(self, level, unit_class, hp_max, hp_current, mp_max, mp_current, gold):
        self.playerWindow.setText(unit_class + "  레벨 : " + str(level) + "  골드  : " + str(gold))
        self.playerWindow.append("hp : " + str(hp_current)+ "/" +str(hp_max) + "   mp : " +str(mp_current)+ "/" + str(mp_max))

    # 메인 화면
    def screen_main(self):
        self.placeWindow.setText("메인 화면")
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("title")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.questWindow.setText("")
        self.playerWindow.setText("")
        self.button_setText("New Game", "How To Play", "Credit", "Exit")

    # 크레딧
    def screen_credit(self):
        self.placeWindow.setText("제작자")
        self.gameWindow.setText("20163136 이민규")
        self.gameWindow.append("20182089 송희범")
        self.button_setText("","","","뒤로")

    # howtoplay
    def screen_howtoplay(self):
        self.placeWindow.setText("HowToPlay")
        self.gameWindow.setText("HowToPlay UI")
        self.button_setText("", "", "", "뒤로")

    # 직업 선택
    def screen_class(self):
        self.placeWindow.setText("직업 선택")
        self.gameWindow.setText("플레이어의 직업을 선택해주세요")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("직업1", "직업2", "직업3", "뒤로")

    # 마을 광장
    def screen_village_square(self, village_name):
        self.placeWindow.setText(village_name)
        self.gameWindow.setText("마을 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("상점", "대화", "던전 선택", "마을 선택")

    # 마을 상점
    def screen_village_shop(self):
        self.placeWindow.setText("상점")
        self.gameWindow.setText("상점 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("아이템1","아이템2","아이템3","뒤로")

    # 마을 상점 구매
    def screen_village_shop_buy(self, item_name, item_num):
        self.gameWindow.append(item_name + "을 구매하였습니다. 현재 개수: " + str(item_num))

    # 마을 상점 구매 실패
    def screen_village_shop_nomoney(self, item_name, item_price):
        self.gameWindow.append(item_name + "구매에 실패하였습니다. 가격은 " + str(item_price) + "골드입니다")

    # 마을 대화
    def screen_village_npc(self, npcList):
        self.gameWindow.setText("NPC 선택 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText(npcList[0], npcList[1], npcList[2], "뒤로")

    # 던전 선택
    def screen_village_dungeonChoice(self, dungeonList):
        self.placeWindow.setText("던전 선택")
        self.gameWindow.setText("던전 선택 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText(dungeonList[0],dungeonList[1],dungeonList[2], "뒤로")

    # 마을 선택
    def screen_village_villageChoice(self, villageList):
        self.gameWindow.setText("마을 선택 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText(villageList[0], villageList[1], "", "뒤로")


    # 던전 입장
    def screen_dungeon_start(self):
        self.placeWindow.setText("던전1-1")
        self.gameWindow.setText("던전 입장 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("", "", "입장", "뒤로")

    # 던전 이동
    def screen_dungeon_move(self):
        self.placeWindow.setText("던전1-1")
        self.gameWindow.setText("던전 이동 UI")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("", "", "아이템", "탈출")

    # 던전 아이템
    def screen_dungeon_item(self, itemList):
        self.gameWindow.append("아이템1: " + str(itemList[0]))
        self.gameWindow.append("아이템2: " + str(itemList[1]))
        self.gameWindow.append("아이템3: " + str(itemList[2]))
        self.button_setText("아이템1", "아이템2", "아이템3", "전투")

    # 던전 몬스터
    def screen_dungeon_monster(self,hp,mp):
        self.placeWindow.setText("던전1-1")
        self.gameWindow.setText("hp: " + str(hp))
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("공격", "스킬", "아이템", "탈출")

    # 던전 보물상자
    def screen_dungeon_box(self):
        self.gameWindow.setText("보물상자 발견!!")
        self.button_setText("","","열기","무시")

    # 던전 보물상자 열기
    def screen_dungeon_box_open(self, gold):
        self.gameWindow.setText(str(gold) + "획득")
        self.button_setText("","","","계속하기")

    #던전 보스 등장
    def screen_dungeon_boss(self, boss_name):
        self.placeWindow.setText("던전1-1 보스")
        self.gameWindow.setText(boss_name + "가 나타났다!!")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("","","싸우자","탈출")

    #던전 보스 배틀
    def screen_dungeon_boss_battle(self, hp, mp):
        self.placeWindow.setText("던전1-1 보스")
        self.gameWindow.setText("hp: " + str(hp))
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("공격", "스킬", "아이템", "탈출")

    # 던전 클리어
    def screen_dungeon_clear(self):
        self.gameWindow.setText("던전을 클리어했다 마을로 돌아가자")
        self.button_setText("","","둘러보기","돌아가기")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = MainUI()
    game.show()
    sys.exit(app.exec_())