import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem

class CafeOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cafe Order App')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.menu_label = QLabel('Menu:')
        layout.addWidget(self.menu_label)

        self.menu_list = QListWidget()
        self.menu_items = {
            'Coffee': 15000,
            'Tea': 10000,
            'Sandwich': 20000,
            'Cake': 25000
        }

        for item, price in self.menu_items.items():
            list_item = QListWidgetItem(f'{item} - Rp {price}')
            self.menu_list.addItem(list_item)
        layout.addWidget(self.menu_list)

        self.add_to_cart_button = QPushButton('Add to Cart')
        self.add_to_cart_button.clicked.connect(self.add_to_cart)
        layout.addWidget(self.add_to_cart_button)

        self.cart_label = QLabel('Cart:')
        layout.addWidget(self.cart_label)

        self.cart_list = QListWidget()
        layout.addWidget(self.cart_list)

        self.total_label = QLabel('Total: Rp 0')
        layout.addWidget(self.total_label)

        self.setLayout(layout)

        self.cart_items = []

    def add_to_cart(self):
        selected_items = self.menu_list.selectedItems()
        for item in selected_items:
            self.cart_list.addItem(item.text())
            self.cart_items.append(item.text())

        self.update_total()

    def update_total(self):
        total = 0
        for item in self.cart_items:
            item_name = item.split(' - ')[0]
            total += self.menu_items[item_name]
        self.total_label.setText(f'Total: Rp {total}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CafeOrderApp()
    ex.show()
    sys.exit(app.exec_())
