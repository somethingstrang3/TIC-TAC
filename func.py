
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from tic import Ui_MainWindow

class TicTac(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TicTac, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        for i in range(9):
            self.ui.buttons[i].clicked.connect(self.process)







    def process(self):
        self.sender().setText(self.ui.switcher.button(self.ui.switcher.checkedId()).text())
        self.sender().setEnabled(False)

        self.ui.switcher.button(0).setEnabled(False)
        self.ui.switcher.button(1).setEnabled(False)
        if self.ui.switcher.checkedId() == 0:
            self.ui.status_label.setText("ход игрока X")
            self.ui.switcher.button(1).setChecked(True)
        else:
            self.ui.status_label.setText("ход игрока 0")
            self.ui.switcher.button(0).setChecked(True)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTac()
    window.show()
    sys.exit(app.exec_())
