from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget, QStackedWidget, QListWidget
from PyQt5.QtCore import Qt

from frontend.MenuBar import menu_bar
from frontend.InputForm import input_form
from frontend.ReceiptView import receipt_view

class receipt_entry(QWidget):

    __model = None

    def __init__(self, model):
        super().__init__()
        self.__model = model
        self.setWindowTitle("Receipt Tracker")

        outer_layout = QVBoxLayout()
        main_layout = QHBoxLayout()
        outer_layout.addWidget(menu_bar(self.__model))
        outer_layout.addLayout(main_layout)

        main_layout.addWidget(receipt_view(self.__model))

        main_layout.addWidget(input_form(self.__model))

        self.setLayout(outer_layout)