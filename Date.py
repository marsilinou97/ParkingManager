import ParkingLot


class Date:
    def __init__(self, parkinglot_a, date_year, date_month, date_day,):
        self.parkinglot_a = parkinglot_a
        self.date_year = date_year
        self.date_month = date_month
        self.date_day = date_day

    def get_year(self):
        return self.date_year

    def get_month(self):
        return self.date_month

    def get_day(self):
        return self.date_day

    def set_rate(self, value):
        self.date_rate = value

    def set_open_spaces(self, value):
        self.date_open_spaces = value
