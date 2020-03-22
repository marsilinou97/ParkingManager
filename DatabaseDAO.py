import psycopg2
import HelperMethods as helpers


# ################################### Start DB connection related methods ###################################

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


def execute_query_with_return(query, parameters=None, fetch_one=False):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"{query}", parameters)
            if fetch_one:
                return curr.fetchone()
            else:
                return curr.fetchall()


def execute_insert_query(query, parameters=None):
    error_msg = ""
    try:
        with get_database_connection() as connection:
            with connection.cursor() as curr:
                # Use parameterized queries to avoid sql injection
                curr.execute(query, parameters)
            connection.commit()
    except Exception as e:
        error_msg = str(e)
    finally:
        return error_msg


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


def add_user(first_name, last_name, address, phone, start_date, role, password, username):
    # Create dic of values
    values = dict(first_name=first_name, last_name=last_name, address=address, phone=phone, start_date=start_date,
                  role=role, password=password, username=username)
    # Build the query to be executed
    query = """INSERT INTO USERS (FIRST_NAME, LAST_NAME, ADDRESS, PHONE, START_DATE, ROLE, PASSWORD, username)
                VALUES ( %(first_name)s, %(last_name)s, %(address)s, %(phone)s, %(start_date)s, %(role)s, %(password)s, %(username)s)"""
    return execute_insert_query(query, values)


def get_user(key_term):
    values = dict(key_term=key_term)
    try:
        int(key_term)
        return execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE FROM USERS WHERE id = %(key_term)s""",
            values, True)

    except ValueError:
        return execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE FROM USERS WHERE USERNAME = %(key_term)s""",
            values, True)


# ################################### END User related methods ###################################


# ################################### Start Parking lot related methods ###################################
def add_parking_lot(address, capacity):
    values = dict(address=address, capacity=capacity)
    query = """insert INTO PARKING_LOTS (address, capacity) VALUES ( %(address)s, %(capacity)s)"""
    return execute_insert_query(query, values)


def add_operation_hours(open_time, close_time, day):
    values = dict(open_time=open_time, close_time=close_time, day=day)
    query = """insert INTO HOURS (open_time, close_time, day) VALUES ( %(open_time)s, %(close_time)s, %(day)s)"""
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
        query = """insert INTO PARKING_LOT_HOURS (LOT_ID, HOURS_ID) VALUES ( (%(parking_lot_id)s, (%(hours_id)s))"""
        return execute_insert_query(query, values)
