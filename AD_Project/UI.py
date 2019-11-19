from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


class mainUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # game Window
        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)

        # place
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

        # enemy statement
        self.enemyWindow = QTextEdit()
        self.enemyWindow.setReadOnly(True)
        self.enemyWindow.setFixedHeight(80)
        self.enemyWindow.setFontPointSize(8)

        # user statement
        self.userWindow = QTextEdit()
        self.userWindow.setReadOnly(True)
        self.userWindow.setFixedHeight(80)
        self.userWindow.setFontPointSize(8)

        # button
        self.button_1 = QToolButton()
        self.button_1.setFixedSize(70, 70)

        self.button_2 = QToolButton()
        self.button_2.setFixedSize(70, 70)

        self.button_3 = QToolButton()
        self.button_3.setFixedSize(70, 70)

        self.button_4 = QToolButton()
        self.button_4.setFixedSize(70, 70)

        # right Layout
        rightLayout = QGridLayout()
        rightLayout.addWidget(self.enemyWindow, 0, 0, 1, 2)
        rightLayout.addWidget(self.userWindow, 1, 0, 1, 2)
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
    def button_text(self, text_1="", text_2="", text_3="", text_4=""):
        self.button_1.setText(text_1)
        self.button_2.setText(text_2)
        self.button_3.setText(text_3)
        self.button_4.setText(text_4)

    # main view
    def mainView(self):
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("title")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.placeWindow.setText("")
        self.enemyWindow.setText("")
        self.userWindow.setText("")
        self.button_text("새 게임", "불러오기", "크레딧", "종료")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = mainUI()
    game.show()
    sys.exit(app.exec_())
