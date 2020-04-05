import datetime
import Loggers


class Car:
    def __init__(self, entry_time=datetime.datetime.now(), exit_time=None, ticket_number=0, car_id=None):
        self.id = car_id
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.ticket_number = ticket_number
        # self.logger = Loggers.car_XXlogger

        # self.logger.info("Car created with entry time {}, ticket number {}".format(self.entry_time, self.ticket_number))

    @property
    def get_entry_time(self):
        return self.entry_time

    @get_entry_time.setter
    def set_entry_time(self, entry_time):
        self.entry_time = entry_time

    @property
    def get_exit_time(self):
        return self.exit_time

    @set_entry_time.setter
    def set_exit_time(self, exit_time):
        self.exit_time = exit_time

    @property
    def get_ticket_number(self):
        return self.ticket_number

    @get_ticket_number.setter
    def set_ticket_number(self, value):
        self.ticket_number = value


if __name__ == '__main__':
    car_test = Car()
    print(car_test.ticket_number)
    car_test.ticket_number = 5
    print(car_test.ticket_number)
