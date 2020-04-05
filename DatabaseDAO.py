from datetime import datetime

import HelperMethods as helpers
import User
from DbSingleton import DbSingleton


# ################################### Start DB related methods ###################################
def execute_query_with_return(query, parameters=None, fetch_one=False):
    with DbSingleton.get_connection().cursor() as curr:
        curr.execute(query, parameters)
        if fetch_one:
            return curr.fetchone()
        else:
            return curr.fetchall()


def execute_insert_query(query, parameters=None, return_id=False):
    return_dict = dict()
    return_dict["error_msg"] = ""
    try:
        with DbSingleton.get_connection().cursor() as curr:
            # Use parameterized queries to avoid sql injection
            if return_id:
                query += " RETURNING ID"
            curr.execute(query, parameters)
            DbSingleton.get_connection().commit()
            if return_id:
                return_dict["id"] = curr.fetchone()[0]
    except Exception as e:
        return_dict["error_msg"] = str(e)
    finally:
        return return_dict


# ################################### END DB connection related methods ###################################


# ################################### Start User related methods ###################################
def login(username, password):
    values = dict(username=username)
    query = """SELECT PASSWORD, ROLE FROM USERS WHERE USERNAME = %(username)s"""
    res = execute_query_with_return(query, values, True)
    if len(res) > 0:
        if helpers.verify_password(stored_password=res[0], provided_password=password):
            return res[1]  # return role if user provides correct creds.
    return -1


def add_user(first_name, last_name, address, phone, start_date, role, password, username, return_id=False):
    # Create dic of values
    values = dict(first_name=first_name, last_name=last_name, address=address, phone=phone, start_date=start_date,
                  role=role, password=password, username=username)
    # Build the query to be executed
    query = """INSERT INTO USERS (FIRST_NAME, LAST_NAME, ADDRESS, PHONE, START_DATE, ROLE, PASSWORD, USERNAME)
                VALUES ( %(first_name)s, %(last_name)s, %(address)s, 
                                                    %(phone)s, %(start_date)s, %(role)s, %(password)s, %(username)s)"""
    return execute_insert_query(query, values, return_id)


def get_user(key_term):
    values = dict(key_term=key_term)
    try:
        int(key_term)
        return User(*list(execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                    FROM USERS WHERE ID = %(key_term)s""", values, True)))

    except ValueError:
        return User(*list(execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                    FROM USERS WHERE USERNAME = %(key_term)s""", values, True)))


# ################################### END User related methods ###################################


# ################################### Start Parking lot related methods ###################################
def add_parking_lot(address, capacity, return_id=False):
    values = dict(address=address, capacity=capacity)
    query = """INSERT INTO PARKING_LOTS (ADDRESS, CAPACITY) VALUES ( %(address)s, %(capacity)s)"""
    return execute_insert_query(query, values, return_id)


def add_operation_hours(open_time, close_time, day):
    values = dict(open_time=open_time, close_time=close_time, day=day)
    query = """INSERT INTO HOURS (OPEN_TIME, CLOSE_TIME, DAY) VALUES ( %(open_time)s, %(close_time)s, %(day)s)"""
    return execute_insert_query(query, values)


def connect_parking_lot_with_hours(parking_lot_id=1, hours_id=None):
    if not hours_id:
        values = dict(parking_lot_id=parking_lot_id)
        query = """INSERT INTO PARKING_LOT_HOURS (LOT_ID, HOURS_ID)
                    VALUES (%(parking_lot_id)s, 1),
                           (%(parking_lot_id)s, 2),
                           (%(parking_lot_id)s, 3),
                           (%(parking_lot_id)s, 4),
                           (%(parking_lot_id)s, 5),
                           (%(parking_lot_id)s, 6),
                           (%(parking_lot_id)s, 7)"""
        return execute_insert_query(query, values)
    else:
        values = dict(parking_lot_id=parking_lot_id, hours_id=hours_id)
        query = """INSERT INTO PARKING_LOT_HOURS (LOT_ID, HOURS_ID) VALUES ( (%(parking_lot_id)s, (%(hours_id)s))"""
        return execute_insert_query(query, values)


