import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(200, 200, 300, 300)

        self.layout = QVBoxLayout()

        self.entry = QLineEdit()
        self.entry.setReadOnly(True)
        self.layout.addWidget(self.entry)

        buttons = [
            ('7', self.on_button_clicked),
            ('8', self.on_button_clicked),
            ('9', self.on_button_clicked),
            ('/', self.on_button_clicked),
            ('4', self.on_button_clicked),
            ('5', self.on_button_clicked),
            ('6', self.on_button_clicked),
            ('*', self.on_button_clicked),
            ('1', self.on_button_clicked),
            ('2', self.on_button_clicked),
            ('3', self.on_button_clicked),
            ('-', self.on_button_clicked),
            ('0', self.on_button_clicked),
            ('.', self.on_button_clicked),
            ('=', self.calculate),
            ('+', self.on_button_clicked),
            ('C', self.clear_entry),]

        for label, func in buttons:
            button = QPushButton(label)
            button.clicked.connect(func)
            self.layout.addWidget(button)

        self.setLayout(self.layout)

    def on_button_clicked(self):
        button = self.sender()
        self.entry.setText(self.entry.text() + button.text())

    def clear_entry(self):
        self.entry.clear()

    def calculate(self):
        try:
            result = eval(self.entry.text())
            self.entry.setText(str(result))
        except Exception as e:
            self.entry.setText("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())