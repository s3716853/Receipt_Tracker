from PyQt5.QtWidgets import QWidget, QMenuBar
from PersonEntry import person_entry

class menu_bar(QMenuBar):
    model = None
    def __init__(self, model):
        super().__init__()
        self.model = model

        file = self.addMenu("File")
        add_person = file.addAction("Add Person")
        add_person.setShortcut("Ctrl+A")
        add_person.triggered.connect(self.add_new_person)
        save = file.addAction("Save")
        self.show()

    def add_new_person(self):
        print("ADD")
        
        #person_entry(self.model).name_entry()


