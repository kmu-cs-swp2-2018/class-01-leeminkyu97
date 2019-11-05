from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from keypad import *
from calcFunctions import *


class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height()+20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(30)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons':numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionLabels, 'layout': funcLayout, 'columns': 1}
        }

        for label in buttonGroups.keys():
            r, c = 0, 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0
                    r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        mainLayout.addLayout(constLayout, 2, 0)

        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        errorList = ['ZeroDivisionErr', 'IndexErr', 'OverFlowErr',
                     'TypeErr', 'ValueErr', 'SyntaxErr', 'etcErr']

        if self.display.text() in errorList:
            self.display.setText('')  # after error

        if key == 'pi':
            key = '3.141592'
        elif key == '빛의 이동 속도 (m/s)':
            key = '3E+8'
        elif key == '소리의 이동 속도 (m/s)':
            key = '340'
        elif key == '태양과의 평균 거리 (km)':
            key = '1.5E+8'

        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except ZeroDivisionError:  # divided by 0
                result = 'ZeroDivisionErr'
            except IndexError:  # over/under indexing
                result = 'IndexErr'
            except OverflowError:  # overflow (could be memory err)
                result = 'OverflowErr'
            except TypeError:  # wrong arg (data type)
                result = 'TypeErr'
            except ValueError:  # wrong arg (ex. big number)
                result = 'ValueErr'
            except SyntaxError:
                result = 'SyntaxErr'
            except:
                result = 'etcErr'
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        elif key in functionLabels:
            index = functionLabels.index(key)
            value = eval("%s(%s)" %(functions[index], self.display.text()))
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)
        self.repaint()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
