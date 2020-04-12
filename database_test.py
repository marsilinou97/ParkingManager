import datetime
from datetime import datetime
from typing import Optional, List

from faker import Faker

import DatabaseDAO as dao
import HelperMethods as helpers
from DbSingleton import DbSingleton

faker = Faker()


def select_all_from_table(table_name):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"SELECT * FROM {table_name}")
        return curr.fetchall()


def display_from_table(table_name):
    for row in select_all_from_table(table_name):
        templist = list(row)
        for i in range(len(row)):
            if type(row[i]) == datetime:
                templist[i] = (row[i].strftime("%Y/%m/%d, %H:%M:%S"))
        print(templist)


def select_all_from_table_filtered(table_name, filter, value):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"SELECT * FROM {table_name} WHERE {filter} = '{value}'")
        return curr.fetchall()


def select_latest_entry_in_column(table_name, column_name, value=None):
    with DbSingleton.get_connection().cursor() as curr:
        if value is None:
            curr.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {column_name} DESC LIMIT 1")
        else:
            curr.execute(
                f"SELECT {column_name} FROM {table_name} WHERE {column_name} LIKE '{value}%' ORDER BY {column_name} DESC LIMIT 1")
        return curr.fetchone()


def check_existing(table_name, column_name, value):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"SELECT * FROM {table_name} WHERE {column_name} = '{value}'")
        return curr.fetchone()


def execute_query_with_return(query, parameters=None, fetch_one=False):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"{query}", parameters)
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


def login(username, password):
    values = dict(username=username)
    query = """SELECT PASSWORD, ROLE FROM USERS WHERE USERNAME = %(username)s"""
    res = execute_query_with_return(query, values, True)
    if len(res) > 0:
        if helpers.verify_password(stored_password=res[0], provided_password=password):
            return res[1]  # return role if user provides correct creds.
    return -1


def update_user(values):
    query = []
    for k, v in values.items():
        if v:
            query.append(f"{k} = %({v}s")

    query = ", ".join(query)

    query = """UPDATE USERS
                SET 
                FIRST_NAME=%(FIRST_NAME)s, LAST_NAME=%(LAST_NAME)s, ADDRESS=%(ADDRESS)s, PHONE=%(PHONE)s, START_DATE=%(START_DATE)s, ROLE=%(ROLE)s, PASSWORD=%(PASSWORD)s, USERNAME=%(USERNAME)s
            WHERE ID = %(user_id)s"""
    execute_query_with_return(query, values)


def get_parking_movement(number_of_rows: int = 20, ticket_number: str = '%%') -> Optional[List[List[str]]]:
    query = """SELECT MOVEMENT_TIME, MOVEMENT_TYPE, TICKET_NUMBER, AMOUNT
                FROM PARKING_MOVEMENTS PM
                         INNER JOIN CARS C ON PM.CAR_ID = C.ID
                WHERE TICKET_NUMBER LIKE %(ticket_number)s
                ORDER BY MOVEMENT_TIME DESC
                """
    if ticket_number != "%%":
        values = dict(ticket_number="%" + ticket_number + "%")
    else:
        values = dict(number_of_rows=number_of_rows, ticket_number=ticket_number)
        query += " LIMIT %(number_of_rows)s"

    res = dao.execute_query_with_return(query, values)
    return [[str(i) for i in row] for row in res]


def main():
    print("")


main()


# issued_on, start_range, end_range, revenue_categories, payment_categories):
def generate_report(day: int, month: int, year: int):
    payment_categories = ["CASH", "Debit", "CREDIT"]
    revenue_categories = ["PARKING TRANSACTION W/REVENUE", "KEYCARD TRANSACTION",
                          "validation transaction", "monthly parkers transaction"]
    revenue_categories += payment_categories
    for revenue_category_name in revenue_categories:
        pass
