import wx
import wx.xrc
import wx.dataview
import datetime

import CarController as car_controller
import ParkingLotcontroller as lot_controller


###########################################################################
## Class MyFrame1
###########################################################################

class TestingFrame(wx.Frame):

    def __init__(self, parent):
        self.amount_textbox = None
        self.payment_option = 0

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Testing Panel', pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        title_sizer = wx.BoxSizer(wx.VERTICAL)

        self.lot_id = wx.StaticText(self, wx.ID_ANY, u"Lot A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lot_id.Wrap(-1)

        self.lot_id.SetFont(
            wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        title_sizer.Add(self.lot_id, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        main_sizer.Add(title_sizer, 0, wx.EXPAND, 5)

        left_right_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_side_sizer = wx.BoxSizer(wx.VERTICAL)

        car_enter_sizer = wx.BoxSizer(wx.VERTICAL)

        car_enter_sizer.SetMinSize(wx.Size(-1, 150))
        self.car_enter_button = wx.Button(self, wx.ID_ANY, u"Car enter", wx.DefaultPosition, wx.DefaultSize, 0)
        car_enter_sizer.Add(self.car_enter_button, 0, wx.ALL, 5)

        enter_options_sizer = wx.BoxSizer(wx.VERTICAL)

        enter_ticket_radio_sizer = wx.BoxSizer(wx.HORIZONTAL)
        enter_ticket_radio_sizer.Add((25, 0), 0, wx.EXPAND, 5)
        self.ticket_enter_option = wx.RadioButton(self, wx.ID_ANY, u"Ticket", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        enter_ticket_radio_sizer.Add(self.ticket_enter_option, 0, wx.ALL, 5)

        enter_options_sizer.Add(enter_ticket_radio_sizer, 0, wx.EXPAND, 5)

        enter_keycard_radio_sizer = wx.BoxSizer(wx.HORIZONTAL)
        enter_keycard_radio_sizer.Add((25, 0), 0, wx.EXPAND, 5)
        self.keycard_enter_option = wx.RadioButton(self, wx.ID_ANY, u"Keycard", wx.DefaultPosition, wx.DefaultSize, 0)
        enter_keycard_radio_sizer.Add(self.keycard_enter_option, 0, wx.ALL, 5)

        enter_options_sizer.Add(enter_keycard_radio_sizer, 0, wx.EXPAND, 5)

        enter_keycard_textbox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        enter_keycard_textbox_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        self.keycard_static_text = wx.StaticText(self, wx.ID_ANY, u"Enter keycard number:", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.keycard_static_text.Wrap(-1)
        self.keycard_static_text.Disable()
        enter_keycard_textbox_sizer.Add(self.keycard_static_text, 0, wx.ALL, 5)

        self.keycard_textbox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.keycard_textbox.Disable()
        enter_keycard_textbox_sizer.Add(self.keycard_textbox, 0, wx.ALL, 5)

        enter_options_sizer.Add(enter_keycard_textbox_sizer, 1, wx.EXPAND, 5)

        car_enter_sizer.Add(enter_options_sizer, 1, wx.EXPAND, 5)

        left_side_sizer.Add(car_enter_sizer, 0, wx.EXPAND, 5)

        car_exit_sizer = wx.BoxSizer(wx.VERTICAL)

        car_exit_sizer.SetMinSize(wx.Size(-1, 150))
        self.car_exit_button = wx.Button(self, wx.ID_ANY, u"Car exit", wx.DefaultPosition, wx.DefaultSize, 0)
        car_exit_sizer.Add(self.car_exit_button, 0, wx.ALL, 5)

        self.car_exit_options_sizer = wx.BoxSizer(wx.VERTICAL)

        exit_keycard_radio_sizer = wx.BoxSizer(wx.HORIZONTAL)
        exit_keycard_radio_sizer.Add((25, 0), 0, wx.EXPAND, 5)
        self.keycard_exit_option = wx.RadioButton(self, wx.ID_ANY, u"Keycard", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        exit_keycard_radio_sizer.Add(self.keycard_exit_option, 0, wx.ALL, 5)

        self.car_exit_options_sizer.Add(exit_keycard_radio_sizer, 0, wx.EXPAND, 5)

        exit_ticket_radio_sizer = wx.BoxSizer(wx.HORIZONTAL)
        exit_ticket_radio_sizer.Add((25, 0), 0, wx.EXPAND, 5)
        self.ticket_exit_option = wx.RadioButton(self, wx.ID_ANY, u"Ticket", wx.DefaultPosition, wx.DefaultSize, 0)
        exit_ticket_radio_sizer.Add(self.ticket_exit_option, 0, wx.ALL, 5)

        self.car_exit_options_sizer.Add(exit_ticket_radio_sizer, 0, wx.EXPAND, 5)

        self.exit_ticket_payment_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.car_exit_options_sizer.Add(self.exit_ticket_payment_text_sizer, 0, wx.EXPAND, 5)

        self.exit_ticket_payment_choices_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.car_exit_options_sizer.Add(self.exit_ticket_payment_choices_sizer, 0, wx.EXPAND, 5)

        self.exit_ticket_amount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.car_exit_options_sizer.Add(self.exit_ticket_amount_sizer, 0, wx.EXPAND, 5)

        self.exit_validation_radio_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.exit_validation_radio_sizer.Add((25, 0), 0, wx.EXPAND, 5)
        self.validation_exit_option = wx.RadioButton(self, wx.ID_ANY, u"Validation", wx.DefaultPosition, wx.DefaultSize, 0)
        self.exit_validation_radio_sizer.Add(self.validation_exit_option, 0, wx.ALL, 5)
        self.car_exit_options_sizer.Add(self.exit_validation_radio_sizer, 0, wx.EXPAND, 5)

        self.exit_validation_payment_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.car_exit_options_sizer.Add(self.exit_validation_payment_text_sizer, 0, wx.EXPAND, 5)

        self.exit_validation_payment_choices_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.car_exit_options_sizer.Add(self.exit_validation_payment_choices_sizer, 0, wx.EXPAND, 5)

        self.exit_validation_amount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.car_exit_options_sizer.Add(self.exit_validation_amount_sizer, 0, wx.EXPAND, 5)

        car_exit_sizer.Add(self.car_exit_options_sizer, 1, wx.EXPAND, 5)

        left_side_sizer.Add(car_exit_sizer, 0, wx.EXPAND, 5)

        gate_entry_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.entry_gate_radio = wx.RadioBox(self, wx.ID_ANY, u"Entry Gate", wx.DefaultPosition, wx.DefaultSize,
                                            ['Open', 'Close'], 0, wx.RA_SPECIFY_COLS)
        gate_entry_sizer.Add(self.entry_gate_radio, 0, wx.ALL, 5)

        self.exit_gate_radio = wx.RadioBox(self, wx.ID_ANY, u"Exit Gate", wx.DefaultPosition, wx.DefaultSize,
                                           ['Open', 'Close'], 0, wx.RA_SPECIFY_COLS)
        gate_entry_sizer.Add(self.exit_gate_radio, 0, wx.ALL, 5)

        left_side_sizer.Add(gate_entry_sizer, 1, wx.EXPAND, 5)

        left_right_sizer.Add(left_side_sizer, 1, wx.EXPAND, 5)

        right_side_sizer = wx.BoxSizer(wx.VERTICAL)

        self.ticket_keycard_list = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 530),
                                                                0)
        self.ticket_keycard_list_column_1 = self.ticket_keycard_list.AppendTextColumn(u"Ticket/Keycard No.",
                                                                                      wx.dataview.DATAVIEW_CELL_ACTIVATABLE,
                                                                                      200, wx.ALIGN_LEFT,
                                                                                      wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.ticket_keycard_list_column_2 = self.ticket_keycard_list.AppendTextColumn(u"Status",
                                                                                      wx.dataview.DATAVIEW_CELL_ACTIVATABLE,
                                                                                      200, wx.ALIGN_LEFT,
                                                                                      wx.dataview.DATAVIEW_COL_RESIZABLE)
        right_side_sizer.Add(self.ticket_keycard_list, 0, wx.ALL, 5)

        left_right_sizer.Add(right_side_sizer, 1, wx.EXPAND, 5)

        main_sizer.Add(left_right_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.car_enter_button.Bind(wx.EVT_BUTTON, self.OnCarEnterClick)
        self.ticket_enter_option.Bind(wx.EVT_RADIOBUTTON, self.OnTicketEnterBtn)
        self.keycard_enter_option.Bind(wx.EVT_RADIOBUTTON, self.OnKeycardEnterBtn)
        self.car_exit_button.Bind(wx.EVT_BUTTON, self.OnCarExitClick)
        self.keycard_exit_option.Bind(wx.EVT_RADIOBUTTON, self.OnKeycardExitBtn)
        self.ticket_exit_option.Bind(wx.EVT_RADIOBUTTON, self.OnTicketExitBtn)
        self.validation_exit_option.Bind(wx.EVT_RADIOBUTTON, self.OnValidationExitBtn)
        self.entry_gate_radio.Bind(wx.EVT_RADIOBOX, self.OnEntryGateBox)
        self.exit_gate_radio.Bind(wx.EVT_RADIOBOX, self.OnExitGateBox)
        self.ticket_keycard_list.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.OnCarDoubleClick, id=wx.ID_ANY)
        self.ticket_keycard_list.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.OnCarSelection, id=wx.ID_ANY)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnCarDoubleClick(self, event):
        pass

    def OnCarSelection(self, event):
        row_number = self.ticket_keycard_list.GetSelectedRow()
        if row_number == -1:
            return None
        return row_number

    def OnCarEnterClick(self, event):
        status = 'On Lot'
        if self.ticket_enter_option.GetValue() == True:
            ticket_number = car_controller.add_car_with_ticket()
            self.ticket_keycard_list.AppendItem([ticket_number, status])
            self.ticket_enter_option.SetValue(False)

        elif self.keycard_enter_option.GetValue() == True:
            if self.keycard_textbox.Value == '':
                wx.MessageBox('Input keycard number.', 'Message', wx.OK)
                return

            keycard_number = self.keycard_textbox.Value
            # Check if keycard exist ##
            if car_controller.check_existing_keycard(keycard_number):
                # Check if keycard exist in lot
                keycard_number = 'K_' + keycard_number
                date_str = '2020-04-24'
                my_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                lot_controller.ParkingMovementController.get_parking_movement(ticket_number=keycard_number, from_date=my_date)
                keycard_history = lot_controller.ParkingMovementController.get_movement_list()

                if keycard_history:
                    # Check keycard's latest status
                    latest_keycard_status = keycard_history[0][1]
                    if latest_keycard_status == 'Entry':
                        wx.MessageBox('Keycard already in used. Enter another.', 'Warning', wx.OK | wx.ICON_WARNING)
                        self.ticket_keycard_list.AppendItem([keycard_number, status])
                        return
                    else: # keycard has history but not on lot
                        item_count = self.ticket_keycard_list.GetItemCount()
                        items = []
                        # Check if keycard in list in panel and change status
                        for i in range(item_count):
                            items.append(self.ticket_keycard_list.GetValue(i, 0))
                        if keycard_number in items:
                            for i in range(item_count):
                                if keycard_number == self.ticket_keycard_list.GetValue(i, 0):
                                    self.ticket_keycard_list.SetValue(status, i, 1)
                                    break
                        else:
                            self.ticket_keycard_list.AppendItem([keycard_number, status])
                else:
                    self.ticket_keycard_list.AppendItem([keycard_number, status])

                car_controller.add_car_with_keycard(keycard_number)
                self.keycard_enter_option.SetValue(False)
                self.keycard_static_text.Disable()
                self.keycard_textbox.Disable()
                self.keycard_textbox.Value = ''

            else:
                wx.MessageBox('Keycard does not exist. Enter another', 'Message', wx.OK)
                return

        else:
            wx.MessageBox('Need to select keycard or ticket', 'Message', wx.OK)

    def OnTicketEnterBtn(self, event):
        self.keycard_textbox.Value = self.keycard_textbox.GetLineText(0)
        self.keycard_static_text.Disable()
        self.keycard_textbox.Disable()

    def OnKeycardEnterBtn(self, event):
        self.keycard_static_text.Enable()
        self.keycard_textbox.Enable()
        self.keycard_textbox.Value = self.keycard_textbox.GetLineText(0)

    def OnCarExitClick(self, event):
        row_number = self.OnCarSelection(event)
        if row_number is None:
            wx.MessageBox('Must select a ticket/keycard from list first', 'Message', wx.OK)
            return

        selection = self.ticket_keycard_list.GetValue(row_number, 0)
        if self.keycard_exit_option.GetValue() == True:
            if selection[0] != 'K':
                wx.MessageBox('Ticket selected. Must select a keycard or switch to ticket option', 'Warning',
                              wx.OK | wx.ICON_WARNING)
                return

            lot_controller.ParkingMovementController.get_parking_movement(ticket_number=selection)
            keycard_history = lot_controller.ParkingMovementController.get_movement_list()
            latest_keycard_status = keycard_history[0][1]
            if latest_keycard_status == 'Exit':
                wx.MessageBox('Keycard already off lot. Select different keycard.', 'Message', wx.OK)
                return

            car_controller.exit_car_with_keycard(selection)
            wx.MessageBox(f'Exiting with keycard: {selection}', 'Message', wx.OK)
            self.ticket_keycard_list.SetValue('Off Lot', row_number, 1)
            self.keycard_exit_option.SetValue(False)

        elif self.ticket_exit_option.GetValue() == True:
            if selection[0] != 'T':
                wx.MessageBox('Keycard selected. Must select a ticket or switch to keycard option', 'Warning',
                              wx.OK | wx.ICON_WARNING)
                return

            # Get and check status(Entry/Exit) of car
            lot_controller.ParkingMovementController.get_parking_movement(ticket_number=selection)
            ticket_history = lot_controller.ParkingMovementController.get_movement_list()
            latest_ticket_status = ticket_history[0][1]

            if latest_ticket_status == 'Exit':
                wx.MessageBox('Ticket already paid for. Select different ticket.', 'Message', wx.OK)
                return

            if self.payment_option == 0:
                wx.MessageBox('Select payment option', 'Message', wx.OK)
                return
            else:
                if self.amount_textbox.Value == '':
                    wx.MessageBox('Input cash amount', 'Message', wx.OK)
                    return
                payment_type = self.payment_ticket_choices.GetString(self.payment_option)
                car_controller.exit_car_with_ticket(selection, float(self.amount_textbox.Value), payment_type)
                wx.MessageBox(f'Exiting with ticket: {selection}\nAmount paid: ${self.amount_textbox.Value}', 'Message',
                              wx.OK)
                self.ticket_keycard_list.SetValue('Off Lot', row_number, 1)
                self.payment_option = 0
                self.exit_ticket_payment_text_sizer.Clear(True)
                self.exit_ticket_payment_choices_sizer.Clear(True)
                self.exit_ticket_amount_sizer.Clear(True)
                self.ticket_exit_option.SetValue(False)
                self.Layout()

        elif self.validation_exit_option.GetValue() == True:
            if selection[0] != 'T':
                wx.MessageBox('Keycard selected. Must select a ticket or switch to keycard option', 'Warning',
                              wx.OK | wx.ICON_WARNING)
                return

            # Get and check status(Entry/Exit) of car
            lot_controller.ParkingMovementController.get_parking_movement(ticket_number=selection)
            ticket_history = lot_controller.ParkingMovementController.get_movement_list()
            latest_ticket_status = ticket_history[0][1]

            if latest_ticket_status == 'Exit':
                wx.MessageBox('Ticket already paid for. Select different ticket.', 'Message', wx.OK)
                return

            if self.payment_option == 0:
                wx.MessageBox('Select payment option', 'Message', wx.OK)
                return
            else:
                if self.amount_validation_textbox.Value == '':
                    wx.MessageBox('Input cash amount', 'Message', wx.OK)
                    return
                payment_type = self.payment_validations_choices.GetString(self.payment_option)
                car_controller.exit_car_with_validation(selection, float(self.amount_validation_textbox.Value), payment_type)
                wx.MessageBox(f'Exiting with ticket: {selection}\nAmount paid: ${self.amount_validation_textbox.Value}', 'Message',
                              wx.OK)
                self.ticket_keycard_list.SetValue('Off Lot', row_number, 1)
                self.payment_option = 0
                self.exit_validation_payment_text_sizer.Clear(True)
                self.exit_validation_payment_choices_sizer.Clear(True)
                self.exit_validation_amount_sizer.Clear(True)
                self.validation_exit_option.SetValue(False)
                self.Layout()

        else:
            wx.MessageBox('Need to select keycard/ticket option', 'Message', wx.OK)

    def OnKeycardExitBtn(self, event):
        self.exit_ticket_payment_text_sizer.Clear(True)
        self.exit_ticket_payment_choices_sizer.Clear(True)
        self.exit_ticket_amount_sizer.Clear(True)
        self.exit_validation_payment_text_sizer.Clear(True)
        self.exit_validation_payment_choices_sizer.Clear(True)
        self.exit_validation_amount_sizer.Clear(True)
        self.Layout()

    def OnTicketExitBtn(self, event):
        self.exit_validation_payment_text_sizer.Clear(True)
        self.exit_validation_payment_choices_sizer.Clear(True)
        self.exit_validation_amount_sizer.Clear(True)
        self.payment_option = 0

        self.exit_ticket_payment_text_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        self.payment_ticket_static_text = wx.StaticText(self, wx.ID_ANY, u"Payment:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.payment_ticket_static_text.Wrap(-1)
        self.exit_ticket_payment_text_sizer.Add(self.payment_ticket_static_text, 0, wx.ALL, 5)

        self.exit_ticket_payment_choices_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        payment_tickets = [wx.EmptyString, u"Cash", u"Credit", u"Debit"]
        self.payment_ticket_choices = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, payment_tickets, 0)
        self.payment_ticket_choices.SetSelection(0)
        self.exit_ticket_payment_choices_sizer.Add(self.payment_ticket_choices, 0, wx.ALL, 5)

        self.payment_ticket_choices.Bind(wx.EVT_CHOICE, self.OnPaymentChoice)

        self.exit_ticket_amount_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        self.amount_ticket_static_text = wx.StaticText(self, wx.ID_ANY, u"Enter amount:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.amount_ticket_static_text.Wrap(-1)
        self.exit_ticket_amount_sizer.Add(self.amount_ticket_static_text, 0, wx.ALL, 5)

        self.amount_textbox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.exit_ticket_amount_sizer.Add(self.amount_textbox, 0, wx.ALL, 5)

        self.Layout()

    def OnValidationExitBtn(self, event):
        self.exit_ticket_payment_text_sizer.Clear(True)
        self.exit_ticket_payment_choices_sizer.Clear(True)
        self.exit_ticket_amount_sizer.Clear(True)
        self.payment_option = 0

        self.exit_validation_payment_text_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        self.payment_validation_static_text = wx.StaticText(self, wx.ID_ANY, u"Payment", wx.DefaultPosition, wx.DefaultSize, 0)
        self.payment_validation_static_text.Wrap(-1)
        self.exit_validation_payment_text_sizer.Add(self.payment_validation_static_text, 0, wx.ALL, 5)

        self.exit_validation_payment_choices_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        payment_validations = [wx.EmptyString, u"Disability", u"Child", u"Senior"]
        self.payment_validations_choices = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, payment_validations, 0)
        self.payment_validations_choices.SetSelection(0)
        self.exit_validation_payment_choices_sizer.Add(self.payment_validations_choices, 0, wx.ALL, 5)

        self.payment_validations_choices.Bind(wx.EVT_CHOICE, self.OnPaymentChoice)

        self.exit_validation_amount_sizer.Add((45, 0), 0, wx.EXPAND, 5)
        self.amount_ticket_static_text = wx.StaticText(self, wx.ID_ANY, u"Enter amount:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.amount_ticket_static_text.Wrap(-1)
        self.exit_validation_amount_sizer.Add(self.amount_ticket_static_text, 0, wx.ALL, 5)

        self.amount_validation_textbox = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.exit_validation_amount_sizer.Add(self.amount_validation_textbox, 0, wx.ALL, 5)

        self.Layout()

    def OnPaymentChoice(self, event):
        self.payment_option = event.GetSelection()

    def OnEntryGateBox(self, event):
        pass

    def OnExitGateBox(self, event):
        pass


def main():
    app = wx.App()
    testing_frame = TestingFrame(None)
    testing_frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
