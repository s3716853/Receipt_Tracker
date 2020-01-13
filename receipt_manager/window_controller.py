from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFormLayout, QLineEdit, QComboBox, QTabWidget, QStackedWidget, QListWidget
from PyQt5.QtCore import QObject, pyqtSignal

from Model import model
from PersonEntry import person_entry
from ReceiptEntry import receipt_entry

class WindowController():
    
    __person_entry = None
    __receipt_entry = None

    def __init__(self, person_entry, receipt_entry):
        self.__person_entry = person_entry
        self.__receipt_entry = receipt_entry