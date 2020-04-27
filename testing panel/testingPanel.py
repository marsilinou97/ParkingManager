import wx
import wx.xrc
import wx.dataview
import datetime

import CarController as car_controller
import ParkingLotcontroller as lot_controller


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        self.m_textCtrl3 = None
        self.cardPayment = False
        self.paymentOption = 0

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Testing Panel', pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Lot A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(
            wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer2.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer6.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer10.SetMinSize(wx.Size(-1, 150))
        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Car enter", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_button3, 0, wx.ALL, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer17.Add((25, 0), 0, wx.EXPAND, 5)
        self.m_radioBtn8 = wx.RadioButton(self, wx.ID_ANY, u"Ticket", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        bSizer17.Add(self.m_radioBtn8, 0, wx.ALL, 5)

        bSizer14.Add(bSizer17, 0, wx.EXPAND, 5)

        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer18.Add((25, 0), 0, wx.EXPAND, 5)
        self.m_radioBtn9 = wx.RadioButton(self, wx.ID_ANY, u"Keycard", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.m_radioBtn9, 0, wx.ALL, 5)

        bSizer14.Add(bSizer18, 0, wx.EXPAND, 5)

        bSizer201 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer201.Add((45, 0), 0, wx.EXPAND, 5)
        self.m_staticText41 = wx.StaticText(self, wx.ID_ANY, u"Enter keycard number:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        self.m_staticText41.Disable()
        bSizer201.Add(self.m_staticText41, 0, wx.ALL, 5)

        self.m_textCtrl31 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl31.Disable()
        bSizer201.Add(self.m_textCtrl31, 0, wx.ALL, 5)

        bSizer14.Add(bSizer201, 1, wx.EXPAND, 5)

        bSizer10.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer10, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        bSizer11.SetMinSize(wx.Size(-1, 150))
        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Car exit", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button4, 0, wx.ALL, 5)

        self.bSizer15 = wx.BoxSizer(wx.VERTICAL)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer19.Add((25, 0), 0, wx.EXPAND, 5)
        self.m_radioBtn10 = wx.RadioButton(self, wx.ID_ANY, u"Keycard", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        bSizer19.Add(self.m_radioBtn10, 0, wx.ALL, 5)

        self.bSizer15.Add(bSizer19, 0, wx.EXPAND, 5)

        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer20.Add((25, 0), 0, wx.EXPAND, 5)
        self.m_radioBtn11 = wx.RadioButton(self, wx.ID_ANY, u"Ticket", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.m_radioBtn11, 0, wx.ALL, 5)

        self.bSizer15.Add(bSizer20, 0, wx.EXPAND, 5)

        self.bSizer21 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer15.Add(self.bSizer21, 0, wx.EXPAND, 5)

        self.bSizer171 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer15.Add(self.bSizer171, 0, wx.EXPAND, 5)

        self.bSizer181 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer15.Add(self.bSizer181, 0, wx.EXPAND, 5)

        self.bSizer191 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer191.Add((25, 0), 0, wx.EXPAND, 5)
        self.m_radioBtn6 = wx.RadioButton(self, wx.ID_ANY, u"Validation", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer191.Add(self.m_radioBtn6, 0, wx.ALL, 5)
        self.bSizer15.Add(self.bSizer191, 0, wx.EXPAND, 5)

        self.bSizer211 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer15.Add(self.bSizer211, 0, wx.EXPAND, 5)

        self.bSizer22 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer15.Add(self.bSizer22, 0, wx.EXPAND, 5)

        self.bSizer23 = wx.BoxSizer(wx.HORIZONTAL)
        self.bSizer15.Add(self.bSizer23, 0, wx.EXPAND, 5)

        bSizer11.Add(self.bSizer15, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_button41 = wx.Button(self, wx.ID_ANY, u"Gate Arm - Open", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button41, 0, wx.ALL, 5)

        self.m_button51 = wx.Button(self, wx.ID_ANY, u"Gate Arm - Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button51, 0, wx.ALL, 5)

        bSizer7.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 530),
                                                                0)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl4.AppendTextColumn(u"Ticket/Keycard No.",
                                                                               wx.dataview.DATAVIEW_CELL_ACTIVATABLE,
                                                                               200, wx.ALIGN_LEFT,
                                                                               wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl4.AppendTextColumn(u"Status",
                                                                               wx.dataview.DATAVIEW_CELL_ACTIVATABLE,
                                                                               200, wx.ALIGN_LEFT,
                                                                               wx.dataview.DATAVIEW_COL_RESIZABLE)
        bSizer8.Add(self.m_dataViewListCtrl4, 0, wx.ALL, 5)

        bSizer3.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnCarEnterClick)
        self.m_radioBtn8.Bind(wx.EVT_RADIOBUTTON, self.OnTicketEnterBtn)
        self.m_radioBtn9.Bind(wx.EVT_RADIOBUTTON, self.OnKeycardEnterBtn)
        self.m_button4.Bind(wx.EVT_BUTTON, self.OnCarExitClick)
        self.m_radioBtn10.Bind(wx.EVT_RADIOBUTTON, self.OnKeycardExitBtn)
        self.m_radioBtn11.Bind(wx.EVT_RADIOBUTTON, self.OnTicketExitBtn)
        self.m_radioBtn6.Bind(wx.EVT_RADIOBUTTON, self.OnValidationExitBtn)
        self.m_button41.Bind(wx.EVT_BUTTON, self.OnGateOpenBtn)
        self.m_button51.Bind(wx.EVT_BUTTON, self.OnGateCloseBtn)
        self.m_dataViewListCtrl4.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.OnCarDoubleClick, id=wx.ID_ANY)
        self.m_dataViewListCtrl4.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.OnCarSelection, id=wx.ID_ANY)


    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnCarDoubleClick(self, event):
        pass

    # print(self.m_dataViewListCtrl4.GetItemData(event.GetItem()))
    # print(self.m_dataViewListCtrl4.GetSelectedRow())
    # rowNo = self.m_dataViewListCtrl4.GetSelectedRow()
    # print(self.m_dataViewListCtrl4.GetValue(rowNo, 0))
    # print(self.m_dataViewListCtrl4.GetValue(rowNo, 1))

    def OnCarSelection(self, event):
        rowNo = self.m_dataViewListCtrl4.GetSelectedRow()
        if rowNo == -1:
            return None
        return rowNo

    def OnCarEnterClick(self, event):
        status = 'on lot'
        if self.m_radioBtn8.GetValue() == True:
            ticketNo = car_controller.add_car_with_ticket()
            self.m_dataViewListCtrl4.AppendItem([ticketNo, status])
            self.m_radioBtn8.SetValue(False)

        elif self.m_radioBtn9.GetValue() == True:
            if self.m_textCtrl31.Value == '':
                wx.MessageBox('Input keycard number.', 'Message', wx.OK)
                return

            keycardNo = self.m_textCtrl31.Value
            ## Check if keycard exist ##
            if car_controller.check_existing_keycard(keycardNo):
                ## Check if keycard exist in lot
                keycardNo = 'K_' + keycardNo
                date_str = '2020-04-24'
                my_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                lot_controller.ParkingMovementController.get_parking_movement(ticket_number=keycardNo, from_date=my_date)
                keycard_history = lot_controller.ParkingMovementController.get_movement_list()

                if keycard_history:
                    ## Check keycard's latest status
                    latest_keycard_status = keycard_history[0][1]
                    if latest_keycard_status == 'Entry':
                        wx.MessageBox('Keycard already in used. Enter another.', 'Warning', wx.OK | wx.ICON_WARNING)
                        return
                    else: ## keycard has history but not on lot
                        item_count = self.m_dataViewListCtrl4.GetItemCount()
                        items = []
                        ## Check if keycard in list in panel and change status
                        for i in range(item_count):
                            items.append(self.m_dataViewListCtrl4.GetValue(i, 0))
                        if keycardNo in items:
                            for i in range(item_count):
                                if keycardNo == self.m_dataViewListCtrl4.GetValue(i, 0):
                                    self.m_dataViewListCtrl4.SetValue(status, i, 1)
                                    break
                        else:
                            self.m_dataViewListCtrl4.AppendItem([keycardNo, status])
                else:
                    self.m_dataViewListCtrl4.AppendItem([keycardNo, status])

                car_controller.add_car_with_keycard(keycardNo)
                self.m_radioBtn9.SetValue(False)
                self.m_staticText41.Disable()
                self.m_textCtrl31.Disable()
                self.m_textCtrl31.Value = ''

            else:
                wx.MessageBox('Keycard does not exist. Enter another', 'Message', wx.OK)
                return

        else:
            wx.MessageBox('Need to select keycard or ticket', 'Message', wx.OK)

    def OnTicketEnterBtn(self, event):
        self.m_textCtrl31.Value = self.m_textCtrl31.GetLineText(0)
        self.m_staticText41.Disable()
        self.m_textCtrl31.Disable()

    def OnKeycardEnterBtn(self, event):
        self.m_staticText41.Enable()
        self.m_textCtrl31.Enable()
        self.m_textCtrl31.Value = self.m_textCtrl31.GetLineText(0)

    def OnCarExitClick(self, event):
        rowNo = self.OnCarSelection(event)
        selection = self.m_dataViewListCtrl4.GetValue(rowNo, 0)
        if rowNo is None:
            wx.MessageBox('Must select a ticket/keycard from list first', 'Message', wx.OK)
            return

        if self.m_radioBtn10.GetValue() == True:
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
            self.m_dataViewListCtrl4.SetValue('off lot', rowNo, 1)
            self.m_radioBtn10.SetValue(False)

        elif self.m_radioBtn11.GetValue() == True:
            if selection[0] != 'T':
                wx.MessageBox('Keycard selected. Must select a ticket or switch to keycard option', 'Warning',
                              wx.OK | wx.ICON_WARNING)
                return

            ## Get and check status(Entry/Exit) of car ##
            lot_controller.ParkingMovementController.get_parking_movement(ticket_number=selection)
            ticket_history = lot_controller.ParkingMovementController.get_movement_list()
            latest_ticket_status = ticket_history[0][1]

            if latest_ticket_status == 'Exit':
                wx.MessageBox('Ticket already paid for. Select different ticket.', 'Message', wx.OK)
                return

            if self.paymentOption == 0:
                wx.MessageBox('Select payment option', 'Message', wx.OK)
                return
            else:
                if self.m_textCtrl3.Value == '':
                    wx.MessageBox('Input cash amount', 'Message', wx.OK)
                    return
                payment_type = self.m_choice3.GetString(self.paymentOption)
                print(payment_type)
                car_controller.exit_car_with_ticket(selection, float(self.m_textCtrl3.Value), payment_type)
                wx.MessageBox(f'Exiting with ticket: {selection}\nAmount paid: ${self.m_textCtrl3.Value}', 'Message',
                              wx.OK)
                self.m_dataViewListCtrl4.SetValue('off lot', rowNo, 1)
                self.bSizer21.Clear(True)
                self.bSizer171.Clear(True)
                self.bSizer181.Clear(True)
                self.m_radioBtn11.SetValue(False)
                self.Layout()

        elif self.m_radioBtn6.GetValue() == True:
            if selection[0] != 'T':
                wx.MessageBox('Keycard selected. Must select a ticket or switch to keycard option', 'Warning',
                              wx.OK | wx.ICON_WARNING)
                return

            ## Get and check status(Entry/Exit) of car ##
            lot_controller.ParkingMovementController.get_parking_movement(ticket_number=selection)
            ticket_history = lot_controller.ParkingMovementController.get_movement_list()
            latest_ticket_status = ticket_history[0][1]

            if latest_ticket_status == 'Exit':
                wx.MessageBox('Ticket already paid for. Select different ticket.', 'Message', wx.OK)
                return

            if self.paymentOption == 0:
                wx.MessageBox('Select payment option', 'Message', wx.OK)
                return
            else:
                if self.m_textCtrl2.Value == '':
                    wx.MessageBox('Input cash amount', 'Message', wx.OK)
                    return
                paymentType = self.m_choice2.GetString(self.paymentOption)
                print(paymentType)
                car_controller.exit_car_with_validation(selection, float(self.m_textCtrl2.Value), paymentType)
                wx.MessageBox(f'Exiting with ticket: {selection}\nAmount paid: ${self.m_textCtrl2.Value}', 'Message',
                              wx.OK)
                self.m_dataViewListCtrl4.SetValue('off lot', rowNo, 1)
                self.bSizer211.Clear(True)
                self.bSizer22.Clear(True)
                self.bSizer23.Clear(True)
                self.m_radioBtn6.SetValue(False)
                self.Layout()

        else:
            wx.MessageBox('Need to select keycard/ticket option', 'Message', wx.OK)

    def OnKeycardExitBtn(self, event):
        self.bSizer21.Clear(True)
        self.bSizer171.Clear(True)
        self.bSizer181.Clear(True)
        self.bSizer211.Clear(True)
        self.bSizer22.Clear(True)
        self.bSizer23.Clear(True)
        self.Layout()

    def OnTicketExitBtn(self, event):
        self.bSizer211.Clear(True)
        self.bSizer22.Clear(True)
        self.bSizer23.Clear(True)

        self.bSizer21.Add((45, 0), 0, wx.EXPAND, 5)
        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"Payment:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        self.bSizer21.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.bSizer171.Add((45, 0), 0, wx.EXPAND, 5)
        m_choice3Choices = [wx.EmptyString, u"Cash", u"Credit", u"Debit"]
        self.m_choice3 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0)
        self.m_choice3.SetSelection(0)
        self.bSizer171.Add(self.m_choice3, 0, wx.ALL, 5)

        self.m_choice3.Bind(wx.EVT_CHOICE, self.OnPaymentChoice)

        self.bSizer181.Add((45, 0), 0, wx.EXPAND, 5)
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Enter amount:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.bSizer181.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer181.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.Layout()

    def OnValidationExitBtn(self, event):
        self.bSizer21.Clear(True)
        self.bSizer171.Clear(True)
        self.bSizer181.Clear(True)

        self.bSizer211.Add((45, 0), 0, wx.EXPAND, 5)
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Payment", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.bSizer211.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.bSizer22.Add((45, 0), 0, wx.EXPAND, 5)
        m_choice2Choices = [wx.EmptyString, u"Disability", u"Child", u"Senior"]
        self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        self.bSizer22.Add(self.m_choice2, 0, wx.ALL, 5)

        self.m_choice2.Bind(wx.EVT_CHOICE, self.OnPaymentChoice)

        self.bSizer23.Add((45, 0), 0, wx.EXPAND, 5)
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Enter amount:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.bSizer23.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer23.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.Layout()

    def OnPaymentChoice(self, event):
        self.paymentOption = event.GetSelection()

    def OnCardPayment(self, event):
        wx.MessageBox('Card swiped!', 'Message', wx.OK)
        self.cardPayment = True

    def OnGateOpenBtn(self, event):
        wx.MessageBox('Gate open', 'Message', wx.OK)

    def OnGateCloseBtn(self, event):
        wx.MessageBox('Gate close', 'Message', wx.OK)


def main():
    app = wx.App()
    mainFrame = MyFrame1(None)
    mainFrame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
