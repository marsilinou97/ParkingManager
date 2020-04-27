from typing import Optional, List
from datetime import datetime
from Car import Car
import DatabaseDAO as dao


def get_latest_ticket():
    query = """SELECT ticket_number FROM Cars Where ticket_number like 'T%' ORDER BY ticket_number DESC"""
    return dao.execute_query_with_return(query, fetch_one=True)


def add_car_with_ticket():
    current_id = int((get_latest_ticket())[0][2:]) + 1  # gets the number portion
    current_ticket = "T_" + str(current_id)  # appends "T_"
    entry_time = datetime.now()
    parking_lot_id = 1
    dao.add_car(entry_time, parking_lot_id, current_ticket, None, return_id=True)
    current_id += 1  # increments current_id after adding the car
    return current_ticket


def add_car_with_keycard(key_card: str):
    entry_time = datetime.now()
    parking_lot_id = 1
    dao.add_car(entry_time, parking_lot_id, key_card, None, return_id=True)


def exit_car_with_keycard(key_card: str):
    exit_time = datetime.now()
    car_id = get_car(ticket_number=key_card).id
    amount = None
    payment_type = 'Keycard'
    dao.exit_car(exit_time, car_id, amount, payment_type, return_id=False)


def exit_car_with_ticket(ticket_number: str, amount, payment_type):
    exit_time = datetime.now()
    car_id = get_car(ticket_number=ticket_number).id
    dao.exit_car(exit_time, car_id, amount, payment_type, return_id=False)


def exit_car_with_validation(ticket_number: str, amount, payment_type):
    exit_time = datetime.now()
    car_id = get_car(ticket_number=ticket_number).id
    payment_type = 'Validation: ' + payment_type
    dao.exit_car(exit_time, car_id, amount, payment_type, return_id=False)


def get_all_cars() -> Optional[List[Car]]:
    cars = list()
    res = dao.execute_query_with_return(
        f"""SELECT id, entry_time,exit_time,ticket_number  
                    FROM cars""", fetch_one=False)
    items = ["car_id", "entry_time", "exit_time", "ticket_number"]
    if len(res) > 0:
        for r in res:
            v = dict(zip(items, r))
            cars.append(Car(**v))
    return cars


def get_car(ticket_number: str = None, entry_time: datetime = None) -> Optional[Car]:
    query = f"""SELECT id, entry_time,exit_time,ticket_number FROM cars WHERE """
    if ticket_number:
        values = dict(ticket_number=ticket_number)
        query += "ticket_number = %(ticket_number)s"
    elif entry_time:
        values = dict(entry_time=entry_time)
        query += "entry_time = %(entry_time)s"
    else:
        return None
    query += "ORDER BY id DESC"
    res = dao.execute_query_with_return(query, values, fetch_one=True)
    items = ["car_id", "entry_time", "exit_time", "ticket_number"]
    if len(res) > 0:
        v = dict(zip(items, res))
        car = Car(**v)
    return car


def check_existing_keycard(key_card) -> bool:
    values = dict(key_card=key_card)
    print(values)
    query = """SELECT exists (SELECT 1 FROM keycards WHERE """
    query += "id = %(key_card)s)"""
    print(query)
    return dao.execute_query_with_return(query, values, fetch_one=True)[0]


def main():
    print("")
    # a = add_car_with_keycard('K_1')
    # print(a)
    # print(check_existing_keycard('20'))
    # add_car_with_ticket()
    # a = get_car(ticket_number='K_1')
    # exit_car_with_keycard('K_11')
    # exit_car_with_validation('T_99461', 2.00, 'Senior')


main()
