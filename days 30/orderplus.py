from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QSpinBox
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

class CafeOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        main_layout = QVBoxLayout()

        self.menu_label = QLabel('MENU')
        self.menu_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.menu_label)
   
        namalayout = QHBoxLayout()
        main_layout.addLayout(namalayout)
        self.nama = QLabel('Nama :')
        namalayout.addWidget(self.nama)
        self.isinama = QLineEdit()
        namalayout.addWidget(self.isinama)


        
        menu_layout = QVBoxLayout()
        self.menu_widget_list = []
        self.menu_items = {
            'Americano': 24000,
            'Vanila Latte': 25000,
            'Coffee Latte': 25000,
            'Espresso': 21000,
            'Lemon Tea': 10000,
            'Roti bakar': 15000,
            'French': 16000
        }

        for item in self.menu_items.keys():
            item_layout = QHBoxLayout()

            item_label = QLabel(item)
            item_layout.addWidget(item_label)

            item_quantity_spinbox = QSpinBox()
            item_quantity_spinbox.setRange(0, 100)
            item_layout.addWidget(item_quantity_spinbox)

            self.menu_widget_list.append((item_label, item_quantity_spinbox))

            menu_layout.addLayout(item_layout)

        main_layout.addLayout(menu_layout)

        self.add_to_cart_button = QPushButton('Tambahkan')
        self.add_to_cart_button.clicked.connect(self.add_to_cart)
        main_layout.addWidget(self.add_to_cart_button)

        self.cart_label = QLabel('Pesanan:')
        main_layout.addWidget(self.cart_label)

        self.cart_list = QListWidget()
        main_layout.addWidget(self.cart_list)

        self.total_label = QLabel('Total: Rp 0')
        main_layout.addWidget(self.total_label)

        self.reset = QPushButton('Pesan')
        main_layout.addWidget(self.reset)
        self.reset.clicked.connect(self.pesan)

        self.setLayout(main_layout)

        self.cart_items = {}

    def add_to_cart(self):
        name = self.isinama.text()
        if not name :
            self.cart_list.addItem('Nama harus diisi.')
            return
        for item_label, item_quantity_spinbox in self.menu_widget_list:
            item_name = item_label.text()
            quantity = item_quantity_spinbox.value()
            if quantity > 0:
                if item_name in self.cart_items:
                    self.cart_items[item_name] += quantity
                else:
                    self.cart_items[item_name] = quantity
                item_quantity_spinbox.setValue(1) 
        self.update_cart_display()
        self.update_total()

    def update_cart_display(self):
        self.cart_list.clear()
        name = self.isinama.text()
        self.cart_list.addItem(f'Nama : {name}')
        for item_name, quantity in self.cart_items.items():
            self.cart_list.addItem(f'{item_name} x {quantity} - Rp {self.menu_items[item_name] * quantity}')

    def update_total(self):
        total = 0
        for item_name, quantity in self.cart_items.items():
            total += self.menu_items[item_name] * quantity
        self.total_label.setText(f'Total: Rp {total}')

    def pesan(self):
        self.cart_list.clear()
        self.total_label.clear()
        self.isinama.clear()