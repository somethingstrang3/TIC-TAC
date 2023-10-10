import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from tic import Ui_MainWindow

class TicTac(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TicTac, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Button.clicked.connect(self.start)

        for i in range(9):
            self.ui.buttons[i].clicked.connect(self.process)

        self.start()


    def start(self):
        self.ui.switcher.button(0).setEnabled(True)
        self.ui.switcher.button(1).setEnabled(True)
        self.ui.switcher.button(1).setChecked(True)
        for i in range(9):
            self.ui.buttons[i].setEnabled(True)
            self.ui.buttons[i].setText("")
        self.ui.status_label.setText("Выберите символ и ходите")

    def process(self):
        self.sender().setText(self.ui.switcher.button(self.ui.switcher.checkedId()).text())
        self.sender().setEnabled(False)

        self.ui.switcher.button(0).setEnabled(False)
        self.ui.switcher.button(1).setEnabled(False)
        if self.ui.switcher.checkedId() == 0:
            self.ui.status_label.setText("Ход игрока X")
            self.ui.switcher.button(1).setChecked(True)
        else:
            self.ui.status_label.setText("Ход игрока O")
            self.ui.switcher.button(0).setChecked(True)

        winner = self.checkWinner()


        if not self.checkDraw() and not winner:
            self.ui.status_label.setText("Ничья")


    def checkWinner(self):
        winPos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for pos in winPos:
            if self.ui.buttons[pos[0]].text() == self.ui.buttons[pos[1]].text() == self.ui.buttons[pos[2]].text() == "O":
                for i in range(9):
                    self.ui.buttons[i].setEnabled(False)
                    self.ui.status_label.setText("игрок O выиграл")
                    return True

            if self.ui.buttons[pos[0]].text() == self.ui.buttons[pos[1]].text() == self.ui.buttons[pos[2]].text() == "X":
                for i in range(9):
                    self.ui.buttons[i].setEnabled(False)
                    self.ui.status_label.setText("игрок X выиграл")
                    return True
        return False

    def checkDraw(self):
        for i in range(9):
            if self.ui.buttons[i].isEnabled():
                return True
        return False






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TicTac()
    window.show()

    sys.exit(app.exec_())