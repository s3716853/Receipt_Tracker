from PyQt5.QtWidgets import QVBoxLayout, QWidget, QCheckBox
from frontend.PersonChangeListener import person_change_listener

class person_select_checkboxes(QWidget, person_change_listener):
    
    owed_people_checkboxes = None
    checkbox_layout = None
    
    def __init__(self, names):
        super().__init__()
        self.owed_people_checkboxes = set()
        self.checkbox_layout = QVBoxLayout()
        
        self.init_checkboxes(names)

        self.setLayout(self.checkbox_layout)
        # self.show()

    def get_selected(self):
        checked_checkboxes = set()
        for checkbox in self.owed_people_checkboxes:
            if checkbox.isChecked():
                checked_checkboxes.add(checkbox.text())
        print(checked_checkboxes)
        
        return checked_checkboxes

    def clear(self):
        for checkbox in self.owed_people_checkboxes:
            checkbox.setCheckState(False)
    
    def person_update(self, model):
        self.init_checkboxes(model.get_names())

    def init_checkboxes(self, names):
        checkbox_names = set()
        for checkbox in self.owed_people_checkboxes:
            checkbox_names.add(checkbox.text())
        
        for name in names:
            if name not in checkbox_names:
                checkbox = QCheckBox(name)
                self.owed_people_checkboxes.add(checkbox)
                self.checkbox_layout.addWidget(checkbox)