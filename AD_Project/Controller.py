import sys
from UI import MainUI


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QApplication, QWidget


class Controller:
    def __init__(self):
        self.UI = MainUI()
        self.UI.button_1.clicked.connect(self.event_button1)
        self.UI.button_2.clicked.connect(self.event_button2)
        self.UI.button_3.clicked.connect(self.event_button3)
        self.UI.button_4.clicked.connect(self.event_button4)
        self.UI.button_5.clicked.connect(self.event_button5)
        self.UI.button_6.clicked.connect(self.event_button6)
        self.UI.button_7.clicked.connect(self.event_button7)
        self.UI.button_8.clicked.connect(self.event_button8)
        self.UI.button_9.clicked.connect(self.event_button9)

    # game start
    def start(self, app):
        self.UI.screen_main()
        self.UI.show()
        sys.exit(app.exec_())

    # button_1 event
    def event_button1(self):
        b1 = self.UI.button_1

        if b1.text() == "Main":
            self.UI.screen_main()
        elif b1.text() == "New Game":
            self.UI.text_load("Prolog.txt")
        elif b1.text() == "Next":
            self.UI.text_next()
        elif b1.text() == "Continue":
            self.UI.text_end()

    # button_2 event
    def event_button2(self):
        b2 = self.UI.button_2

        if b2.text() == "Skip":
            self.UI.text_end()

    # button_3 event
    def event_button3(self):
        b3 = self.UI.button_3

        if b3.text() == "Credit":
            self.UI.screen_credit()

    # button_4 event
    def event_button4(self):
        b4 = self.UI.button_4

        if b4.text() == "Exit":
            self.UI.close()

    # button_5 event
    def event_button5(self):
        b5 = self.UI.button_5

    # button_6 event
    def event_button6(self):
        b6 = self.UI.button_6

    # button_7 event
    def event_button7(self):
        b7 = self.UI.button_7

    # button_8 event
    def event_button8(self):
        b8 = self.UI.button_8

    # button_9 event
    def event_button9(self):
        b9 = self.UI.button_9


if __name__ == '__main__':
    a = Controller()
    a.start()