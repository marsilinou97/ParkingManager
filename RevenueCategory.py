class RevenueCategory:
    def __init__(self, name , quantity, revenue):
        self._name = name
        self._quantity = quantity
        self._revenue = revenue

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_revenue(self):
        return self.__revenue

    def set_name(self, value):
        self.__name = value

    def set_quantity(self, value):
        self.__quantity = value

    def set_revenue(self, value):
        self.__revenue = value
    
    def __repr__(self):
        return self._name + " " + str(self._quantity) + " " + str(self._revenue)
    