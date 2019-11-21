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
        self.enemyWindow = QTextEdit()
        self.enemyWindow.setReadOnly(True)
        self.enemyWindow.setFixedHeight(90)
        self.enemyWindow.setFontPointSize(8)

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
        downLayout.addWidget(self.enemyWindow, 1, 0)
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
        self.enemyWindow.clear()
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

    # 맵 로드
    def map_load(self):
        pass

    # 맵 지우기
    def map_end(self):
        pass

    # 메인 화면
    def screen_main(self):
        self.placeWindow.setText("메인 화면")
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("title")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.enemyWindow.setText("")
        self.playerWindow.setText("")
        self.button_setText("New Game", "How To Play", "Credit", "Exit")

    # 크레딧
    def screen_credit(self):
        self.placeWindow.setText("제작자")
        self.gameWindow.setText("20163136이민규\n20182089송희범")  # 가운데정렬 문제해결 요함
        self.gameWindow.setAlignment(Qt.AlignCenter)

        self.button_setText("Main")

    # 직업 선택
    def screen_class(self):
        self.placeWindow.setText("직업 선택")
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.gameWindow.setText("플레이어의 직업을 선택해주세요")
        self.button_setText("직업1", "직업2", "직업3", "뒤로")

    # 마을 광장
    def screen_village_square(self):
        pass

    # 마을 상점
    def screen_village_shop(self):
        pass

    # 던전 이동
    def screen_dungeon_move(self):
        pass

    # 던전 전투
    def screen_dungeon_battle(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = MainUI()
    game.show()
    sys.exit(app.exec_())
