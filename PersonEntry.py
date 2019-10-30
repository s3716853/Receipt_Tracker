from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFormLayout, QLineEdit, QDialog
from PyQt5.QtCore import Qt

class person_entry(QDialog):
   
    __receipt_name_entry = None
    __model = None

    def __init__(self, model):
        super().__init__()
        self.__model = model
        self.setWindowTitle("Insert Names")
        self.setFocusPolicy(Qt.StrongFocus)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        #self.name_entry()

        main_layout = QFormLayout()

        self.__receipt_name_entry = QLineEdit()
        main_layout.addRow("Name", self.__receipt_name_entry)

        button_layout = QHBoxLayout()
        add_button = QPushButton('Add')
        end_button = QPushButton('Finish')
        add_button.clicked.connect(self.add_person)
        end_button.clicked.connect(self.finish_entry)
        self.__receipt_name_entry.returnPressed.connect(self.add_person)
        button_layout.addWidget(add_button)
        button_layout.addWidget(end_button)

        main_layout.addRow(button_layout)

        self.setLayout(main_layout)

    def add_person(self):
        self.__model.add_person(self.__receipt_name_entry.text())
        self.__receipt_name_entry.clear()

    def finish_entry(self):
        self.close()