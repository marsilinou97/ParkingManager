import random
import string
from datetime import datetime
from typing import Optional, Union, List

from faker import Faker

from DbSingleton import DbSingleton
from User import User
from Car import Car
from Report import Report
from RevenueCategory import RevenueCategory
from Keycard import Keycard
from Movement import Movement
from Validation import Validation
import datetime

faker = Faker()


def select_all_from_table(table_name):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"SELECT * FROM {table_name}")
        return curr.fetchall()


def select_all_from_table_filtered(table_name, filter, value):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"SELECT * FROM {table_name} WHERE {filter} = '{value}'")
        return curr.fetchall()


def execute_query_with_return(query, parameters=None, fetch_one=False):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(query, parameters)
        if fetch_one:
            return curr.fetchone()
        else:
            return curr.fetchall()


def execute_query(query, parameters=None):
    with DbSingleton.get_connection().cursor() as curr:
        # Use parameterized queries to avoid sql injection
        curr.execute(query, parameters)
    DbSingleton.get_connection().commit()


def clear_table(table):
    execute_query("delete from " + table)


def add_user(first_name, last_name, address, phone, start_date, role):
    # Create dic of values
    values = dict(first_name=first_name, last_name=last_name, address=address, phone=phone, start_date=start_date,
                  role=role)
    # Build the query to be executed
    query = """INSERT INTO users (first_name, last_name, address, phone, start_date, role)
                VALUES ( %(first_name)s, %(last_name)s, %(address)s, %(phone)s, %(start_date)s, %(role)s)"""

    execute_query(query, values)


def add_movement(movement_time, movement_type, ticket_number, amount):
    # Create dic of values
    values = dict(movement_time=movement_time, movement_type=movement_type, ticket_number=ticket_number, amount=amount)
    # Build the query to be executed
    query = """INSERT INTO parking_movements (movement_time, movement_type, car_id, amount)
                VALUES ( %(movement_time)s, %(movement_type)s, %(ticket_number)s, %(amount)s)"""

    execute_query(query, values)


def add_revenue_category(revenue_category, quantity, revenue):
    values = dict(revenue_category=revenue_category, quantity=quantity, revenue=revenue)

    query = """INSERT INTO REVENUE_CATEGORIES (REVENUE_CATEGORY, QUANTITY, REVENUE) VALUES ( %(revenue_category)s, %(quantity)s, %(revenue)s)"""
    execute_query(query, values)


def add_report(issued_on, start_range, end_range, parking_lot_ID):
    values = dict(issued_on=issued_on, start_range=start_range, end_range=end_range,
                  parking_lot_ID=parking_lot_ID)

    query = """INSERT INTO REPORTS (ISSUED_ON, START_RANGE, END_RANGE, parking_lot_ID)
                VALUES ( %(issued_on)s, %(start_range)s, %(end_range)s, %(parking_lot_ID)s)"""

    execute_query(query, values)


def add_reports_revenue_categories(revenue_category, report):
    values = dict(revenue_category=revenue_category, report=report)

    query = """INSERT INTO REPORTS_REVENUE_CATEGORIES(REVENUE_CATEGORY, REPORT) 
                VALUES ( %(revenue_category)s, %(report)s)"""

    execute_query(query, values)


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def main():
    clear_table("parking_movements")
    print("clearing data")

    time1 = datetime(2020, 3, 1, 10, 0, 0)
    type1 = "Entry"
    ticketnumber1 = 100
    amount1 = 0
    add_movement(time1, type1, ticketnumber1, amount1)

    # Add an exit into the parking lot.
    time2 = datetime(2020, 3, 1, 10, 30, 0)
    type2 = "Exit"
    ticketnumber2 = 100
    amount2 = 0
    add_movement(time2, type2, ticketnumber2, amount2)

    # Add a movement into the parking lot.
    time3 = datetime(2020, 3, 1, 11, 30, 0)
    type3 = "Entry"
    ticketnumber3 = 101
    amount3 = 0
    add_movement(time3, type3, ticketnumber3, amount3)

    # Add an exit into the parking lot.
    time4 = datetime(2020, 3, 1, 12, 30, 0)
    type4 = "Exit"
    ticketnumber4 = 101
    amount4 = 0
    add_movement(time4, type4, ticketnumber4, amount4)

    print("Done adding test values")


