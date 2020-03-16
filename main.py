from ParkingLot import ParkingLot
from TestCalender import TestCalender
if __name__ == "__main__":

    lot_a = ParkingLot("Csulb Lot A", "1250 Bellflower Blvd, Long Beach, CA 90840", 24, 1000, 500, 7.00)
    calender_a = TestCalender(2020)
    #print(calender_a.get_yearly())

    calender_a.set_default_rate(10.00)
    calender_a.set_rate(4, 17, 12.50)
    calender_a.set_rate(4, 31, 12.50)
    calender_a.set_rate_range(4, 2, 15, 7.50)

    print(calender_a.show_month(4))
    print(calender_a.show_rates(4))

    #print("Parking Lot: " + lot_a.get_name + " operates from 00:00 to " + str(lot_a.get_hours) + ":00. It is located at: " + lot_a.get_address)
    print((lot_a.get_capacity()))

    print("10 cars enter the Lot.")
    for i in range(0,10):
        lot_a.car_enter()
    print((lot_a.get_capacity()))

    print("5 cars exit the Lot.")
    for i in range(0,5):
        lot_a.car_exit()
    print((lot_a.get_capacity()))





