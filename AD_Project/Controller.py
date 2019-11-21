import sys
from UI import MainUI
from UnitModel import Unit


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

    # game start
    def start(self, app):
        self.UI.screen_main()
        self.UI.show()
        sys.exit(app.exec_())

    # move button_1 event
    def event_moveButton1(self):
        mb1 = self.UI.moveButton_1
        flag = False

    # move button_2 event
    def event_moveButton2(self):
        mb2 = self.UI.moveButton_2
        flag = False

    # move button_3 event
    def event_moveButton3(self):
        mb3 = self.UI.moveButton_3
        flag = False

    # move button_4 event
    def event_moveButton4(self):
        mb4 = self.UI.moveButton_4
        flag = False



    # action button_1 event
    def event_actionButton1(self):
        ab1 = self.UI.actionButton_1

        if ab1.text() == "Main":
            self.UI.screen_main()
        elif ab1.text() == "New Game":
            self.UI.text_load("Prolog.txt")
        elif ab1.text() == "Next":
            self.UI.text_next()
        elif ab1.text() == "Continue":
            self.UI.text_end()

    # action button_2 event
    def event_actionButton2(self):
        ab2 = self.UI.actionButton_2

        if ab2.text() == "Skip":
            self.UI.text_end()

    # action button_3 event
    def event_actionButton3(self):
        ab3 = self.UI.actionButton_3

        if ab3.text() == "Credit":
            self.UI.screen_credit()

    # action button_4 event
    def event_actionButton4(self):
        ab4 = self.UI.actionButton_4
        if ab4.text() == "Exit":
            self.UI.close()




if __name__ == '__main__':
    a = Controller()
    a.start()