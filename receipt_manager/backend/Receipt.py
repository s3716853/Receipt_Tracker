from backend.ReceiptLine import ReceiptLine

class Receipt:
    __receipt_lines = None

    def __init__(self):
        self.__receipt_lines = list()
    
    def add_line(self, item, percent_contribute):
        self.__receipt_lines.append(ReceiptLine(item, percent_contribute))

    def to_string(self):
        string = ""
        for receipt_line in self.__receipt_lines:
            string = string + receipt_line.to_string() + "\n"
        
        return string

    def to_string_set(self):
        receipt_lines = list()

        for receipt_line in self.__receipt_lines:
            receipt_lines.append(receipt_line.to_string())

        return receipt_lines
        
    def get_owed(self):
        total = 0
        for receipt_line in self.__receipt_lines:
            total = total + receipt_line.get_owed()
        
        return total
