import random
import string
import json
import psycopg2
from faker import Faker
import HelperMethods as helpers
from User import User

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
    query = """INSERT INTO REPORTS (ISSUED_ON, START_RANGE, END_RANGE, REVENUE_CATEGORIES)
                VALUES ( %(issued_on)s, %(start_range)s, %(end_range)s, %(revenue_categories)s)"""
    execute_query(query, values)


def clear_table(table):
    execute_query("delete from " + table)


def get_user(key_term):
    values = dict(key_term=key_term)
    try:
        int(key_term)
        return execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE FROM USERS WHERE ID = %(key_term)s""",
            values, True)

    except ValueError:
        return execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE FROM USERS WHERE USERNAME = %(key_term)s""",
            values, True)


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
    x = get_user('user')
    print(User(*list(x)))

main()
