from PyQt5.QtWidgets import QVBoxLayout, QWidget, QCheckBox

class person_select_checkboxes(QWidget):
    owed_people_checkboxes = None
    
    def __init__(self, names):
        super().__init__()
        self.owed_people_checkboxes = set()
        checkbox_layout = QVBoxLayout()
        
        for name in names:
            checkbox = QCheckBox(name)
            self.owed_people_checkboxes.add(checkbox)
            checkbox_layout.addWidget(checkbox)

        self.setLayout(checkbox_layout)
        self.show()

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