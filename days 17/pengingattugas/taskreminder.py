import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox

class TaskReminder(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Task Reminder')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Enter a new task')
        self.add_button = QPushButton('Add Task', self)
        self.add_button.clicked.connect(self.addTask)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        self.task_list = QListWidget(self)


        self.delete_button = QPushButton('Delete Selected Task', self)
        self.delete_button.clicked.connect(self.deleteTask)

        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def addTask(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Task cannot be empty')

    def deleteTask(self):
        selected_task = self.task_list.currentItem()
        if selected_task:
            self.task_list.takeItem(self.task_list.row(selected_task))
        else:
            QMessageBox.warning(self, 'Warning', 'No task selected')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TaskReminder()
    ex.show()
    sys.exit(app.exec_())
