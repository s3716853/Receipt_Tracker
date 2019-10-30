from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget, QStackedWidget, QListWidget
from PyQt5.QtCore import Qt
from MenuBar import menu_bar
from ReceiptPrintOut import receipt_printout
from InputForm import input_form

class receipt_entry(QWidget):
   
    stack = None
    __model = None

    def __init__(self, model):
        super().__init__()
        self.__model = model
        self.setWindowTitle("Receipt Tracker")

        outer_layout = QVBoxLayout()
        main_layout = QHBoxLayout()
        outer_layout.addWidget(menu_bar(self.__model))
        outer_layout.addLayout(main_layout)

        leftlist = QComboBox()
        leftlist.adjustSize()
        leftlist.currentIndexChanged.connect(self.display)

        self.stack = QStackedWidget()
        for name in self.__model.get_names():
            self.stack.addWidget(receipt_printout(name, self.__model))
            leftlist.addItem(name)
        
        receipt_layout = QVBoxLayout()
        receipt_layout.addWidget(leftlist)
        receipt_layout.addWidget(self.stack)

        main_layout.addLayout(receipt_layout)

        main_layout.addWidget(input_form(self.__model))

        self.setLayout(outer_layout)

    def display(self,i):
        self.stack.setCurrentIndex(i)