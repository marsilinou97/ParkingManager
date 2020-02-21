import datetime

class Validation:
    def __init__(self, validation_name, validation_quantity, validation_type, validation_amount, start_date, end_date, ):
        self._validation_name = validation_name
        self._validation_quantity = validation_quantity
        self._validation_type = validation_type
        self._validation_amount = validation_amount
        self._start_date = start_date
        self._end_date = end_date

            
    def get_validation_name(self):
        return self.__validation_name
    
    def get_validation_type(self):
        return self.__validation_type
       
    def get_validation_amount(self):
        return self.__validation_amount
    
    def get_validation_quantity(self):
        return self.__validation_quantity
    
    def get_start_date(self):
        return self.__start_date
    
    def get_end_date(self): 
        return self.__end_date
    
    def set_validation_name(self, value):
        self.__validation_name = value
        
    def set_validation_type(self, value):
        self.__validation_type = value
    
    def set_validation_amount(self, value):
        self.__validation_amount = value
        
    def set_validation_quantity(self, value):
        self.__validation_quantity = value
        
    def set_start_date(self, value):
        self.__start_date = value
        
    def set_end_date(self, value):
        self.__end_date = value
        
        
        
        
        