from faker import Faker
import DatabaseDAO as dao
import HelperMethods as helpers

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
        error_message = dao.add_user(fn, ln, addr, phone, start_date, role, password, username)
        if error_message:
            print(f"Error occured while adding user: {error_message}")
        else:
            print("Added user successfully")


def generate_parking_lot(n=1, addr=None, capacity=None):
    for _ in range(n):
        addr = faker.address()
        capacity = faker.random_int(100, 100000)
        error_message = dao.add_parking_lot(addr, capacity)

        if error_message:
            print(f"Error occured while adding parking lot: {error_message}")
        else:
            print("Added parking successfully")


def generate_hours():
    # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    error_message = ""
    error_message += dao.add_operation_hours("7:00", "11:00", 0)
    error_message += dao.add_operation_hours("7:00", "11:00", 1)
    error_message += dao.add_operation_hours("7:00", "11:00", 2)
    error_message += dao.add_operation_hours("7:00", "11:00", 3)
    error_message += dao.add_operation_hours("7:00", "11:00", 4)
    error_message += dao.add_operation_hours("9:00", "11:00", 5)
    error_message += dao.add_operation_hours("9:00", "11:00", 6)

    if error_message:
        print(f"Error occured while adding hours: {error_message}")
    else:
        print("Added hours successfully")


def connect_parking_lot_with_hours(parking_lot_id=1, hours_id=None):
    error_message = dao.connect_parking_lot_with_hours(parking_lot_id)

    if error_message:
        print(f"Error occured while connecting parking lot with hours: {error_message}")
    else:
        print("Connected parking lot with hours successfully")


def main():
    generate_users(5)
    generate_parking_lot(1)
    generate_hours()
    connect_parking_lot_with_hours(1)
    generate_parking_lot(1)


if __name__ == '__main__':
    main()
