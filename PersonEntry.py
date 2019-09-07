from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget

class person_entry():
   
    name_entry = None
    model = None
    window = None

    def __init__(self, model):
        self.model = model
        self.name_entry()
    
    def name_entry(self):
        app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle("Insert Names")

        main_layout = QFormLayout()

        self.name_entry = QLineEdit()
        main_layout.addRow("Name", self.name_entry)

        button_layout = QHBoxLayout()
        add_button = QPushButton('Add')
        end_button = QPushButton('Finish')
        add_button.clicked.connect(self.add_person)
        end_button.clicked.connect(self.finish_entry)
        self.name_entry.returnPressed.connect(self.add_person)
        button_layout.addWidget(add_button)
        button_layout.addWidget(end_button)

        main_layout.addRow(button_layout)

        self.window.setLayout(main_layout)
        self.window.show()
        app.exec_()

    def add_person(self):
        self.model.add_person(self.name_entry.text())
        self.name_entry.clear()

    def finish_entry(self):
        self.window.close()