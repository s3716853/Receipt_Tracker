from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget, QStackedWidget, QListWidget
from PyQt5.QtCore import QObject, pyqtSignal

from backend.Model import model
from frontend.PersonEntry import person_entry
from frontend.ReceiptEntry import receipt_entry

class GuiView():
    
    model = None
    __receipt_entry = None
    __person_entry = None
    __app = None

    #https://www.tutorialspoint.com/pyqt/pyqt_basic_widgets.htm

    def __init__(self):
        self.__app = QApplication([])
        self.model = model()

        self.__person_entry = person_entry(self.model)
        self.__receipt_entry = receipt_entry(self.model)
        

    def menu(self):
        self.__person_entry.exec()
        self.__receipt_entry.show()
        self.__app.exec_()
        #self.tracker()
        
    # def name_insert(self):
    #     person_entry(self.model).name_entry()

    # def tracker(self):
    #     pass
    #     #window.show()