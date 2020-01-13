from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget

from frontend.ReceiptChangeListener import receipt_change_listener

class receipt_printout(QWidget, receipt_change_listener):

    name = None
    item_list = None

    def __init__(self, name, model):
        super().__init__()
        self.name = name
        model.add_receipt_listeners(self)
        left_column_layout = QVBoxLayout()
        self.setLayout(left_column_layout)
        self.item_list = QListWidget()
        self.item_list.addItem(name)
        left_column_layout.addWidget(self.item_list)

        self.show()

    def receipt_update(self, model):
        self.item_list.clear()
        for receipt_line in model.receipt_to_string_set(self.name):
            self.item_list.addItem(receipt_line)
        total = "Total: " + str(model.get_total(self.name))
        self.item_list.addItem(total)
        
