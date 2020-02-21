class User:
    def __init__(self, user_first_name, user_last_name, user_address, 
        user_telephone_number, user_id, user_password, user_start_date, user_access_level):
        self._user_first_name = user_first_name
        self._user_last_name = user_last_name
        self._user_address = user_address
        self._user_telephone_number = user_telephone_number
        self._user_id = user_id
        self._user_password = user_password
        self._user_start_date = user_start_date
        self._user_access_level = user_access_level
        
    def get_firstname(self):
        return self.__user_firstname
    
    def get_lastname(self):
        return self.__user_lastname
    
    def get_address(self):
        return self.__user_address
    
    def get_telephone_number(self):
        return self.__user_telephone_number
    
    def get_id(self):
        return self.__user_id
    
    def get_password(self):
        return self.__user_password
    
    def get_start_date(self):
        return self.__user_start_date
    
    def get_access_level(self):
        return self.__user_access_level
    
    def set_firstname(self, value):
        self.__user_firstname = value
    
    def set_lastname(self, value):
        self.__user_lastname = value    
    
    def set_address(self, value):
        self.__user_address = value   
    
    def set_telephone_number(self, value):
        self.__user_telephone_number = value 
        
    def set_id(self, value):
        self.__user_id = value 
        
    def set_password(self, value):
        self.__user_password = value   
        
    def set_start_date(self, value):
        self.__user_start_date = value   
        
    def set_access_level(self, value):
        self.__user_access_level = value 