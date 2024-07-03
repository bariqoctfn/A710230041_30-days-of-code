import sys
from PyQt5.QtGui import *
from orderplus import CafeOrderApp
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    gui = CafeOrderApp()
    gui.setWindowTitle("Cafe Order")
    gui.setWindowIcon(QIcon("US.png"))
    gui.setGeometry(600,200,600,700)
    gui.show()
    


    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()