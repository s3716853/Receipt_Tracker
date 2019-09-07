class ReceiptLine:
    __item = None
    __percent_contribute = None

    def __init__(self, item, percent_contribute):
        self.__item = item
        self.__percent_contribute = percent_contribute

    def to_string(self):
        return "Item: " + self.__item.get_name() + " Price: " + str(self.__item.get_price()) + " Owed: " + str(self.get_owed())

    def get_owed(self):
        return float(self.__item.get_price())*(float(self.__percent_contribute))