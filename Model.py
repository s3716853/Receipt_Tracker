from ReceiptTracker import ReceiptTracker
from Item import Item

class model():
    receipts = None
    receipt_change_listeners = None
    person_change_listeners = None

    def __init__(self):
        self.receipts = set()
        self.receipt_change_listeners = set()
        self.person_change_listeners = set()

    def get_names(self):
        names = set()
        for receipt in self.receipts:
            names.add(receipt.get_name())
        
        return names

    def add_receipt_line(self, people, name, cost):
        shared_item = Item(name, cost)
        print(cost)
        try:
           float(cost)
        except ValueError as error:
            raise TypeError

        for receipt in self.receipts:
            for person in people:
                if person == receipt.get_name():
                    receipt.add_receipt_line(shared_item, 1/(len(people)+1))
        
        self.update_receipt_listeners()
    
    def update_receipt_listeners(self):
        for receipt_listener in self.receipt_change_listeners:
            receipt_listener.receipt_update(self)
    
    def add_receipt_listeners(self, receipt_listener):
        self.receipt_change_listeners.add(receipt_listener)

    #returns whole receipt as string
    def receipt_to_string(self, receipt_name):
        return_string = ""

        for receipt in self.receipts:
            #print(receipt_name, receipt.get_name())
            if receipt_name == receipt.get_name():
                return_string = receipt.to_string()
        
        return return_string

    #returns set of receipt lines as strings
    def receipt_to_string_set(self, receipt_name):
        receipt_lines_strings = None

        for receipt in self.receipts:
            if receipt_name == receipt.get_name():
                receipt_lines_strings = receipt.to_string_set()
        
        return receipt_lines_strings

    def add_person(self, name):
        print(name)
        if name not in self.get_names():
            self.receipts.add(ReceiptTracker(name))
        for listener in self.person_change_listeners:
            listener.person_update(self)
    
    def add_person_change_listeners(self, listener):
        self.person_change_listeners.add(listener)
    
    # def remove_person(self, name):
    #     for receipt in self.receipts:
    #         if receipt.name == name:
    #             receipts.remove(receipt)

    def get_total(self, name):
        total = 0
        for receipt in self.receipts:
            if name == receipt.get_name():
                total = receipt.get_owed()
        return total