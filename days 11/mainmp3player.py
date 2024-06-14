from PyQt5.QtWidgets import QApplication, QDialog
from mp3player import Ui_mp3

class DialogWindow(QDialog, Ui_mp3):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
window = DialogWindow()
window.show()
app.exec_()
