from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget, QStackedWidget, QListWidget
from PyQt5.QtCore import QObject, pyqtSignal
from Model import model
from InputForm import input_form
from ReceiptPrintOut import receipt_printout
from PersonEntry import person_entry
from MenuBar import menu_bar

class GuiView():
    
    model = None
    stack = None

    #https://www.tutorialspoint.com/pyqt/pyqt_basic_widgets.htm

    def __init__(self):
        self.model = model()

    def menu(self):
        self.name_insert()
        self.tracker()

    def name_insert(self):
        person_entry(self.model)

    def tracker(self):
        app = QApplication([])
        window = QWidget()
        window.setWindowTitle("Receipt Tracker")
        
        outer_layout = QVBoxLayout()
        main_layout = QHBoxLayout()
        outer_layout.addWidget(menu_bar(self.model))
        outer_layout.addLayout(main_layout)

        leftlist = QComboBox()
        leftlist.adjustSize()
        leftlist.currentIndexChanged.connect(self.display)

        self.stack = QStackedWidget()
        for name in self.model.get_names():
            self.stack.addWidget(receipt_printout(name, self.model))
            leftlist.addItem(name)
        
        receipt_layout = QVBoxLayout()
        receipt_layout.addWidget(leftlist)
        receipt_layout.addWidget(self.stack)

        main_layout.addLayout(receipt_layout)

        main_layout.addWidget(input_form(self.model))

        window.setLayout(outer_layout)
        window.show()
        app.exec_()

    def display(self,i):
        self.stack.setCurrentIndex(i)
