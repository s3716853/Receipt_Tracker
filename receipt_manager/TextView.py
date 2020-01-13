from Item import Item
from ReceiptTracker import ReceiptTracker

#https://pythonspot.com/python-database-programming-sqlite-tutorial/

class TextView():
    def __init__(self):
        print("*** Welcome to Receipt Tracker ***")
    
    def menu(self):
        end_program = False
        user_input = None
        
        while end_program != True:
            print('Enter "S" to enter main program')
            print('Enter "X" to exit the program')
            user_input = input(">>> ")
            if user_input.upper() == 'S':
                self.ReceiptTracking()
            elif user_input.upper() == 'X':
                end_program = True
            else:
                print('---INCORRECT INPUT---')

    def ReceiptTracking(self):
        print('*** Receipt Tracker ***')
        print('Enter your friend\'s names (type END once all are entered)')

        names_entered = False
        receipts = dict()
        key = 0
        while names_entered != True:
            name = input(">>> ")
            if name.upper() == 'END':
                names_entered = True
            else:
                receipts[key] = ReceiptTracker(name)
                key = key + 1
        
        items_entered = False

        while items_entered != True:
            print('Enter Item Name (type END to stop entering items)')
            name = input(">>> ")
            if name.upper() == 'END':
                items_entered = True
            else:
                input_ok = False
                print('Enter Item Cost (type END to stop entering items)')
                
                while not input_ok:
                    try:
                        cost = input(">>> ")
                        if cost.upper() == 'END':
                            items_entered = True
                            input_ok = True
                        else:
                            input_ok = True
                            cost = float(cost)
                    except ValueError:
                        print("----INPUT NUMBER ONLY (DECIMAL ALLOWED)----")

                print("Enter the number of each person (type END when done)")
                for key in receipts:
                    print(str(key) + " - " + receipts[key].get_name())

                people_entered = False
                people = set()

                while people_entered != True:
                    key = input(">>> ")
                    if key.upper() == 'END':
                        people_entered = True
                    elif not key.isdigit():
                        print("----KEY INVALID----")
                    elif int(key) in receipts:
                        people.add(int(key))
                    else:
                        print("----KEY INVALID----")

                item = Item(name, cost)
                for key in people:
                    receipts[key].add_receipt_line(item, 1/(len(people)+1))
    

        for receipt in receipts.values():
            print(receipt.to_string())