from Receipt import Receipt

class ReceiptTracker():
    __receipt = None
    __person = None

    def __init__(self, name):
        self.__person = name
        self.__receipt = Receipt()
    
    def add_receipt_line(self, item, percent_contribute):
        self.__receipt.add_line(item, percent_contribute)

    def get_name(self):
        return self.__person
    
    def to_string(self):
        return self.__person + "\n" + self.__receipt.to_string() + "\n" + "Total Owed: " + str(self.__receipt.get_owed())

    def to_string_set(self):
        return self.__receipt.to_string_set()

    def get_owed(self):
        return self.__receipt.get_owed()