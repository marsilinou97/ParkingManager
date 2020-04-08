
from datetime import datetime

import ParkingLot
from DatabaseDAO import add_car
from database_test import clear_table, select_all_from_table, display_from_table



def entry(parkinglot):
    parkinglot.set_open_spaces(parkinglot.get_open_spaces()-1)
    parkinglot.set_occupied_spaces(parkinglot.get_occupied_spaces()+1)


def main():
    clear_table("parking_movements")
    clear_table("cars")
    # entry_time=datetime.now()
    # parking_lot_id=1
    # ticket_number="t100"
    # add_car(entry_time, parking_lot_id, ticket_number);
    # add_car(entry_time, parking_lot_id, "t101");
    # add_car(entry_time, parking_lot_id, "t102");

    # time1 = datetime(2020, 3, 1, 10, 0, 0)
    # type1 = "Entry"
    # ticketnumber1 = "t100"
    # amount1 = 0
    # add_movement(time1,type1,ticketnumber1,amount1)
    #
    # # Add an exit into the parking lot.
    # time2 = datetime(2020, 3, 1, 10, 30, 0)
    # type2 = "Exit"
    # ticketnumber2 = "t100"
    # amount2 = 0
    # add_movement(time2, type2, ticketnumber2, amount2)
    #
    # # Add a movement into the parking lot.
    # time3 = datetime(2020, 3, 1, 11, 30, 0)
    # type3 = "Entry"
    # ticketnumber3 = "t101"
    # amount3 = 0
    # add_movement(time3,type3,ticketnumber3,amount3)
    #
    # # Add an exit into the parking lot.
    # time4 = datetime(2020, 3, 1, 12, 30, 0)
    # type4 = "Exit"
    # ticketnumber4 = "t101"
    # amount4 = 0
    # add_movement(time4,type4,ticketnumber4,amount4)
    #
    #
    # # Add a movement into the parking lot.
    # time5 = datetime(2020, 3, 2, 11, 30, 0)
    # type5 = "Entry"
    # ticketnumber5 = "t102"
    # amount5 = 0
    # add_movement(time5,type5,ticketnumber5,amount5)
    #
    # # Add an exit into the parking lot.
    # time6 = datetime(2020, 3, 2, 12, 30, 0)
    # type6 = "Exit"
    # ticketnumber6 = "t102"
    # amount6 = 0
    # add_movement(time6,type6,ticketnumber6,amount6)
    #
    # entry_time = datetime.now()
    # exit_time = datetime(9999, 12, 31, 0, 0, 0)
    #
    # add_car(entry_time, exit_time, 1, "t" + str(ticket_number));





main()
# def exit(self):
#     parkinglot.set_open_spaces(parkinglot.get_open_spaces() + 1);
#     parkinglot.set_occupied_spaces(parkinglot.get_occupied_spaces() - 1)