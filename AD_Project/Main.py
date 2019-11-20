from Controller import Controller

from PyQt5.QtWidgets import QApplication, QWidget


def gameMain(app):
    game = Controller()
    game.start(app)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gameMain(app)
