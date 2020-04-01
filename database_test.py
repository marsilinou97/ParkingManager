import random
import string
import json
import psycopg2
from faker import Faker
import HelperMethods as helpers
from User import User
from datetime import datetime
from RevenueCategory import RevenueCategory

faker = Faker()



def get_database_connection():
    with open("creds.json", "r") as creds_file:
        creds = json.loads(creds_file.read())

    try:
        con = psycopg2.connect(
            host="rajje.db.elephantsql.com",
            database=creds["database"],
            user=creds["user"],
            password=creds["password"]
        )
        return con
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        exit(1)
    except Exception as e:
        print(f'Error {e}')
        exit(1)


def select_all_from_table(table_name):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"SELECT * FROM {table_name}")
            return curr.fetchall()

def select_all_from_table_filtered(table_name, filter, value):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"SELECT * FROM {table_name} WHERE {filter} = '{value}'")
            return curr.fetchall()

def execute_query_with_return(query, parameters, fetch_one=False):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"{query}", parameters)
            if fetch_one:
                return curr.fetchone()
            else:
                return curr.fetchall()


def execute_query(query, parameters=None):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            # Use parameterized queries to avoid sql injection
            curr.execute(query, parameters)
        connection.commit()


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
    query = """INSERT INTO parking_movements (movement_time, movement_type, ticket_number, amount)
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

def get_user(key_term):
    values = dict(key_term=key_term)
    try:
        int(key_term)
        return User(*list(execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE FROM USERS WHERE ID = %(key_term)s""",
            values, True)))

    except ValueError:
        return User(*list(execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE FROM USERS WHERE USERNAME = %(key_term)s""",
            values, True)))


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def login(username, password):
    values = dict(username=username)
    query = """SELECT PASSWORD, ROLE FROM USERS WHERE USERNAME = %(username)s"""
    res = execute_query_with_return(query, values, True)
    if len(res) > 0:
        if helpers.verify_password(stored_password=res[0], provided_password=password):
            return res[1]  # return role if user provides correct creds.
    return -1


def main():
    clear_table("parking_movements")
    print("clearing data")

    time1 = datetime(2020, 3, 1, 10, 0, 0)
    type1 = "Entry"
    ticketnumber1 = 100
    amount1 = 0
    add_movement(time1,type1,ticketnumber1,amount1)

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
    add_movement(time3,type3,ticketnumber3,amount3)

    # Add an exit into the parking lot.
    time4 = datetime(2020, 3, 1, 12, 30, 0)
    type4 = "Exit"
    ticketnumber4 = 101
    amount4 = 0
    add_movement(time4, type4, ticketnumber4, amount4)

    print("Done adding test values");
main();

