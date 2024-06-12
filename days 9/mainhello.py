from PyQt5.QtWidgets import QApplication, QMainWindow
from hello import Ui_hello

class HelloWindow(QMainWindow, Ui_hello):
    def __init__(self, parent=None):
        super(HelloWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
window = HelloWindow()
window.show()
app.exec_()