# main()


def get_car(ticket_number=None, get_all=False):
    values = dict(ticket_number=ticket_number)
    return list(execute_query_with_return(
        f"""SELECT ENTRY_TIME, EXIT_TIME, PARKING_LOT_ID
             FROM CARS
                WHERE USERNAME = %(key_term)s""",
        values, fetch_one=True))


def update_user(values):
    query = []
    for k, v in values.items():
        if v:
            query.append(f"{k} = %({v}s")

    query = ", ".join(query)
    #
    # query = """UPDATE USERS
    #             SET
    #             FIRST_NAME=%(FIRST_NAME)s, LAST_NAME=%(LAST_NAME)s, ADDRESS=%(ADDRESS)s, PHONE=%(PHONE)s, START_DATE=%(START_DATE)s, ROLE=%(ROLE)s, PASSWORD=%(PASSWORD)s, USERNAME=%(USERNAME)s
    #         WHERE ID = %(user_id)s"""
    execute_query_with_return(query, values)


# Getters
def get_user(key_term: Optional[Union[int, str]]) -> Optional[User]:
    values = dict(key_term=key_term)
    if isinstance(key_term, int):
        return User(*list(execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                        FROM USERS WHERE ID = %(key_term)s""",
            values, True)))
    else:
        return User(*list(execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                        FROM USERS WHERE USERNAME = %(key_term)s""",
            values, True)))


def get_all_users() -> Optional[List[User]]:
    users = list()
    res = execute_query_with_return(
        f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                            FROM USERS""", fetch_one=False)
    items = ["first_name", "last_name", "address", "phone", "user_id", "password", "start_date", "access_level"]
    for r in res:
        v = dict(zip(items, r))
        users.append(User(**v))
    return users


def get_all_cars() -> Optional[List[Car]]:
    cars = list()
    res = execute_query_with_return(
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
    res = execute_query_with_return(query, values, fetch_one=True)
    items = ["car_id", "entry_time", "exit_time", "ticket_number"]
    if len(res) > 0:
        v = dict(zip(items, res))
        car = Car(**v)
    return car


print(get_car("T_30933"))
print(get_all_cars())


def get_report(month: int, year: int, day: int = 1) -> Optional[Report]:
    values = dict(month=month, year=year, day=day)
    results = execute_query_with_return(
        f"""SELECT R.ISSUED_ON, R.START_RANGE, R.END_RANGE, RC.REVENUE_CATEGORY, RC.QUANTITY, RC.REVENUE
                FROM REPORTS R
                         INNER JOIN REPORTS_REVENUE_CATEGORIES RRC ON R.ID = RRC.REPORT
                         INNER JOIN REVENUE_CATEGORIES RC ON RRC.REVENUE_CATEGORY = RC.ID
                WHERE date_part('day', START_RANGE) = %(day)s
                  AND date_part('month', START_RANGE) = %(month)s
                  AND date_part('year', START_RANGE) = %(year)s;""", values, False)
    revenue_categories = list()
    payment_categories = list()
    if len(results) > 0:
        for result in results:
            result = result[3:]
            if result[0].lower() in ['cash', 'debit', 'check', 'card', 'credit']:
                revenue_categories.append(RevenueCategory(*result))
            else:
                payment_categories.append(RevenueCategory(*result))
        report = Report(*results[0][:3], revenue_categories, payment_categories)
        print(report)
    else:
        print("No matching report")

# get_report(month=1, year=2020)
