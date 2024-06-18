import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QDate

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplikasi Kalender")
        self.setGeometry(100, 100, 400, 300)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.show_date)

        self.label = QLabel(self)
        self.label.setText("Tanggal yang dipilih: Tidak ada")

        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.label)
    
    def show_date(self, date):
        self.label.setText(f"Tanggal yang dipilih: {date.toString()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())
