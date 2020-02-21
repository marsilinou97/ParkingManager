class Keycard:
	def __init__(self, keycard_number, keycard_owner_id, keycard_status):
			self._keycard_number = keycard_number
			self._keycard_owner_id = keycard_owner_id
			self._keycard_status = keycard_status
			
	def get_number(self):
		return self._keycard_number
	
	def get_owner_id(self):
		return self._keycard_owner_id
	
	def get_status(self):
		return self._keycard_status
	
	def set_number(self, value):
		self.__keycard_number = value
	
	def set_owner_id(self, value):
		self.__keycard_owner_id = value
		
	def set_status(self, value):
		self.__keycard_status = value
