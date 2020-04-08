from datetime import datetime

from DatabaseDAO import add_car
from database_test import select_latest_entry_in_column, select_all_from_table, clear_table, check_existing


def add_car_with_ticket():
    entry_time = datetime.now()
    parking_lot_id = 1
    ticket_number = int((select_latest_entry_in_column("cars", "ticket_number", "t")[0])[1:]) + 1
    add_car(entry_time, parking_lot_id, ticket_number, return_id=True)

def add_car_with_keycard(keycard_number: int):
    entry_time = datetime.now()
    parking_lot_id = 1
    if check_existing("keycards", "id", keycard_number):
        add_car(entry_time, parking_lot_id, keycard_number, return_id=True)

def main():
    clear_table("parking_movements")
    clear_table("cars")

    entry_time=datetime.now()
    parking_lot_id=1
    ticket_number="t100"
    add_car(entry_time, parking_lot_id, ticket_number,return_id=True)
    add_car(entry_time, parking_lot_id, "t101",return_id=True)

    for row in select_all_from_table("cars"):
        print(row)

    add_car_with_ticket()

    for row in select_all_from_table("cars"):
        print(row)

main()
