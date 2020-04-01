import datetime

class Report:
    def __init__(self, issued_on, start_range, end_range, revenue_categories, payment_categories):
        self.issued_on = issued_on
        self.start_range = start_range
        self.end_range = end_range
        self.revenue_categories = revenue_categories
        self.payment_categories = payment_categories

    def get_issued_on(self):
        return self.issued_on

    def get_start_range(self):
        return self.start_range

    def get_end_range(self):
        return self.end_range

    def get_revenue_categories(self):
        return self.revenue_categories

    def get_payment_categories(self):
        return self.payment_categories

    def set_issued_on(self, value):
        self.issued_on = value

    def set_start_range(self, value):
        self.start_range = value;

    def set_end_range(self, value):
        self.end_range = value;

    def set_payment_categories(self, value):
        self.payment_categories = value

    def set_revenue_categories(self, value):
        self.revenue_categories = value

    def __repr__(self):
        string = ""
        for a in self.revenue_categories:
            string += (str)(a);
        string2 = ""
        for a in self.payment_categories:
            string2 += (str)(a);
        return str(self.start_range) + "  ---  " + str(self.end_range) + "\n" + string + string2
