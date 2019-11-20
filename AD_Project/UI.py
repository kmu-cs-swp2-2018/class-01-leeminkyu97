from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


class MainUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # game Window
        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)

        # place Window
        self.placeWindow = QLineEdit()
        self.placeWindow.setFixedWidth(100)
        self.placeWindow.setReadOnly(True)

        # place Layout
        placeLayout = QVBoxLayout()
        placeLayout.addWidget(self.placeWindow)
        placeLayout.addStretch(1)

        # left Layout
        leftLayout = QGridLayout()
        leftLayout.addWidget(self.gameWindow, 0, 0)

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

        # button
        self.button_1 = QToolButton()
        self.button_1.setFixedSize(80, 80)

        self.button_2 = QToolButton()
        self.button_2.setFixedSize(80, 80)

        self.button_3 = QToolButton()
        self.button_3.setFixedSize(80, 80)

        self.button_4 = QToolButton()
        self.button_4.setFixedSize(80, 80)

        # right Layout
        rightLayout = QGridLayout()
        rightLayout.addWidget(self.enemyWindow, 0, 0, 1, 2)
        rightLayout.addWidget(self.playerWindow, 1, 0, 1, 2)
        rightLayout.addWidget(self.button_1, 2, 0)
        rightLayout.addWidget(self.button_2, 2, 1)
        rightLayout.addWidget(self.button_3, 3, 0)
        rightLayout.addWidget(self.button_4, 3, 1)

        # main Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(placeLayout, 0, 0)
        mainLayout.addLayout(leftLayout, 1, 0)
        mainLayout.addLayout(rightLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("title")

        self.setGeometry(300, 300, 1500, 1000)

    # 버튼 문자 변경
    def button_setText(self, text_1="", text_2="", text_3="", text_4=""):
        self.button_1.setText(text_1)
        self.button_2.setText(text_2)
        self.button_3.setText(text_3)
        self.button_4.setText(text_4)

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

    # 메인 화면
    def screen_main(self):
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("title")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.placeWindow.setText("메인 화면")
        self.enemyWindow.setText("")
        self.playerWindow.setText("")
        self.button_setText("New Game", "Load", "Credit", "Exit")

    # 크레딧
    def screen_credit(self):
        self.placeWindow.setText("제작자")
        self.gameWindow.setText("20163136이민규\n20180000송희범")  # 가운데정렬 문제해결 요함
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
