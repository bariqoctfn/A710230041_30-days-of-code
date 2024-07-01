import sys
from PyQt5.QtGui import *
from orderplus import CafeOrderApp
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CafeOrderApp()
    window.show()
    sys.exit(app.exec_())