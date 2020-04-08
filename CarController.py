from datetime import datetime
from typing import Optional, List
from Car import Car

import DatabaseDAO as dao


def car_entered(entry_time, parking_lot_id, ticket_number, return_id=False):
    return dao.add_car(entry_time, parking_lot_id, ticket_number, return_id)


def car_exit():
    pass


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
