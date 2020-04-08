import Loggers
class ParkingLot:
    def __init__(self, parkinglot_name, parkinglot_address, parkinglot_hours, parkinglot_total_spaces,
                 parkinglot_occupied_spaces, parkinglot_rate):

        self.parkinglot_name = parkinglot_name
        self.parkinglot_address = parkinglot_address
        self.parkinglot_hours = parkinglot_hours
        self.parkinglot_total_spaces = parkinglot_total_spaces
        self.parkinglot_occupied_spaces = parkinglot_occupied_spaces
        self.parkinglot_rate = parkinglot_rate
        self.parkinglot_open_spaces = self.parkinglot_total_spaces - self.parkinglot_occupied_spaces
       # self.logger = Loggers.PL_logger
       # self.logger.info("Parking lot created with entry time {}, ticket number {}".format(self.parkinglot_name,
                                                                                          # self.parkinglot_address,
                                                                                          # self.parkinglot_hours,
                                                                                          # self.parkinglot_total_spaces,
                                                                                          # self.parkinglot_occupied_spaces,
                                                                                          # self.parkinglot_rate))

    @property
    def get_name(self):
        return self.parkinglot_name

    @property
    def get_address(self):
        return self.parkinglot_address

    @property
    def get_hours(self):
        return self.parkinglot_hours

    @property
    def get_total_spaces(self):
        return self.parkinglot_total_spaces

    @property
    def get_occupied_spaces(self):
        return self.parkinglot_occupied_spaces

    @property
    def get_rate(self):
        return self.parkinglot_rate

    @property
    def get_open_spaces(self):
        return self.parkinglot_open_spaces


    def set_name(self, value):
        self.parkinglot_name = value

    def set_address(self, value):
        self.parkinglot_address = value

    def set_hours(self, value):
        self.parkinglot_hours = value

    def set_total_spaces(self, value):
        self.parkinglot_total_spaces = value

    def set_occupied_spaces(self, value):
        self.parkinglot_occupied_spaces = value

    def set_rate(self, value):
        self.parkinglot_rate = value

    def set_open_spaces(self, value):
        self.parkinglot_open_spaces = value;


    def get_capacity(self):
        return "Current Capacity is: " + str(self.parkinglot_occupied_spaces) + "/" + str(self.parkinglot_total_spaces)
