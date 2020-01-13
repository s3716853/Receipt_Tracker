from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget, QStackedWidget, QListWidget
from PersonChangeListener import person_change_listener
from ReceiptPrintOut import receipt_printout

class receipt_view(QWidget, person_change_listener):

    __receipt_printouts = None
    __receipt_stack = None
    __person_list = None
    __model = None

    def __init__(self, model):
        super().__init__()
        self.__model = model
        self.__model.add_person_change_listeners(self)
        self.__receipt_printouts = list()
        # self.setWindowTitle("Receipt Tracker")

        self.__person_list = QComboBox()
        self.__person_list.adjustSize()
        self.__person_list.currentIndexChanged.connect(self.display)

        self.__receipt_stack = QStackedWidget()
        # for name in self.__model.get_names():
        #     printout = receipt_printout(name, self.__model)
        #     self.__receipt_printouts.add(printout)
        #     self.__receipt_stack.addWidget(printout)
        #     self.__person_list.addItem(name)
        
        receipt_layout = QVBoxLayout()
        receipt_layout.addWidget(self.__person_list)
        receipt_layout.addWidget(self.__receipt_stack)

        self.setLayout(receipt_layout)
        self.show()

    def display(self,i):
        self.__receipt_stack.setCurrentIndex(i)

    def person_update(self, model):
        for printout in self.__receipt_printouts:
            self.__receipt_stack.removeWidget(printout)
            
        for name in model.get_names():
            in_set = False
            for printout in self.__receipt_printouts:
                if name == printout.name:
                    in_set = True
            if not in_set:
                self.__receipt_printouts.append(receipt_printout(name, model))
                self.__person_list.addItem(name)
        
        for printout in self.__receipt_printouts:
            self.__receipt_stack.addWidget(printout)

        