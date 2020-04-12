import json
from sys import exit
import psycopg2


class DbSingleton:
    __connection = None

    def __init__(self):
        # Private constructor.
        if DbSingleton.__connection is not None:
            raise Exception("This class is a singleton!")
        DbSingleton.__connection = DbSingleton.__get_database_connection()

    @staticmethod
    def get_connection():
        if DbSingleton.__connection is None:
            # First time creating an instance, call the constructor
            DbSingleton()
        else:
            # connection.closed = 0 --> connection is open
            if DbSingleton.__connection.closed == 0:
                try:
                    # Make sure connection is alive and not corrupted
                    with DbSingleton.__connection.cursor() as cur:
                        cur.execute('SELECT 1')
                except Exception as e:
                    # In case of failure accessing the current db connection
                    # try to close it then instantiate a new one
                    DbSingleton.__force_close_current_connection()
                    DbSingleton.__connection = DbSingleton.__get_database_connection()
                    print(f"Error while retrieving the same connection details: {e}")
                    print("Trying to get a new connection")
            else:
                # The connection is closed or corrupted
                # Make sure old connection is properly closed before creating a new one
                print("DbSingleton, db is closed")
                DbSingleton.__force_close_current_connection()
                DbSingleton.__connection = DbSingleton.__get_database_connection()
        return DbSingleton.__connection

    @staticmethod
    def __force_close_current_connection():
        try:
            DbSingleton.__connection.close()
        except Exception:
            pass

    @staticmethod
    def __get_database_connection():
        with open("creds.json", "r") as creds_file:
            creds = json.loads(creds_file.read())
        try:
            con = psycopg2.connect(
                host=creds["host"],
                database=creds["database"],
                user=creds["user"],
                password=creds["password"]
            )
            return con
        except psycopg2.DatabaseError as e:
            print(f'Error in DB singleton: {e}')
            exit(1)
        except Exception as e:
            print(f'Error in DB singleton: {e}')
            exit(1)