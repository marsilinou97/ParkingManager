class ParkingLot:
    def __init__(self, parkinglot_name, parkinglot_address, parkinglot_hours, parkinglot_total_spaces, parkinglot_available_spaces, parkinglot_rate ):
        self._parkinglot_name = parkinglot_name
        self._parkinglot_address = parkinglot_address
        self._parkinglot_hours = parkinglot_hours
        self._parkinglot_total_spaces = parkinglot_total_spaces
        self._parkinglot_available_spaces = parkinglot_available_spaces
        self._parkinglot_rate = parkinglot_rate
    
    def get_name(self):
        return self._parkinglot_name
    
    def get_address(self):
        return self._parkinglot_address
    
    def get_hours(self):
        return self._parkinglot_hours
    
    def get_total_spaces(self):
        return self._parkinglot_total_spaces
    
    def get_available_spaces(self):
        return self._parkinglot_available_spaces
    
    def get_rate(self):
        return self._parkinglot_rate
    
    def set_name(self, value):
        self._parkinglot_name = value
        
    def set_address(self, value):
        self._parkinglot_address = value
        
    def set_hours(self, value):
        self._parkinglot_hours = value
        
    def set_total_spaces(self, value):
        self._parkinglot_total_spaces = value
        
    def set_available_spaces(self, value):
        self._parkinglot_available_spaces = value
        
    def set_rate(self, value):
        self._parkinglot_rate = value