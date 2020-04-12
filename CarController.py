from datetime import datetime
from typing import Optional, List
from Car import Car
import DatabaseDAO as dao
# TODO: replace with dao methods
from database_test import select_latest_entry_in_column, select_all_from_table, clear_table, check_existing


def add_car_with_ticket():
    entry_time = datetime.now()
    parking_lot_id = 1
    ticket_number = int((select_latest_entry_in_column("cars", "ticket_number", "t")[0])[1:]) + 1
    dao.add_car(entry_time, parking_lot_id, ticket_number, return_id=True)


def add_car_with_keycard(keycard_number: int):
    entry_time = datetime.now()
    parking_lot_id = 1
    if check_existing("keycards", "id", keycard_number):
        dao.add_car(entry_time, parking_lot_id, keycard_number, return_id=True)


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
    res = dao.execute_query_with_return(query, values, fetch_one=True)
    items = ["car_id", "entry_time", "exit_time", "ticket_number"]
    if len(res) > 0:
        v = dict(zip(items, res))
        car = Car(**v)
    return car


def main():
    clear_table("parking_movements")
    clear_table("cars")

    entry_time = datetime.now()
    parking_lot_id = 1
    ticket_number = "t100"
    dao.add_car(entry_time, parking_lot_id, ticket_number, return_id=True)
    dao.add_car(entry_time, parking_lot_id, "t101", return_id=True)

    for row in select_all_from_table("cars"):
        print(row)

    add_car_with_ticket()

    for row in select_all_from_table("cars"):
        print(row)


main()
