from faker import Faker
import DatabaseDAO as dao
import HelperMethods as helpers
import random

faker = Faker()


def generate_users(n=5):
    for _ in range(n):
        # Generate random data
        fn = faker.first_name()
        ln = faker.last_name()
        addr = faker.address()
        phone = faker.phone_number()
        start_date = faker.date_time_between(start_date='-5y', end_date='now')
        role = faker.random_int(0, 5)
        password = helpers.hash_password(helpers.random_password(9))
        username = fn[0] + ln
        # Add the user to the db
        res = dao.add_user(fn, ln, addr, phone, start_date, role, password, username)
        if res["error_msg"]:
            print(f"Error occured while adding user: {res}")
        else:
            print(f"Added user successfully")


def generate_parking_lot(n=1, return_ids=False):
    return_dict = dict()
    return_dict["error_msg"] = ""
    return_dict["ids"] = list()
    for _ in range(n):
        addr = faker.address()
        capacity = faker.random_int(100, 100000)
        res = dao.add_parking_lot(addr, capacity, return_ids)
        if return_ids:
            return_dict["ids"].append(res["id"])

        if res["error_msg"]:
            return_dict["error_msg"] += res["error_msg"]
            print(f"Error occurred while adding parking lot: {res['error_msg']}")
        else:
            print(f"Added parking lot successfully")
    return return_dict


def generate_hours():
    # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    error_message = ""
    res = dao.add_operation_hours("7:00", "11:00", 0)
    if res["error_msg"]:
        error_message += res["error_msg"]
    res = dao.add_operation_hours("7:00", "11:00", 1)
    if res["error_msg"]:
        error_message += res["error_msg"]
    res = dao.add_operation_hours("7:00", "11:00", 2)
    if res["error_msg"]:
        error_message += res["error_msg"]
    res = dao.add_operation_hours("7:00", "11:00", 3)
    if res["error_msg"]:
        error_message += res["error_msg"]
    res = dao.add_operation_hours("7:00", "11:00", 4)
    if res["error_msg"]:
        error_message += res["error_msg"]
    res = dao.add_operation_hours("9:00", "11:00", 5)
    if res["error_msg"]:
        error_message += res["error_msg"]
    res = dao.add_operation_hours("9:00", "11:00", 6)
    if res["error_msg"]:
        error_message += res["error_msg"]

    if error_message:
        print("Error occurred while adding hours: " + error_message)
    else:
        print("Added hours successfully")


def connect_parking_lot_with_hours(parking_lot_id=1, hours_id=None):
    if hours_id:
        res = dao.connect_parking_lot_with_hours(parking_lot_id, hours_id)
    else:
        res = dao.connect_parking_lot_with_hours(parking_lot_id)

    if res["error_msg"]:
        print(f"Error occurred while connecting parking lot with hours: {res['error_msg']}")
    else:
        print("Connected parking lot with hours successfully")


def generate_revenue_categories():
    added_ids = list()
    revenue_categories = ["CASH", "CHECK", "Debit", "CREDIT"]
    for revenue_category_name in revenue_categories:
        quantity = faker.random_int(0, 99999)
        revenue = faker.random_int(0, 99999) / 100
        res = dao.add_revenue_category(revenue_category_name, quantity, revenue, return_id=True)
        if res["error_msg"]:
            print(f"Error occurred while adding user: {res}")
        else:
            print(f"Added revenue category successfully")
        added_ids.append(res["id"])

    return added_ids


def generate_report(n=1, parking_lot_id=None):
    for _ in range(n):
        start_date = faker.date_time_between(start_date='-5y', end_date='now')
        end_date = faker.date_time_between(start_date='-5y', end_date='now')
        if not parking_lot_id:
            parking_lot_id = dao.get_random_row("PARKING_LOTS", columns_names=["ID"])[0]
        issues_on = faker.date_time_between(start_date='-5y', end_date='now')
        revenue__category_ids = generate_revenue_categories()
        res = dao.add_report(start_date, end_date, parking_lot_id, issues_on, revenue__category_ids)
        if res["error_msg"]:
            print(f"Error occurred while adding report: {res}")
        else:
            print(f"Added report successfully")


def generate_car(n=1, parking_lot_id=None):
    # ENTRY_TIME, EXIT_TIME, PARKING_LOT_ID
    ticket_prefix = ['K_', 'T_']
    if not parking_lot_id:
        parking_lot_id = 1
    for _ in range(n):
        entry_time = faker.date_time_between(start_date='-5y', end_date='now')
        ticket_number = f"{random.choice(ticket_prefix)}" + str(random.randint(1, 99999))
        res = dao.add_car(entry_time, parking_lot_id, ticket_number)
        if res["error_msg"]:
            print(f"Error occurred while adding car: {res}")
        else:
            print(f"Added car successfully")


def main():
    # add_movement(movement_time, movement_type, ticket_number=None, amount=None, return_id=False):
    import time
    start = time.time()
    generate_car(10)
    print(f"time of executrion: {time.time() - start}")
    # # Generates 7 enteries in the DB with with the start and end time, the values are hard-coded and don't change so
    # # running that multiple times will be redundant
    # # generate_hours()
    #
    # # Generates random users to the DB
    # generate_users(20)
    #
    # # Generate two parking lots and storing their ids to add more data to them
    # ids = generate_parking_lot(n=2, return_ids=True)["ids"]
    #
    # for parking_lot_id in ids:
    #     # For every parking lot, add to it the following...
    #
    #     # Create 5 reports, revenue categories will be added to evey report automatically
    #     generate_report(n=5, parking_lot_id=parking_lot_id)
    #     # Set the start and end time for every parking lot
    #     connect_parking_lot_with_hours(parking_lot_id)


if __name__ == '__main__':
    main()
