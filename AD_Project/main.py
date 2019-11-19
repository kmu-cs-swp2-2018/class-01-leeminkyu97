from Controller import controller

from PyQt5.QtWidgets import QApplication, QWidget


def gameMain(app):
    game = controller()
    game.start(app)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gameMain(app)
