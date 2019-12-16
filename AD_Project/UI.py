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
        elif self.current_text == "npc1_1.txt":
            self.questWindow.setText("1번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc1_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc2_1.txt":
            self.questWindow.setText("2번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc2_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc3_1.txt":
            self.questWindow.setText("3번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc3_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc4_1.txt":
            self.questWindow.setText("4번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc4_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc5_1.txt":
            self.questWindow.setText("5번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc5_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc6_1.txt":
            self.questWindow.setText("6번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc6_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc7_1.txt":
            self.questWindow.setText("7번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc7_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc8_1.txt":
            self.questWindow.setText("8번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc8_2.txt":
            self.screen_quest_end()
        elif self.current_text == "npc9_1.txt":
            self.questWindow.setText("9번 퀘스트")
            self.screen_quest()
        elif self.current_text == "npc9_2.txt":
            self.text_load("Epilogue.txt")
        elif self.current_text == "Epilogue.txt":
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

        self.mapWindow.setFontPointSize(10)
        self.mapWindow.setText(tmp)

    # gameover
    def gameover(self):
        self.gameWindow.setText("")
        self.gameWindow.append("플레이어가 죽었습니다")
        self.gameWindow.append("ㅜㅅㅜ")
        self.placeWindow.clear()
        self.mapWindow.clear()
        self.playerWindow.clear()
        self.button_setText("","","","메인으로")

    # 유저 상태창
    def status_player(self, level, unit_class, hp_max, hp_current, mp_max, mp_current, gold):
        self.playerWindow.setText(unit_class + "  레벨 : " + str(level) + "  골드  : " + str(gold))
        self.playerWindow.append("hp : " + str(hp_current) + "/" + str(hp_max) + "   mp : " + str(mp_current)+ "/" + str(mp_max))

    # 메인 화면
    def screen_main(self):
        self.placeWindow.setText("메인 화면")
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("In A Dream")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.questWindow.setText("")
        self.playerWindow.setText("")
        self.button_setText("New Game", "How To Play", "Credit", "Exit")

    # 크레딧
    def screen_credit(self):
        self.placeWindow.setText("제작자")
        self.gameWindow.setText("")
        self.gameWindow.append("20163136 이민규")
        self.gameWindow.append("20182089 송희범")
        self.button_setText("","","","뒤로")

    # howtoplay
    def screen_howtoplay(self):
        self.placeWindow.setText("HowToPlay")
        self.gameWindow.setText("마을에서 NPC에게 퀘스트를 받고 해당 던전에 가서 퀘스트를 클리어하는 방식입니다")
        self.gameWindow.append("")
        self.gameWindow.append("□:벽")
        self.gameWindow.append("■:길(몬스터, 보물상자, 보스)")
        self.gameWindow.append("○:이미 한번 깬 길")
        self.gameWindow.append("★:플레이어")
        self.gameWindow.append("")
        self.gameWindow.append("던전에선 도중에 탈출할 수 있지만, 일정 데미지를 입습니다")
        self.button_setText("", "", "", "뒤로")

    # 직업 선택
    def screen_class(self):
        self.placeWindow.setText("직업 선택")
        self.gameWindow.setText("")
        self.gameWindow.append("플레이어의 직업을 선택해주세요")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("나무꾼", "저격수", "고고학자", "뒤로")

    # 스킬
    def screen_skill(self, skillList):
        self.button_setText(skillList[0],skillList[1],skillList[2],"전투")

    # 마을 이동 불가
    def screen_village_cant(self):
        self.gameWindow.append("")
        self.gameWindow.append("아직 갈 수 없는 마을입니다")

    # 마을 광장
    def screen_village_square(self, village_name):
        self.placeWindow.setText(village_name)
        self.gameWindow.setText("")
        self.gameWindow.append("마을에서 무엇을 할까?")
        self.button_setText("상점", "대화", "던전 선택", "마을 선택")

    # 마을 상점
    def screen_village_shop(self):
        self.placeWindow.setText("상점")
        self.gameWindow.setText("")
        self.gameWindow.append("어서오세요! 꽤 보고싶었다구요?")
        self.gameWindow.append("")
        self.gameWindow.append("HP물약: 100골드")
        self.gameWindow.append("MP물약: 100골드")
        self.button_setText("HP물약","MP물약","","뒤로")

    # 마을 상점 구매
    def screen_village_shop_buy(self, item_name, item_num):
        self.gameWindow.append("")
        self.gameWindow.append(item_name + "을 구매하였습니다. 현재 개수: " + str(item_num))

    # 마을 상점 구매 실패
    def screen_village_shop_nomoney(self, item_name, item_price):
        self.gameWindow.append("")
        self.gameWindow.append(item_name + "구매에 실패하였습니다. 가격은 " + str(item_price) + "골드입니다")

    # 마을 대화
    def screen_village_npc(self, npcList):
        self.gameWindow.setText("")
        self.gameWindow.append("대화할 상대를 선택하여 주세요")
        self.button_setText(npcList[0], npcList[1], npcList[2], "뒤로")

    # 던전 선택
    def screen_village_dungeonChoice(self, dungeonList):
        self.placeWindow.setText("던전 선택")
        self.gameWindow.setText("")
        self.gameWindow.append("들어가실 던전을 선택하여주세요")
        self.gameWindow.append("")
        self.gameWindow.append("해당 던전의 퀘스트를 받아야 입장이 가능합니다")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText(dungeonList[0],dungeonList[1],dungeonList[2], "뒤로")

    # 마을 선택
    def screen_village_villageChoice(self, villageList):
        self.placeWindow.setText("마을 선택")
        self.gameWindow.setText("")
        self.gameWindow.append("이동하실 마을을 선택하여주세요")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText(villageList[0], villageList[1], "", "뒤로")

    # NPC 레벨 부족
    def npc_cant(self, level):
        self.gameWindow.append("")
        self.gameWindow.append("아직 나와 대화할 때가 아니네 " + str(level) + "은 찍고 오게나")

    # NPC 퀘스트 수락
    def npc_over(self):
        self.gameWindow.append("")
        self.gameWindow.append("저번에 도와줘서 고마웠네")

    # 퀘스트 수락
    def screen_quest(self):
        self.gameWindow.setText("퀘스트를 받았다!")
        self.button_setText("","","","뒤로")

    # 퀘스트 완료
    def screen_quest_end(self):
        self.gameWindow.setText("퀘스트를 완료했다!")
        self.questWindow.clear()
        self.button_setText("","","","뒤로")

    # 던전 입장 불가
    def screen_dungeon_cant(self):
        self.gameWindow.append("")
        self.gameWindow.append("던전에 해당하는 퀘스트를 받고 오시오")

    # 던전 입장
    def screen_dungeon_start(self, dungeon_name):
        self.placeWindow.setText(dungeon_name)
        self.gameWindow.setText(dungeon_name + "의 입구이다.")
        self.gameWindow.append("")
        self.gameWindow.append("으쓱한 기운이 느껴진다.")
        self.button_setText("", "", "입장", "뒤로")

    # 던전 이동
    def screen_dungeon_move(self, clear):
        self.gameWindow.setText("우측 하단의 방향키로 이동해주세요")
        self.gameWindow.append("")
        self.gameWindow.append("□:벽")
        self.gameWindow.append("■:길(몬스터, 보물상자, 보스)")
        self.gameWindow.append("○:이미 한번 깬 길")
        self.gameWindow.append("★:플레이어")
        if clear == False:
            self.button_setText("", "", "아이템", "탈출")
        else:
            self.button_setText("", "", "아이템", "나가기")

    # 던전 아이템
    def screen_dungeon_item(self, itemList):
        self.gameWindow.append("")
        self.gameWindow.append("HP물약: " + str(itemList[0]))
        self.gameWindow.append("MP물약: " + str(itemList[1]))
        self.button_setText("HP물약", "MP물약", "", "전투")

    # 던전 몬스터
    def screen_dungeon_monster(self,name,hp):
        self.gameWindow.setText("")
        self.gameWindow.append(name + "의 hp: " + str(hp))
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("공격", "스킬", "아이템", "탈출")

    # 던전 몬스터 공격
    def screen_dungeon_monster_attack(self, name, hp, dmgToMon, dmgToPly):
        self.gameWindow.clear()
        self.gameWindow.setText("")
        self.gameWindow.append(name + "에게")
        self.gameWindow.append(str(dmgToMon) + "의 데미지를 주었다")
        self.gameWindow.append("")
        self.gameWindow.append(str(dmgToPly) + "의 피해를 받았다")
        self.gameWindow.append("")
        self.gameWindow.append(name + "의 hp: " + str(hp))
        self.gameWindow.setAlignment(Qt.AlignCenter)

    # 던전 보물상자
    def screen_dungeon_box(self):
        self.gameWindow.setText("보물상자 발견!!")
        self.button_setText("","","열기","")

    # 던전 보물상자 열기
    def screen_dungeon_box_open(self, gold):
        self.gameWindow.setText(str(gold) + "획득")
        self.button_setText("","","","계속하기")

    #던전 보스 등장
    def screen_dungeon_boss(self, boss_name):
        self.placeWindow.setText(boss_name)
        self.gameWindow.setText("")
        self.gameWindow.append(boss_name + "가 나타났다!!")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.button_setText("","","싸우자","탈출")

    # 던전 클리어
    def screen_dungeon_clear(self):
        self.gameWindow.setText("")
        self.gameWindow.append("던전을 클리어했다 마을로 돌아가자")
        self.button_setText("","","둘러보기","돌아가기")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = MainUI()
    game.show()
    sys.exit(app.exec_())