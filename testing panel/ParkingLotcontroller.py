import wx
import wx.grid as wxGrid

# import WarningDialog
from DatabaseDAO import *

import datetime


class ParkingMovementController:
    __movement_list = None

    def __init__(self):
        if ParkingMovementController.__movement_list is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingMovementController.__movement_list = 1
            ParkingMovementController.get_parking_movement()

    @staticmethod
    def get_parking_movement(number_of_rows: int = 1000, ticket_number: str = "%%", from_date=datetime.datetime.today(), to_date=datetime.datetime.today()):
        if ParkingMovementController.__movement_list is None:
            ParkingMovementController()

        old_row_length = len(ParkingMovementController.__movement_list) if isinstance(ParkingMovementController.__movement_list, list) else 0
        query = """SELECT MOVEMENT_TIME, MOVEMENT_TYPE, TICKET_NUMBER, AMOUNT
                    FROM PARKING_MOVEMENTS PM
                             INNER JOIN CARS C ON PM.CAR_ID = C.ID
                    WHERE TICKET_NUMBER LIKE %(ticket_number)s
                    AND MOVEMENT_TIME::DATE BETWEEN %(from_date)s::DATE AND %(to_date)s::DATE
                    ORDER BY MOVEMENT_TIME DESC
                    """
        if ticket_number != "%%":
            values = dict(ticket_number="%" + ticket_number + "%", from_date=from_date, to_date=to_date)
        else:
            values = dict(number_of_rows=number_of_rows, ticket_number=ticket_number, from_date=from_date, to_date=to_date)
            query += " LIMIT %(number_of_rows)s"

        query_result = execute_query_with_return(query, values)
        ParkingMovementController.__movement_list = query_result
        ParkingMovementController.__movement_list = [[i.strftime("%Y-%m-%d  %H:%M") if isinstance(i, datetime.datetime) else str(i) for i in row] for row in query_result]

        new_row_length = len(ParkingMovementController.__movement_list)
        return old_row_length, new_row_length

    @staticmethod
    def convert_date_type(from_date: wx.DateTime, to_date: wx.DateTime):
        if ParkingMovementController.__movement_list is None:
            ParkingMovementController()

        from_date = datetime.date(*map(int, from_date.FormatISODate().split('-')))
        to_date = datetime.date(*map(int, to_date.FormatISODate().split('-')))
        return from_date, to_date

    @staticmethod
    def add_movement(movement_time, movement_type, car_id=None, amount=None, payment_type=None, return_id=False):
        if ParkingMovementController.__movement_list is None:
            ParkingMovementController()

        values = dict(movement_time=movement_time, movement_type=movement_type, car_id=car_id, amount=amount, payment_type=payment_type)
        query = """INSERT INTO PARKING_MOVEMENTS (MOVEMENT_TIME, MOVEMENT_TYPE, CAR_ID, AMOUNT, PAYMENT_TYPE)
                    VALUES (%(movement_time)s, %(movement_type)s, %(car_id)s, %(amount)s, %(payment_type)s)"""
        return execute_insert_query(query, values, return_id)

    @staticmethod
    # def set_date_picker(from_date_picker: wx.adv.DatePickerCtrl, to_date_picker: wx.adv.DatePickerCtrl):
    #     if ParkingMovementController.__movement_list is None:
    #         ParkingMovementController()
    #
    #     from_date = from_date_picker.GetValue()
    #     to_date = from_date_picker.GetValue().Add(wx.DateSpan(months=1))
    #
    #     if to_date.IsLaterThan(wx.DateTime.Today()):
    #         to_date = wx.DateTime.Today()
    #
    #     to_date_picker.SetRange(from_date, to_date)
    #     to_date_picker.SetValue(to_date)
    #     to_date_picker.Enable()

    @staticmethod
    def set_label(grid: wxGrid):
        if ParkingMovementController.__movement_list is None:
            ParkingMovementController()

        labels = ['Date / Time', 'Movement Type', 'Ticket', 'Amount']
        grid.SetLabelFont(wx.Font(16, 74, 90, 90, False, "Gill Sans MT"))
        grid.SetLabelBackgroundColour(wx.Colour(64, 64, 64))
        grid.SetLabelTextColour(wx.Colour(255, 255, 255))
        for label in range(len(labels)):
            grid.SetColLabelValue(label, labels[label])

    @staticmethod
    def populate_grid(grid: wxGrid, old_num_of_rows: int = 0):
        if ParkingMovementController.__movement_list is None:
            ParkingMovementController()

        rows = len(ParkingMovementController.__movement_list)
        if not rows:
            # WarningDialog.WarningDialog(None, "No parking movement today").ShowModal()
            pass

        if old_num_of_rows:
            grid.DeleteRows(0, old_num_of_rows, False)

        cols = grid.GetNumberCols()

        for row in range(len(ParkingMovementController.__movement_list)):
            grid.AppendRows()
            for col in range(cols):
                grid.SetCellValue(row, col, ParkingMovementController.__movement_list[row][col])

    @staticmethod
    def get_movement_list():
        return ParkingMovementController.__movement_list


def main():
    print("")
    # date_str = '2020-04-24'
    # my_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    #
    # pa = ParkingMovementController()
    # pa.get_parking_movement(ticket_number='K_10', from_date=my_date)
    # m = pa.get_movement_list()
    # print(m)


# main()
