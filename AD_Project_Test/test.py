from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


class testUI(QWidget):
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

        self.mapWindow.setFontPointSize(15)
        self.mapWindow.setText("■■■■■□■■■\n■■■■■□■■■\n■□□☆□□■■■\n■■■■□■■■■\n■■■■■■■■■")




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = testUI()
    game.show()
    sys.exit(app.exec_())
