import random
import string
from datetime import datetime
from typing import Optional, Union, List

from faker import Faker
import DatabaseDAO as dao
from DbSingleton import DbSingleton
from User import User
from Car import Car
from Report import Report
from RevenueCategory import RevenueCategory
from Keycard import Keycard
from Movement import Movement
from Validation import Validation
import datetime


def select_all_from_table_filtered(table_name, filter, value):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(f"SELECT * FROM {table_name} WHERE {filter} = '{value}'")
        return curr.fetchall()


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
