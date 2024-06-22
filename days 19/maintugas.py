import sys
from PyQt5.QtWidgets import QApplication, QDialog
from tugas import Ui_Dialog

class TugasDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.hitung_pajak)

    def hitung_pajak(self):
        harga = float(self.ui.lineEdit.text())
        pajak_persen = float(self.ui.comboBox.currentText().strip('%'))
        pajak = harga * (pajak_persen / 100)
        total_harga = harga + pajak
        self.ui.label_3.setText(f"Total Harga Beserta Pajak Adalah: {total_harga:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = TugasDialog()
    dialog.show()
    sys.exit(app.exec_())
