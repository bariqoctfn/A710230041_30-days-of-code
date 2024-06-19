import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import QTimer

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
        self.time_left = 0

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Enter time in seconds:", self)
        self.layout.addWidget(self.label)
        
        self.time_input = QLineEdit(self)
        self.layout.addWidget(self.time_input)
        
        self.start_button = QPushButton("Start Timer", self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)
        
        self.timer_label = QLabel("Time left: 0", self)
        self.layout.addWidget(self.timer_label)
        
        self.setLayout(self.layout)
        
        self.setWindowTitle('Timer App')
        self.show()

    def start_timer(self):
        try:
            self.time_left = int(self.time_input.text())
            self.timer.start(1000)  # Timer triggers every 1 second
        except ValueError:
            self.timer_label.setText("Invalid input! Please enter a number.")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.setText(f"Time left: {self.time_left}")
        else:
            self.timer.stop()
            self.timer_label.setText("Time's up!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerApp()
    sys.exit(app.exec_())