# TODO: complete
def add_movement(movement_time, movement_type, ticket_number=None, amount=None, return_id=False):
    values = dict(movement_time=movement_time, movement_type=movement_type, ticket_number=ticket_number, amount=amount)
    query = """INSERT INTO PARKING_MOVEMENTS (MOVEMENT_TIME, MOVEMENT_TYPE, TICKET_NUMBER, AMOUNT)
                VALUES (%(movement_time)s, %(movement_type)s, %(ticket_number)s, %(amount)s)"""
    return execute_insert_query(query, values, return_id)
    # if amount:
    #     query = """INSERT INTO PARKING_MOVEMENTS (MOVEMENT_TIME, MOVEMENT_TYPE, AMOUNT)
    #                  VALUES ()"""
    # if ticket_number:
    #     query = """INSERT INTO PARKING_MOVEMENTS (MOVEMENT_TIME, MOVEMENT_TYPE, TICKET_NUMBER, AMOUNT)
    #                 VALUES ()"""


# ################################### END Parking lot related methods ###################################


# ################################### Start report related methods ###################################
def connect_report_with_category(report_id, revenue_category_id):
    values = dict(report_id=report_id, revenue_category_id=revenue_category_id)
    query = "INSERT INTO REPORTS_REVENUE_CATEGORIES(REVENUE_CATEGORY, REPORT) VALUES (%(revenue_category_id)s , %(report_id)s)"
    return execute_insert_query(query, values)


def add_report(start_date, end_date, parking_lot_id, issues_on=None, revenue__category_ids=None):
    return_dict = dict()
    return_dict["error_msg"] = ""
    values = dict(start_date=start_date, end_date=end_date, parking_lot_id=parking_lot_id)
    if issues_on:
        values["issues_on"] = issues_on
        query = """INSERT INTO REPORTS (ISSUED_ON, START_RANGE, END_RANGE, PARKING_LOT_ID) 
            VALUES (%(issues_on)s, %(start_date)s, %(end_date)s, %(parking_lot_id)s) """
    else:
        query = """INSERT INTO REPORTS (ISSUED_ON, START_RANGE, END_RANGE, PARKING_LOT_ID) 
                VALUES (now(), %(start_date)s, %(end_date)s, %(parking_lot_id)s) """
    if revenue__category_ids:
        report_res = execute_insert_query(query, values, return_id=True)
        if report_res["error_msg"]:
            return_dict["error_msg"] = report_res["error_msg"]
            return return_dict
        else:
            report_id = report_res["id"]
        for revenue__category_id in revenue__category_ids:
            res = connect_report_with_category(report_id, revenue__category_id)
            if res["error_msg"]:
                error_msg = f"Error message during connecting report with id: {report_id} with revenue category with id: {revenue__category_id}\n{res['error_msg']}"
                print(error_msg)
                return_dict["error_msg"] += error_msg
            else:
                print(f"Connected report: {report_id} with revenue category: {revenue__category_id}")

    else:
        return_dict = execute_insert_query(query, values)

    return return_dict


def add_revenue_category(revenue_category_name, quantity, revenue, return_id=False):
    values = dict(revenue_category_name=revenue_category_name, quantity=quantity, revenue=revenue)
    query = """INSERT INTO REVENUE_CATEGORIES (REVENUE_CATEGORY, QUANTITY, REVENUE) 
                VALUES (%(revenue_category_name)s, %(quantity)s, %(revenue)s)"""
    return execute_insert_query(query, values, return_id)


# ################################### End Parking lot related methods ###################################

# ################################### Start car related methods ###################################

def add_car(entry_time, parking_lot_id, ticket_number, return_id=False):
    values = dict(entry_time=entry_time, parking_lot_id=parking_lot_id, ticket_number=ticket_number)
    query = """INSERT INTO CARS (ENTRY_TIME, TICKET_NUMBER, PARKING_LOT_ID)
                VALUES (%(entry_time)s, %(ticket_number)s, %(parking_lot_id)s)"""
    adding_car_res = execute_insert_query(query, values, return_id=return_id)

    res = add_movement(datetime.now().strftime("%H:%M:%S"), 'Entry', adding_car_res["id"])
    if res["error_msg"]:
        print(f"Error occurred while adding parking movement: {res}")

    return adding_car_res


# ################################### End car related methods ###################################


# ################################### START GENERAL methods ###################################

# NOTE: This method is only intended to be used only by developers as it doesn't implement parametrized query and
# vulnerable to SQLi
def get_random_row(table_name, columns_names=None):
    table_name.replace("'", "").replace("\"", "")
    query = """SELECT {rows_names}
                FROM {table_name}
                ORDER BY random()
                LIMIT 1;""".format(table_name=table_name, rows_names="*" if not columns_names else ", ".join(
        [row_name for row_name in columns_names]))

    return execute_query_with_return(query, fetch_one=True)
