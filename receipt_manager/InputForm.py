from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget
from PersonSelectCheckboxes import person_select_checkboxes

class input_form(QWidget):
    
    checkbox = None
    add_button = None
    model = None
    item_name_entry = None
    item_cost_entry = None

    def __init__(self, model):
        super().__init__()
        self.model = model

        self.checkbox = person_select_checkboxes(self.model.get_names())
        self.model.add_person_change_listeners(self.checkbox)
        right__column_layout = QFormLayout()
        self.setLayout(right__column_layout)

        self.item_name_entry = QLineEdit()
        self.item_cost_entry = QLineEdit()
        right__column_layout.addRow("Item Name", self.item_name_entry)
        right__column_layout.addRow("Item Cost", self.item_cost_entry)

        right__column_layout.addRow("Contributed",self.checkbox)


        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_item)
        right__column_layout.addRow(self.add_button)

        self.show()
    
    def add_item(self):
        people = self.checkbox.get_selected()
        if len(people) != 0:
            try:
                self.model.add_receipt_line(people, self.item_name_entry.text(), self.item_cost_entry.text())
                self.item_name_entry.clear()
                self.item_cost_entry.clear()
                self.checkbox.clear()
            except TypeError as error:
                print("TYPE ERROR")
        else:
            print("SET EMPTY")