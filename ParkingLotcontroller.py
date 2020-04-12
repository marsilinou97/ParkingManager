import wx
import wx.grid as wxGrid
from DatabaseDAO import *


# TODO: connect with db
def entry(parkinglot):
    parkinglot.set_open_spaces(parkinglot.get_open_spaces() - 1)
    parkinglot.set_occupied_spaces(parkinglot.get_occupied_spaces() + 1)


def get_parking_movement(number_of_rows: int = 50, ticket_number: str = "%%"):
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

    res = execute_query_with_return(query, values)
    return [[str(i) for i in row] for row in res]


data = get_parking_movement()


def add_movement(movement_time, movement_type, car_id=None, amount=None, return_id=False):
    values = dict(movement_time=movement_time, movement_type=movement_type, car_id=car_id, amount=amount)
    query = """INSERT INTO PARKING_MOVEMENTS (MOVEMENT_TIME, MOVEMENT_TYPE, CAR_ID, AMOUNT)
                VALUES (%(movement_time)s, %(movement_type)s, %(car_id)s, %(amount)s)"""
    return execute_insert_query(query, values, return_id)


def set_label(grid: wxGrid):
    labels = ['Date / Time', 'Movement Type', 'Ticket', 'Amount']
    grid.SetLabelFont(wx.Font(16, 74, 90, 90, False, "Gill Sans MT"))
    grid.SetLabelBackgroundColour(wx.Colour(64, 64, 64))
    grid.SetLabelTextColour(wx.Colour(255, 255, 255))
    for label in range(len(labels)):
        grid.SetColLabelValue(label, labels[label])


def populate_grid(grid: wxGrid):
    rows = grid.GetNumberRows()
    cols = grid.GetNumberCols()

    for row in range(rows):
        for col in range(cols):
            grid.SetCellValue(row, col, data[row][col])

    set_label(grid)

# print(data)
# print(len(data))
