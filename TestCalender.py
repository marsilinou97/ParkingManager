import calendar
import copy
weekdays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]


class TestCalender:

    def __init__(self, year):
        self.year = year
        self.months = []
        calendar.setfirstweekday(calendar.SUNDAY)
        for month in range(1, 13):
            self.months.append(calendar.monthcalendar(year, month))
        self.rates = []
        self.rates = copy.deepcopy(self.months)

    def set_default_rate(self, value):
        for i in range(0, 12):
            for j in range(0, len(self.months[i])):
                for k in range(0, 7):
                    if self.rates[i][j][k] != 0:
                        self.rates[i][j][k] = value

    def set_rate(self, month, day, value):
        counter = 0
        for j in range(0, len(self.rates[month - 1])):
            for k in range(0, 7):
                if self.months[month - 1][j][k] == day:
                    self.rates[month - 1][j][k] = value
                    counter = 1
        if counter == 0:
            print("Date does not exist. No changes were made")
        else:
            print("Rate for " + str(month) + "-" + str(day) + " has been set to " + str(value))

    def set_rate_range(self, month, day1, day2, value):
        counter = 0
        for j in range(0, len(self.rates[month - 1])):
            for k in range(0, 7):
                if self.months[month - 1][j][k] >= day1 and self.months[month-1][j][k] <= day2:
                    self.rates[month - 1][j][k] = value
                    counter = 1
        if counter == 0:
            print("Date does not exist. No changes were made")
        else:
            print("Rate between " + str(month) + "-" + str(day1) + " and " + str(day2) + " has been set to " + str(value))

    def show_rates(self, month):
        temp = ""
        print(str(weekdays) + "\n")
        for j in range(0, len(self.rates[month - 1])):
            print(str(self.rates[month - 1][j]) + "\n")

    def show_month(self, month):
        print(str(weekdays) + "\n")
        for j in range(0, len(self.months[month - 1])):
            print(str(self.months[month - 1][j]) + "\n")

    def get_yearly(self):
        return calendar.calendar(self.year)

    def get_year(self):
        return self.year
