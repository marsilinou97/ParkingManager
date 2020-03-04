import random
import string

import psycopg2
from faker import Faker

from User import User

faker = Faker()


def get_database_connection():
    try:
        con = psycopg2.connect(
            host="rajje.db.elephantsql.com",
            database='dmuhvnag',
            user='dmuhvnag',
            password='Pibk3nJehuU-kusJpY0PoC0Ad96Sgjqb'
        )
        return con
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        exit(1)


def select_all_from_table(table_name):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"SELECT * FROM {table_name}")
            return curr.fetchall()


def execute_query_with_return(query, fetch_one=False):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"{query}")
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


def add_user(first_name, last_name, address, phone, start_date, role, password):
    # Create dic of values
    values = dict(first_name=first_name, last_name=last_name, address=address, phone=phone, start_date=start_date,
                  role=role, password=password)
    # Build the query to be executed 
    query = """INSERT INTO USERS (FIRST_NAME, LAST_NAME, ADDRESS, PHONE, START_DATE, ROLE, PASSWORD)
                VALUES ( %(first_name)s, %(last_name)s, %(address)s, %(phone)s, %(start_date)s, %(role)s, %(password)s)"""
    execute_query(query, values)


def add_revenue_category(revenue_category, quantity, revenue):
    values = dict(revenue_category=revenue_category, quantity=quantity, revenue=revenue)

    query = """INSERT INTO REVENUE_CATEGORIES (REVENUE_CATEGORY, QUANTITY, REVENUE) VALUES ( %(revenue_category)s, %(quantity)s, %(revenue)s)"""
    execute_query(query, values)


def add_report(issued_on, start_range, end_range, revenue_categories):
    values = dict(issued_on=issued_on, start_range=start_range, end_range=end_range,
                  revenue_categories=revenue_categories)

    query = """INSERT INTO REPORT (ISSUED_ON, START_RANGE, END_RANGE, REVENUE_CATEGORIES)
                VALUES ( %(issued_on)s, %(start_range)s, %(end_range)s, %(revenue_categories)s)"""
    execute_query(query, values)


def clear_table(table):
    execute_query("delete from " + table)


# TODO: user parameterized query
def get_user(id):
    return execute_query_with_return(
        f"""SELECT first_name, last_name, address, PHONE, id, password, start_date, role from USERS WHERE ID = {id}""",
        True)


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def main():
    # Add 5 random users to the database
    # for _ in range(5):
    #     # Generate random data
    #     fn = faker.first_name()
    #     ln = faker.last_name()
    #     addr = faker.address()
    #     phone = faker.phone_number()
    #     start_date = faker.date_time_between(start_date='-5y', end_date='now')
    #     role = faker.random_int(0, 5)
    #     password = randomString()
    #     # Add the user to the db
    #     add_user(fn, ln, addr, phone, start_date, role, password)

    # rc1 = RevenueCategory("Parking Transaction w/ Revenue", 500, 5000.00)
    # rc2 = RevenueCategory('Key Card Transaction', 100, 0.00)
    # rc3 = RevenueCategory('Validation Transaction', 200, 0.00)
    # list = [rc1, rc2, rc3]
    # issued_on = datetime.datetime(2020, 2, 26)
    # start_range = datetime.datetime(2020, 2, 26, 0, 0, 0)
    # end_range = datetime.datetime(2020, 2, 26, 23, 59, 59)
    # revenue_categories = list
    # add_report(issued_on, start_range, end_range, revenue_categories)

    x = get_user(1)
    print(User(*list(x)))


main()

