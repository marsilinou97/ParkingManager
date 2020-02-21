import datetime

class Report:
    def __init__(self, date, revenue_categories):
        self._date = date
        self._revenue_categories = revenue_categories

    def get_date(self):
        return self.__date

    def get_revenue_categories(self):
        return self.__revenue_categories

    def set_date(self, value):
        self.__date = value

    def set_revenue_categories(self, value):
        self.__revenue_categories = value
    
    def __repr__(self):
        return str(self._date) + " " +  str(self._revenue_categories)

    