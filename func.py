import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from tic import Ui_MainWindow

class TicTac(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TicTac, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TicTac()
    window.show()

    sys.exit(app.exec_())