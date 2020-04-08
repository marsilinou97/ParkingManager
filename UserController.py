from datetime import datetime
from typing import Optional, List, Union
from User import User

import DatabaseDAO as dao


# Getters
def get_user(key_term: Union[int, str]) -> Optional[User]:
    values = dict(key_term=key_term)
    if isinstance(key_term, int):
        return User(*list(dao.execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                        FROM USERS WHERE ID = %(key_term)s""",
            values, True)))
    else:
        return User(*list(dao.execute_query_with_return(
            f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                        FROM USERS WHERE USERNAME = %(key_term)s""",
            values, True)))


def get_users(count: int = 25) -> Optional[List[User]]:
    users = list()
    res = dao.execute_query_with_return(
        f"""SELECT FIRST_NAME, LAST_NAME, ADDRESS, PHONE, ID, PASSWORD, START_DATE, ROLE 
                            FROM USERS LIMIT 10""", fetch_one=False)
    items = ["first_name", "last_name", "address", "phone", "user_id", "password", "start_date", "access_level"]
    for r in res:
        v = dict(zip(items, r))
        users.append(User(**v))
    return users


# TODO: test
def update_user(values):
    query = []
    for k, v in values.items():
        if v:
            query.append(f"{k} = %({v})s")

    query = ", ".join(query)
    dao.execute_query_with_return(query, values)
