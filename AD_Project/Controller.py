import sys
from UI import mainUI

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QApplication, QWidget


class controller:
    def __init__(self):
        self.UI = mainUI()

    # game start
    def start(self, app):
        self.UI.mainView()
        self.UI.show()
        sys.exit(app.exec_())

