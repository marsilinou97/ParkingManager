class User:
    def __init__(self, first_name, last_name, address, phone, user_id, start_date, access_level):
        self.__user_first_name = first_name
        self.__user_last_name = last_name
        self.__user_address = address
        self.__user_telephone_number = phone
        self.__user_id = user_id
        self.__user_start_date = start_date
        self.__user_access_level = access_level

    def get_firstname(self):
        """

        @return:
        """
        return self.__user_first_name

    def get_lastname(self):
        """

        @return:
        """
        return self.__user_last_name

    def get_address(self):
        """

        @return:
        """
        return self.__user_address

    def get_telephone_number(self):
        """

        @return:
        """
        return self.__user_telephone_number

    def get_id(self):
        """

        @return:
        """
        return self.__user_id

    def get_start_date(self):
        """

        @return:
        """
        return self.__user_start_date

    def get_access_level(self):
        """

        @return:
        """
        return self.__user_access_level

    def set_firstname(self, value):
        """

        @return:
        """
        self.__user_first_name = value

    def set_lastname(self, value):
        """

        @return:
        """
        self.__user_last_name = value

    def set_address(self, value):
        """

        @return:
        """
        self.__user_address = value

    def set_telephone_number(self, value):
        """

        @return:
        """
        self.__user_telephone_number = value

    def set_id(self, value):
        """

        @return:
        """
        self.__user_id = value

    def set_start_date(self, value):
        """

        @return:
        """
        self.__user_start_date = value

    def set_access_level(self, value):
        """

        @return:
        """
        self.__user_access_level = value

    def __repr__(self):
        return f"{self.__user_id} - {self.__user_first_name} {self.__user_last_name}"
