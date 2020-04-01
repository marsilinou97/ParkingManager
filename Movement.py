import datetime

class Movement:
    def __init__(self, movement_time, transaction, ticket_number, amount):
        self._movement_time = movement_time
        self._transaction = transaction
        self._ticket_number = ticket_number
        self._amount = amount;

    def get_movement_time(self):
        return self._movement_time

    def get_transaction(self):
        return self._transaction

    def get_ticket_number(self):
        return self._ticket_number

    def get_amount(self):
        return self._amount

