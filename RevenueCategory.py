class RevenueCategory:
    def __init__(self, name, quantity, revenue):
        self.name = name
        self.quantity = quantity
        self.revenue = revenue

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def get_revenue(self):
        return self.revenue

    def set_name(self, value):
        self.name = value

    def set_quantity(self, value):
        self.quantity = value

    def set_revenue(self, value):
        self.revenue = value

    def __repr__(self):
        return self.name + "\t" + str(self.quantity) + "\t" + str(self.revenue) + "\n"
    