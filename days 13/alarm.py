import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QTimeEdit, QWidget, QMessageBox
from PyQt5.QtCore import QTimer, QTime
import datetime

class JamAlarm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jam Alarm")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Atur Waktu Alarm :", self)
        self.layout.addWidget(self.label)

        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("HH:mm")
        self.layout.addWidget(self.time_edit)

        self.set_button = QPushButton("Atur Alarm", self)
        self.set_button.clicked.connect(self.set_alarm)
        self.layout.addWidget(self.set_button)

        self.status_label = QLabel("", self)
        self.layout.addWidget(self.status_label)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.alarm_time = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_alarm)

    def set_alarm(self):
        self.alarm_time = self.time_edit.time()
        self.status_label.setText(f"Jam Alarm Diatur Tepat {self.alarm_time.toString('HH:mm')}")
        self.timer.start(1000)

    def check_alarm(self):
        current_time = QTime.currentTime()
        if self.alarm_time is not None and current_time >= self.alarm_time:
            self.timer.stop()
            self.show_alarm()

    def show_alarm(self):
        QMessageBox.information(self, "Alarm", "BANGUN TOLOL!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JamAlarm()
    window.show()
    sys.exit(app.exec_())
