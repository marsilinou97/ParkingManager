import datetime

class Report:
    def __init__(self, issued_on, start_range, end_range, revenue_categories):
        self.issue_on = issued_on
        self.start_range  = start_range
        self.end_range = end_rangeX
        self._revenue_categories = revenue_categories

    def get_issued_on(self):
        return self.issued_on

    def get_start_range(self):
        return self.start_range

    def get_date(self):
        return self.date

    def get_revenue_categories(self):
        return self.revenue_categories

    def set_date(self, value):
        self.date = value

    def set_revenue_categories(self, value):
        self.revenue_categories = value
    
    def __repr__(self):
        return str(self.date) + " " +  str(self.revenue_categories)

    