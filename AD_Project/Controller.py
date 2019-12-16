import sys
from UI import MainUI
from Model import Unit, Village, Dungeon, Monster
import MapData
import random
import copy


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

        # 이름, hp, dmg, gold

        self.d11 = Dungeon()
        self.d11.map = MapData.maps[0]
        self.d11.monster = [["겁나 큰개구리", 100, 10, 10], ["머리 셋달린 악어", 105, 12, 10], ["식인 부레옥잠", 110, 13, 10], ["팔뚝만한 실지렁이", 100, 14, 10]]
        self.d11.boss = ["겁나 큰개구리와 합체한 머리 셋달린 악어", 130, 16, 10]
        self.d11.initX = 3
        self.d11.initY = 3

        self.d12 = Dungeon()
        self.d12.map = MapData.maps[1]
        self.d12.monster = [["겁나 큰입 베스", 120, 15, 10], ["걸어다니는 독버들", 130, 16, 10], ["입이 배까지 찢어지는 뉴트리아", 140, 17, 10],
                            ["붉은 귀 거북", 150, 18, 10]]
        self.d12.boss = ["쓰레기강 요괴 사오정", 180, 22, 10]
        self.d12.initX = 3
        self.d12.initY = 3

        self.d13 = Dungeon()
        self.d13.map = MapData.maps[2]
        self.d13.monster = [["거짓말하는 자작나무", 160, 20, 10], ["야무진 오동나무", 175, 22, 10], ["핏빛의 단풍나무", 180, 23, 10], ["유연한 소나무", 185, 24, 10]]
        self.d13.boss = ["오동나무 아저씨", 200, 25, 10]
        self.d13.initX = 3
        self.d13.initY = 3

        self.d21 = Dungeon()
        self.d21.map = MapData.maps[3]
        self.d21.monster = [["미쳐버린 광신도", 190, 25, 10], ["추격자 집사", 195, 26, 10], ["끈질긴 전도사", 200, 27, 10], ["현혹하는 목사", 205, 28, 10]]
        self.d21.boss = ["악마와 계약한 장로", 220, 32, 10]
        self.d21.initX = 3
        self.d21.initY = 3

        self.d22 = Dungeon()
        self.d22.map = MapData.maps[4]
        self.d22.monster = [["핵폐기물 좀비", 225, 29, 10], ["사일런트힐 너스", 220, 30, 10], ["피곤한 레지던트", 215, 32, 10], ["어리버리한 인턴", 210, 33, 10]]
        self.d22.boss = ["문도박사", 240, 35, 10]
        self.d22.initX = 3
        self.d22.initY = 3

        self.d23 = Dungeon()
        self.d23.map = MapData.maps[5]
        self.d23.monster = [["오염된 시식코너 판매원", 230, 35, 10], ["쌍칼 정육점직원", 240, 36, 10], ["돈많은 진상손님", 245, 37, 10],
                            ["돌진하는 카트", 235, 39, 10]]
        self.d23.boss = ["사장아들 매니저", 255, 42, 10]
        self.d23.initX = 3
        self.d23.initY = 3

        self.d31 = Dungeon()
        self.d31.map = MapData.maps[6]
        self.d31.monster = [["고문관 이등병", 250, 40, 10], ["일개미 일병", 255, 41, 10], ["맞고자란 상병", 260, 42, 10], ["꼬장킹 병장", 265, 44, 10]]
        self.d31.boss = ["전역짤린 병장", 275, 48, 10]
        self.d31.initX = 3
        self.d31.initY = 3

        self.d32 = Dungeon()
        self.d32.map = MapData.maps[7]
        self.d32.monster = [['대대장', 270, 45, 10], ['연대장', 275, 47, 10], ['사단장', 280, 49, 10], ['군단장', 290, 52, 10]]
        self.d32.boss = ["사령관", 300, 54, 10]
        self.d32.initX = 3
        self.d32.initY = 3

        self.d33 = Dungeon()
        self.d33.map = MapData.maps[8]
        self.d33.monster = [['군의관', 250, 40, 10], ['간호장교', 265, 44, 10], ['꾀병걸린 병장', 260, 42, 10], ['실패한 실험체', 270, 30, 10]]
        self.d33.boss = ["생체병기-73", 320, 58, 10]
        self.d33.initX = 3
        self.d33.initY = 3

        self.dun = Dungeon()  #현재 던전
        self.mon = Monster()  #현재 몬스터

    # game start
    def start(self, app):
        self.UI.screen_main()
        self.UI.show()
        sys.exit(app.exec_())

    # back control
    def back(self):
        if self.player.before == "메인 화면":
            self.player.place = self.player.before
            self.UI.screen_main()
        elif "마을" in self.player.before:
            self.player.place = self.player.before
            self.UI.screen_village_square(self.player.before)

    # attack
    def attack(self, str):
        damage = str
        return damage

    # 직업 1
    def job1(self):
        self.player.level = 1
        self.player.unit_class = "나무꾼"
        self.player.hp_max = 100
        self.player.hp_current = 100
        self.player.mp_max = 100
        self.player.mp_current = 100
        self.player.gold = 100
        self.player.str = 10
        self.player.dex = 1
        self.player.int = 1

    # 직업 2
    def job2(self):
        self.player.level = 1
        self.player.unit_class = "저격수"
        self.player.hp_max = 100
        self.player.hp_current = 100
        self.player.mp_max = 100
        self.player.mp_current = 100
        self.player.gold = 100
        self.player.str = 10
        self.player.dex = 1
        self.player.int = 1

    # 직업 3
    def job3(self):
        self.player.level = 1
        self.player.unit_class = "고고학자"
        self.player.hp_max = 100
        self.player.hp_current = 100
        self.player.mp_max = 100
        self.player.mp_current = 100
        self.player.gold = 100
        self.player.str = 10
        self.player.dex = 1
        self.player.int = 1

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
            self.player.enemyType = "몬스터"
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            r = random.randint(0, len(self.dun.monster)-1)
            self.mon.name = self.dun.monster[r][0]
            self.mon.hp = self.dun.monster[r][1]
            self.mon.atk = self.dun.monster[r][2]
            self.mon.gold = self.dun.monster[r][3]
            self.UI.screen_dungeon_monster(self.mon.name, self.mon.hp)

        if self.dun.map[x-1][y] == 3:   # 이미 깬 길
            self.player.flag = True
            self.player.enemyType = "이동"
            self.dun.map[x][y] = 3
            self.dun.map[x - 1][y] = 2
            self.player.x = x - 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move(self.dun.clear)

        if self.dun.map[x-1][y] == 4:   # 보물상자
            self.player.flag = True
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_box()

        if self.dun.map[x-1][y] == 5:   # 보스
            self.player.flag = False
            self.player.enemyType = "보스"
            self.dun.map[x][y] = 3
            self.dun.map[x-1][y] = 2
            self.player.x = x-1
            self.UI.map_draw(self.dun.map)
            self.mon.name = self.dun.boss[0]
            self.mon.hp = self.dun.boss[1]
            self.mon.atk = self.dun.boss[2]
            self.mon.gold = self.dun.boss[3]
            self.UI.screen_dungeon_boss(self.mon.name)

    # move button_2 event
    def event_moveButton2(self):
        mb2 = self.UI.moveButton_2

        x = self.player.x
        y = self.player.y

        if not ("던전" in self.player.place):
            return
        if y == 0:
            return
        if self.player.flag == False:
            return

        if self.dun.map[x][y-1] == 1:  # 몬스터
            self.player.flag = False
            self.player.enemyType = "몬스터"
            self.dun.map[x][y] = 3
            self.dun.map[x][y-1] = 2
            self.player.y = y - 1
            self.UI.map_draw(self.dun.map)
            r = random.randint(0, len(self.dun.monster) - 1)
            self.mon.name = self.dun.monster[r][0]
            self.mon.hp = self.dun.monster[r][1]
            self.mon.atk = self.dun.monster[r][2]
            self.mon.gold = self.dun.monster[r][3]
            self.UI.screen_dungeon_monster(self.mon.name, self.mon.hp)

        if self.dun.map[x][y-1] == 3:  # 이미 깬 길
            self.player.flag = True
            self.player.enemyType = "이동"
            self.dun.map[x][y] = 3
            self.dun.map[x][y-1] = 2
            self.player.y = y - 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move(self.dun.clear)

        if self.dun.map[x][y-1] == 4:  # 보물상자
            self.player.flag = True
            self.dun.map[x][y] = 3
            self.dun.map[x][y-1] = 2
            self.player.y = y - 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_box()

        if self.dun.map[x][y-1] == 5:  # 보스
            self.player.flag = False
            self.player.enemyType = "보스"
            self.dun.map[x][y] = 3
            self.dun.map[x][y-1] = 2
            self.player.y = y - 1
            self.UI.map_draw(self.dun.map)
            self.mon.name = self.dun.boss[0]
            self.mon.hp = self.dun.boss[1]
            self.mon.atk = self.dun.boss[2]
            self.mon.gold = self.dun.boss[3]
            self.UI.screen_dungeon_boss(self.mon.name)

    # move button_3 event
    def event_moveButton3(self):
        mb3 = self.UI.moveButton_3

        x = self.player.x
        y = self.player.y

        if not ("던전" in self.player.place):
            return
        if y == self.dun.map[-1]:
            return
        if self.player.flag == False:
            return

        if self.dun.map[x][y + 1] == 1:  # 몬스터
            self.player.flag = False
            self.player.enemyType = "몬스터"
            self.dun.map[x][y] = 3
            self.dun.map[x][y + 1] = 2
            self.player.y = y + 1
            self.UI.map_draw(self.dun.map)
            r = random.randint(0, len(self.dun.monster) - 1)
            self.mon.name = self.dun.monster[r][0]
            self.mon.hp = self.dun.monster[r][1]
            self.mon.atk = self.dun.monster[r][2]
            self.mon.gold = self.dun.monster[r][3]
            self.UI.screen_dungeon_monster(self.mon.name, self.mon.hp)

        if self.dun.map[x][y + 1] == 3:  # 이미 깬 길
            self.player.flag = True
            self.player.enemyType = "이동"
            self.dun.map[x][y] = 3
            self.dun.map[x][y + 1] = 2
            self.player.y = y + 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move(self.dun.clear)

        if self.dun.map[x][y + 1] == 4:  # 보물상자
            self.player.flag = True
            self.dun.map[x][y] = 3
            self.dun.map[x][y + 1] = 2
            self.player.y = y + 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_box()

        if self.dun.map[x][y + 1] == 5:  # 보스
            self.player.flag = False
            self.player.enemyType = "보스"
            self.dun.map[x][y] = 3
            self.dun.map[x][y + 1] = 2
            self.player.y = y + 1
            self.UI.map_draw(self.dun.map)
            self.mon.name = self.dun.boss[0]
            self.mon.hp = self.dun.boss[1]
            self.mon.atk = self.dun.boss[2]
            self.mon.gold = self.dun.boss[3]
            self.UI.screen_dungeon_boss(self.mon.name)

    # move button_4 event
    def event_moveButton4(self):
        mb4 = self.UI.moveButton_4

        x = self.player.x
        y = self.player.y

        if not ("던전" in self.player.place):
            return
        if x == self.dun.map[-1]:
            return
        if self.player.flag == False:
            return

        if self.dun.map[x + 1][y] == 1:  # 몬스터
            self.player.flag = False
            self.player.enemyType = "몬스터"
            self.dun.map[x][y] = 3
            self.dun.map[x + 1][y] = 2
            self.player.x = x + 1
            self.UI.map_draw(self.dun.map)
            r = random.randint(0, len(self.dun.monster) - 1)
            self.mon.name = self.dun.monster[r][0]
            self.mon.hp = self.dun.monster[r][1]
            self.mon.atk = self.dun.monster[r][2]
            self.mon.gold = self.dun.monster[r][3]
            self.UI.screen_dungeon_monster(self.mon.name, self.mon.hp)

        if self.dun.map[x + 1][y] == 3:  # 이미 깬 길
            self.player.flag = True
            self.player.enemyType = "이동"
            self.dun.map[x][y] = 3
            self.dun.map[x + 1][y] = 2
            self.player.x = x + 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move(self.dun.clear)

        if self.dun.map[x + 1][y] == 4:  # 보물상자
            self.player.flag = True
            self.dun.map[x][y] = 3
            self.dun.map[x + 1][y] = 2
            self.player.x = x + 1
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_box()

        if self.dun.map[x + 1][y] == 5:  # 보스
            self.player.flag = False
            self.player.enemyType = "보스"
            self.dun.map[x][y] = 3
            self.dun.map[x + 1][y] = 2
            self.player.x = x + 1
            self.UI.map_draw(self.dun.map)
            self.mon.name = self.dun.boss[0]
            self.mon.hp = self.dun.boss[1]
            self.mon.atk = self.dun.boss[2]
            self.mon.gold = self.dun.boss[3]
            self.UI.screen_dungeon_boss(self.mon.name)



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
            self.player.before = self.player.place
            self.player.place = "상점"
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
            self.dun = copy.deepcopy(self.d11)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab1.text() == "던전2-1":
            self.player.before = self.player.place
            self.player.place = "던전2-1"
            self.dun = copy.deepcopy(self.d21)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab1.text() == "던전3-1":
            self.player.before = self.player.place
            self.player.place = "던전3-1"
            self.dun = copy.deepcopy(self.d31)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab1.text() == "공격":
            if "몬스터" in self.player.enemyType:
                self.mon.hp -= self.attack(self.player.str)
                self.player.hp_current -= self.attack(self.mon.atk)
                self.UI.screen_dungeon_monster_attack(self.mon.name, self.mon.hp,self.mon.atk)
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                      self.player.gold)
                if self.mon.hp <= 0:    # 몬스터의 체력이 0 이하이면 이동 화면
                    self.player.gold += self.mon.gold
                    self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                          self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                          self.player.gold)
                    self.player.flag = True
                    self.UI.screen_dungeon_move(self.dun.clear)
            elif "보스" in self.player.enemyType:
                self.mon.hp -= self.attack(10)
                self.UI.screen_dungeon_boss_battle(self.mon.name, self.mon.hp)
                if self.mon.hp <= 0:  # 몬스터의 체력이 0 이하이면 이동 화면
                    self.dun.clear = True
                    self.player.flag = True
                    self.player.quest_cnt += 1
                    self.UI.screen_dungeon_clear()
        elif ab1.text() == "아이템1":
            if self.player.place == "상점":
                if self.player.gold < 50:
                    self.UI.screen_village_shop_nomoney("아이템1", 50)
                    return
                self.player.item[0] += 1
                self.player.gold -= 50
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
                self.UI.screen_village_shop_buy("아이템1", self.player.item[0])
            else:
                self.player.item[0] -= 1
                if self.player.hp_current + 10 < self.player.hp_max:
                    self.player.hp_current += 10
                else:
                    self.player.hp_current = self.player.hp_max
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                      self.player.gold)
        elif ab1.text() == "npc1":
            if self.player.quest_cnt == 0:
                self.UI.text_load("npc1_1.txt")
            elif self.player.quest_cnt == 1:
                self.player.quest_cnt += 1
                self.UI.text_load("npc1_2.txt")
        elif ab1.text() == "npc4":
            if self.player.quest_cnt == 6:
                self.UI.text_load("npc4_1.txt")
            elif self.player.quest_cnt == 7:
                self.player.quest_cnt += 1
                self.UI.text_load("npc4_2.txt")
        elif ab1.text() == "npc7":
            if self.player.quest_cnt == 12:
                self.UI.text_load("npc7_1.txt")
            elif self.player.quest_cnt == 13:
                self.player.quest_cnt += 1
                self.UI.text_load("npc7_2.txt")




    # action button_2 event
    def event_actionButton2(self):
        ab2 = self.UI.actionButton_2

        if ab2.text() == "Skip":
            self.UI.text_end()
        elif ab2.text() == "How To Play":
            self.player.before = self.player.place
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
        elif ab2.text() == "던전1-2":
            self.player.before = self.player.place
            self.player.place = "던전1-2"
            self.dun = copy.deepcopy(self.d12)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab2.text() == "던전2-2":
            self.player.before = self.player.place
            self.player.place = "던전2-2"
            self.dun = copy.deepcopy(self.d22)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab2.text() == "던전3-2":
            self.player.before = self.player.place
            self.player.place = "던전3-2"
            self.dun = copy.deepcopy(self.d32)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab2.text() == "아이템2":
            if self.player.place == "상점":
                if self.player.gold < 50:
                    self.UI.screen_village_shop_nomoney("아이템2", 50)
                    return
                self.player.item[1] += 1
                self.player.gold -= 50
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                      self.player.gold)
                self.UI.screen_village_shop_buy("아이템2", self.player.item[1])
            else:
                self.player.item[1] -= 1
                if self.player.hp_current + 10 < self.player.hp_max:
                    self.player.hp_current += 10
                else:
                    self.player.hp_current = self.player.hp_max
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                      self.player.gold)
        elif ab2.text() == "직업2":
            self.job2()
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.UI.screen_village_square(self.player.place)
        elif ab2.text() == "npc2":
            if self.player.quest_cnt == 2:
                self.UI.text_load("npc2_1.txt")
            elif self.player.quest_cnt == 3:
                self.player.quest_cnt += 1
                self.UI.text_load("npc2_2.txt")
        elif ab2.text() == "npc5":
            if self.player.quest_cnt == 8:
                self.UI.text_load("npc5_1.txt")
            elif self.player.quest_cnt == 9:
                self.player.quest_cnt += 1
                self.UI.text_load("npc5_2.txt")
        elif ab2.text() == "npc8":
            if self.player.quest_cnt == 14:
                self.UI.text_load("npc8_1.txt")
            elif self.player.quest_cnt == 15:
                self.player.quest_cnt += 1
                self.UI.text_load("npc8_2.txt")



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
            self.player.enemyType = "이동"
            self.UI.map_draw(self.dun.map)
            self.UI.screen_dungeon_move(self.dun.clear)
        elif ab3.text() == "열기":
            self.UI.map_draw(self.dun.map)
            self.player.gold += 500
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.UI.screen_dungeon_box_open(500)
        elif ab3.text() == "싸우자":
            self.UI.screen_dungeon_boss_battle(self.mon.name, self.mon.hp)
        elif ab3.text() == "둘러보기":
            self.UI.screen_dungeon_move(self.dun.clear)
        elif ab3.text() == "던전1-3":
            self.player.before = self.player.place
            self.player.place = "던전1-3"
            self.dun = copy.deepcopy(self.d13)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab3.text() == "던전2-3":
            self.player.before = self.player.place
            self.player.place = "던전2-3"
            self.dun = copy.deepcopy(self.d23)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab3.text() == "던전3-3":
            self.player.before = self.player.place
            self.player.place = "던전3-3"
            self.dun = copy.deepcopy(self.d33)
            self.player.x = self.dun.initX
            self.player.y = self.dun.initY
            self.UI.screen_dungeon_start()
        elif ab3.text() == "아이템3":
            if self.player.place == "상점":
                if self.player.gold < 50:
                    self.UI.screen_village_shop_nomoney("아이템3", 50)
                    return
                self.player.item[2] += 1
                self.player.gold -= 50
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                      self.player.gold)
                self.UI.screen_village_shop_buy("아이템3", self.player.item[2])
            else:
                self.player.item[2] -= 1
                if self.player.hp_current + 10 < self.player.hp_max:
                    self.player.hp_current += 10
                else:
                    self.player.hp_current = self.player.hp_max
                self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                      self.player.hp_current, self.player.mp_max, self.player.mp_current,
                                      self.player.gold)
        elif ab3.text() == "직업3":
            self.job3()
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.UI.screen_village_square(self.player.place)
        elif ab3.text() == "아이템":
            self.UI.screen_dungeon_item(self.player.item)
        elif ab3.text() == "npc3":
            if self.player.quest_cnt == 4:
                self.UI.text_load("npc3_1.txt")
            elif self.player.quest_cnt == 5:
                self.player.quest_cnt += 1
                self.UI.text_load("npc3_2.txt")
        elif ab3.text() == "npc6":
            if self.player.quest_cnt == 10:
                self.UI.text_load("npc6_1.txt")
            elif self.player.quest_cnt == 11:
                self.player.quest_cnt += 1
                self.UI.text_load("npc6_2.txt")
        elif ab3.text() == "npc9":
            if self.player.quest_cnt == 16:
                self.UI.text_load("npc9_1.txt")
            elif self.player.quest_cnt == 17:
                self.player.quest_cnt += 1
                self.UI.text_load("npc9_2.txt")

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
                self.d11.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전1-2":
                self.dun.map[self.player.x][self.player.y] = self.d12.map[self.player.x][self.player.y]
                self.dun.map[self.d12.initX][self.d12.initY] = 2
                self.d12.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전1-3":
                self.dun.map[self.player.x][self.player.y] = self.d13.map[self.player.x][self.player.y]
                self.dun.map[self.d13.initX][self.d13.initY] = 2
                self.d13.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전2-1":
                self.dun.map[self.player.x][self.player.y] = self.d21.map[self.player.x][self.player.y]
                self.dun.map[self.d21.initX][self.d21.initY] = 2
                self.d21.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전2-2":
                self.dun.map[self.player.x][self.player.y] = self.d22.map[self.player.x][self.player.y]
                self.dun.map[self.d22.initX][self.d22.initY] = 2
                self.d22.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전2-3":
                self.dun.map[self.player.x][self.player.y] = self.d23.map[self.player.x][self.player.y]
                self.dun.map[self.d23.initX][self.d23.initY] = 2
                self.d23.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전3-1":
                self.dun.map[self.player.x][self.player.y] = self.d31.map[self.player.x][self.player.y]
                self.dun.map[self.d31.initX][self.d31.initY] = 2
                self.d31.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전3-2":
                self.dun.map[self.player.x][self.player.y] = self.d32.map[self.player.x][self.player.y]
                self.dun.map[self.d32.initX][self.d32.initY] = 2
                self.d32.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전3-3":
                self.dun.map[self.player.x][self.player.y] = self.d33.map[self.player.x][self.player.y]
                self.dun.map[self.d33.initX][self.d33.initY] = 2
                self.d33.map = copy.deepcopy(self.dun.map)
            self.player.hp_current = self.player.hp_current-13
            self.UI.status_player(self.player.level, self.player.unit_class, self.player.hp_max,
                                  self.player.hp_current, self.player.mp_max, self.player.mp_current, self.player.gold)
            self.back()
        elif ab4.text() == "나가기": # 던전 클리어 후
            self.UI.mapWindow.clear()
            if self.player.place == "던전1-1":
                self.dun.map[self.player.x][self.player.y] = self.d11.map[self.player.x][self.player.y]
                self.dun.map[self.d11.initX][self.d11.initY] = 2
                self.d11.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전1-2":
                self.dun.map[self.player.x][self.player.y] = self.d12.map[self.player.x][self.player.y]
                self.dun.map[self.d12.initX][self.d12.initY] = 2
                self.d12.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전1-3":
                self.dun.map[self.player.x][self.player.y] = self.d13.map[self.player.x][self.player.y]
                self.dun.map[self.d13.initX][self.d13.initY] = 2
                self.d13.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전2-1":
                self.dun.map[self.player.x][self.player.y] = self.d21.map[self.player.x][self.player.y]
                self.dun.map[self.d21.initX][self.d21.initY] = 2
                self.d21.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전2-2":
                self.dun.map[self.player.x][self.player.y] = self.d22.map[self.player.x][self.player.y]
                self.dun.map[self.d22.initX][self.d22.initY] = 2
                self.d22.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전2-3":
                self.dun.map[self.player.x][self.player.y] = self.d23.map[self.player.x][self.player.y]
                self.dun.map[self.d23.initX][self.d23.initY] = 2
                self.d23.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전3-1":
                self.dun.map[self.player.x][self.player.y] = self.d31.map[self.player.x][self.player.y]
                self.dun.map[self.d31.initX][self.d31.initY] = 2
                self.d31.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전3-2":
                self.dun.map[self.player.x][self.player.y] = self.d32.map[self.player.x][self.player.y]
                self.dun.map[self.d32.initX][self.d32.initY] = 2
                self.d32.map = copy.deepcopy(self.dun.map)
            elif self.player.place == "던전3-3":
                self.dun.map[self.player.x][self.player.y] = self.d33.map[self.player.x][self.player.y]
                self.dun.map[self.d33.initX][self.d33.initY] = 2
                self.d33.map = copy.deepcopy(self.dun.map)
            self.back()
        elif ab4.text() == "계속하기": # 상자 열었을 때
            self.player.flag = True
            self.UI.screen_dungeon_move(self.dun.clear)
        elif ab4.text() == "돌아가기": # 보스방 깼을 때 마을로
            self.UI.mapWindow.clear()
            if self.player.place == "던전1-1":
                self.d11 = copy.deepcopy(self.dun)
            self.back()
        elif ab4.text() == "마을 선택":
            self.player.before = self.player.place
            if self.player.place == "마을1":
                self.UI.screen_village_villageChoice(self.v1.linked_vil)
            elif self.player.place == "마을2":
                self.UI.screen_village_villageChoice(self.v2.linked_vil)
            elif self.player.place == "마을3":
                self.UI.screen_village_villageChoice(self.v3.linked_vil)
        elif ab4.text() == "전투":
            if self.player.enemyType == "이동":
                self.UI.screen_dungeon_move(self.dun.clear)
            elif self.player.enemyType == "몬스터":
                self.UI.screen_dungeon_monster(self.mon.name, self.mon.hp)
            elif self.player.enemyType == "보스":
                self.UI.screen_dungeon_boss_battle(self.mon.name, self.mon.hp)


if __name__ == '__main__':
    a = Controller()
    a.start()
