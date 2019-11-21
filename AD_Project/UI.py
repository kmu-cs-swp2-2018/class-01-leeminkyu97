from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


class MainUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # place Window
        self.placeWindow = QLineEdit()
        self.placeWindow.setFixedWidth(100)
        self.placeWindow.setReadOnly(True)

        # place Layout
        placeLayout = QVBoxLayout()
        placeLayout.addWidget(self.placeWindow)
        placeLayout.addStretch(1)

        # game Window
        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)

        # map Window
        self.mapWindow = QTextEdit()
        self.mapWindow.setReadOnly(True)

        # enemy Window
        self.enemyWindow = QTextEdit()
        self.enemyWindow.setReadOnly(True)
        self.enemyWindow.setFixedHeight(80)
        self.enemyWindow.setFontPointSize(8)

        # player Window
        self.playerWindow = QTextEdit()
        self.playerWindow.setReadOnly(True)
        self.playerWindow.setFixedHeight(80)
        self.playerWindow.setFontPointSize(8)

        # upper Layout
        upperLayout = QGridLayout()
        upperLayout.addWidget(self.gameWindow, 0, 0)
        upperLayout.addWidget(self.mapWindow,0,1)

        # down Layout
        downLayout = QGridLayout()
        downLayout.addWidget(self.enemyWindow,1 ,0)
        downLayout.addWidget(self.playerWindow,1 ,1)

        # button
        self.button_1 = QToolButton()
        self.button_1.setFixedSize(80, 80)
        self.button_2 = QToolButton()
        self.button_2.setFixedSize(80, 80)
        self.button_3 = QToolButton()
        self.button_3.setFixedSize(80, 80)
        self.button_4 = QToolButton()
        self.button_4.setFixedSize(80, 80)
        self.button_5 = QToolButton()
        self.button_5.setFixedSize(80, 80)
        self.button_6 = QToolButton()
        self.button_6.setFixedSize(80, 80)
        self.button_7 = QToolButton()
        self.button_7.setFixedSize(80, 80)
        self.button_8 = QToolButton()
        self.button_8.setFixedSize(80, 80)
        self.button_9 = QToolButton()
        self.button_9.setFixedSize(80, 80)

        # button Layout
        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.button_1, 0, 0)
        buttonLayout.addWidget(self.button_2, 0, 1)
        buttonLayout.addWidget(self.button_3, 0, 2)
        buttonLayout.addWidget(self.button_4, 1, 0)
        buttonLayout.addWidget(self.button_5, 1, 1)
        buttonLayout.addWidget(self.button_6, 1, 2)
        buttonLayout.addWidget(self.button_7, 2, 0)
        buttonLayout.addWidget(self.button_8, 2, 1)
        buttonLayout.addWidget(self.button_9, 2, 2)

        # main Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(placeLayout, 0, 0)
        mainLayout.addLayout(upperLayout,1,0)
        mainLayout.addLayout(downLayout,2,0)
        mainLayout.addLayout(buttonLayout,3,0)

        self.setLayout(mainLayout)

        self.setWindowTitle("title")

        self.setGeometry(500,500,1000,2000)

    # 버튼 문자 변경
    def button_setText(self, text_1="", text_2="", text_3="", text_4="", text_5="", text_6="", text_7="", text_8="", text_9=""):
        self.button_1.setText(text_1)
        self.button_2.setText(text_2)
        self.button_3.setText(text_3)
        self.button_4.setText(text_4)
        self.button_5.setText(text_5)
        self.button_6.setText(text_6)
        self.button_7.setText(text_7)
        self.button_8.setText(text_8)
        self.button_9.setText(text_9)

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

    # 메인 화면
    def screen_main(self):
        self.placeWindow.setText("메인 화면")
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("title")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.enemyWindow.setText("")
        self.playerWindow.setText("")
        self.button_setText("New Game", "How To Play", "Credit", text_9= "Exit")

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
        self.button_setText("직업1", "직업2", "직업3")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = MainUI()
    game.show()
    sys.exit(app.exec_())
