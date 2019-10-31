import pickle
import sys
from PyQt5.QtWidgets import QTableWidget, QWidget, QApplication, QGridLayout, QLineEdit, QLabel, QComboBox, QPushButton, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        self.dbfilename = 'assignment6.dat'
        self.initScoreDB()
        self.initUI()
        self.bindData()

    def initScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            self.scoredb = []
        finally:
            fH.close()

    def initUI(self):
        TEXTINPUT_WIDTH = 140
        ELEMENT_HEIGHT = 20
        self.setGeometry(300, 300, 550, 300)
        self.setWindowTitle('Assignment6')

        self.scoreTable = QTableWidget(self)
        self.scoreTable.resize(300, 300)
        self.scoreTable.setColumnCount(3)

        nameLabel = QLabel('Name', self)
        nameLabel.move(310, 0)
        self.name = QLineEdit(self)
        self.name.move(400, 0)
        self.name.resize(TEXTINPUT_WIDTH, ELEMENT_HEIGHT)

        ageLabel = QLabel('Age', self)
        ageLabel.move(310, 20)
        self.age = QLineEdit(self)
        self.age.move(400, 20)
        self.age.resize(TEXTINPUT_WIDTH, ELEMENT_HEIGHT)
        self.age.setValidator(QIntValidator())

        scoreLabel = QLabel('Score', self)
        scoreLabel.move(310, 40)
        self.score = QLineEdit(self)
        self.score.move(400, 40)
        self.score.resize(TEXTINPUT_WIDTH, ELEMENT_HEIGHT)
        self.score.setValidator(QIntValidator())

        amountLabel = QLabel('Amount', self)
        amountLabel.move(310, 60)
        self.amount = QLineEdit(self)
        self.amount.move(400, 60)
        self.amount.resize(TEXTINPUT_WIDTH, ELEMENT_HEIGHT)
        self.amount.setValidator(QIntValidator())

        self.addButton = QPushButton('Add', self)
        self.addButton.resize(230, ELEMENT_HEIGHT + 5)
        self.addButton.move(310, 80)

        self.deleteButton = QPushButton('Delete by name', self)
        self.deleteButton.resize(230, ELEMENT_HEIGHT + 5)
        self.deleteButton.move(310, 105)

        self.filterButton = QPushButton('Filter by name', self)
        self.filterButton.resize(230, ELEMENT_HEIGHT + 5)
        self.filterButton.move(310, 130)

        self.increaseButton = QPushButton('Increase score', self)
        self.increaseButton.resize(230, ELEMENT_HEIGHT + 5)
        self.increaseButton.move(310, 155)

        self.sortKey = QComboBox(self)
        self.sortKey.addItems(['Age', 'Score'])
        self.sortKey.resize(230, ELEMENT_HEIGHT)
        self.sortKey.move(310, 250)

        self.sortButton = QPushButton('Sort by key', self)
        self.sortButton.resize(230, ELEMENT_HEIGHT + 5)
        self.sortButton.move(310, 270)

        self.show()

    def bindData(self):
        self.addButton.clicked.connect(self.addScore)
        self.deleteButton.clicked.connect(self.deleteScoreByName)
        self.filterButton.clicked.connect(self.filterByName)
        self.increaseButton.clicked.connect(self.increaseScore)
        self.sortButton.clicked.connect(self.sortByKey)

        self.resetTable()

    def addScore(self):
        self.scoredb.append([self.name.text(), self.age.text(), self.score.text()])
        self.resetTable()

    def deleteScoreByName(self):
        self.scoredb = [x for x in self.scoredb if x[0] != self.name.text()]
        self.resetTable()

    def filterByName(self):
        if self.name.text() == '':
            filterdRows = self.scoredb
        else:
            filterdRows = [x for x in self.scoredb if x[0] == self.name.text()]

        self.resetTable(filterdRows)

    def increaseScore(self):
        for i in range(len(self.scoredb)):
            if self.scoredb[i][0] == self.name.text():
                self.scoredb[i][2] = str(int(self.scoredb[i][2]) + int(self.amount.text()))

        self.resetTable()

    def sortByKey(self):
        self.resetTable(sorted(self.scoredb, key=lambda scoredb: int(scoredb[self.sortKey.currentIndex() + 1])))

    def resetTable(self, rows=False):
        if not rows:
            rows = self.scoredb
        self.scoreTable.setRowCount(0)
        self.scoreTable.setRowCount(len(rows))
        self.scoreTable.setHorizontalHeaderLabels(['Name', 'Age', 'Score'])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.scoreTable.setItem(i, j, QTableWidgetItem(rows[i][j]))


    def closeEvent(self, event):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())