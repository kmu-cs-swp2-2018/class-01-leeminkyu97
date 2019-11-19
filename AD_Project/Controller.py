import sys
from UI import mainUI

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QApplication, QWidget


class controller:
    def __init__(self):
        self.UI = mainUI()
        self.UI.button_3.clicked.connect(self.button3_event)

    # game start
    def start(self, app):
        self.UI.mainView()
        self.UI.show()
        sys.exit(app.exec_())

    # button_1 event
    def button1_event(self):
        b1 = self.UI.button_1

    # button_2 event
    def button2_event(self):
        b2 = self.UI.button_2

    # button_3 event
    def button3_event(self):
        b3 = self.UI.button_3

        if b3.text() == "Credit":
            self.UI.credit()

    # button_4 event
    def button4_event(self):
        b4 = self.UI.button_4
