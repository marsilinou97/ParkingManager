# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Mar 23 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import random

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800, 600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Lot A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )

		bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer10.SetMinSize( wx.Size( -1,150 ) )
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Car enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer17.Add( ( 25, 0), 0, wx.EXPAND, 5 )

		self.m_radioBtn8 = wx.RadioButton( self, wx.ID_ANY, u"Ticket", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		bSizer17.Add( self.m_radioBtn8, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer18.Add( ( 25, 0), 0, wx.EXPAND, 5 )

		self.m_radioBtn9 = wx.RadioButton( self, wx.ID_ANY, u"Keycard", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_radioBtn9, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer201 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer201.Add((45, 0), 0, wx.EXPAND, 5)

		self.m_staticText41 = wx.StaticText(self, wx.ID_ANY, u"Enter keycard number:", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText41.Wrap(-1)
		self.m_staticText41.Disable()

		bSizer201.Add(self.m_staticText41, 0, wx.ALL, 5)

		self.m_textCtrl31 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrl31.Disable()
		bSizer201.Add(self.m_textCtrl31, 0, wx.ALL, 5)

		bSizer14.Add(bSizer201, 1, wx.EXPAND, 5)

		bSizer10.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer11.SetMinSize( wx.Size( -1,150 ) )
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Car exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer19.Add( ( 25, 0), 0, wx.EXPAND, 5 )

		self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"Keycard", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		bSizer19.Add( self.m_radioBtn10, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer20.Add( ( 25, 0), 0, wx.EXPAND, 5 )

		self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"Ticket", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_radioBtn11, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer21.Add( ( 45, 0), 0, wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Payment:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer21.Add( self.m_staticText21, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer171.Add( ( 45, 0), 0, wx.EXPAND, 5 )

		m_choice3Choices = [ wx.EmptyString, u"Cash", u"Credit/Debit" ]
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		self.m_choice3.Disable()
		bSizer171.Add( self.m_choice3, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer171, 1, wx.EXPAND, 5 )

		self.bSizer181 = wx.BoxSizer( wx.HORIZONTAL )


		self.bSizer181.Add( ( 45, 0), 0, wx.EXPAND, 5 )


		bSizer15.Add( self.bSizer181, 1, wx.EXPAND, 5 )


		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer191.Add( ( 45, 0), 0, wx.EXPAND, 5 )


		bSizer15.Add( bSizer191, 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )


		bSizer7.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button41 = wx.Button(self, wx.ID_ANY, u"Gate Arm - Open", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer13.Add(self.m_button41, 0, wx.ALL, 5)

		self.m_button51 = wx.Button(self, wx.ID_ANY, u"Gate Arm - Close", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer13.Add(self.m_button51, 0, wx.ALL, 5)

		bSizer7.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,530 ), 0 )
		self.m_dataViewListColumn1 = self.m_dataViewListCtrl4.AppendTextColumn( u"Ticket/Keycard No.", wx.dataview.DATAVIEW_CELL_ACTIVATABLE, 200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn2 = self.m_dataViewListCtrl4.AppendTextColumn( u"Status", wx.dataview.DATAVIEW_CELL_ACTIVATABLE, 200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer8.Add( self.m_dataViewListCtrl4, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnCarEnterClick )
		self.m_radioBtn8.Bind( wx.EVT_RADIOBUTTON, self.OnTicketEnterBtn )
		self.m_radioBtn9.Bind( wx.EVT_RADIOBUTTON, self.OnKeycardEnterBtn )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnCarExitClick )
		self.m_radioBtn10.Bind( wx.EVT_RADIOBUTTON, self.OnKeycardExitBtn )
		self.m_radioBtn11.Bind( wx.EVT_RADIOBUTTON, self.OnTicketExitBtn )
		self.m_choice3.Bind( wx.EVT_CHOICE, self.OnPaymentChoice )
		self.m_button41.Bind(wx.EVT_BUTTON, self.OnGateOpenBtn)
		self.m_button51.Bind(wx.EVT_BUTTON, self.OnGateCloseBtn)
		self.m_dataViewListCtrl4.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.OnCarDoubleClick, id = wx.ID_ANY )
		self.m_dataViewListCtrl4.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.OnCarSelection, id = wx.ID_ANY )

		### dummy data
		data = []
		for i in range(20):
			carID = str(i)
			status = ''
			r = random.randint(0, 1)
			if r == 0:
				status = 'off lot'
			else:
				status = 'on lot'
			data.append([carID, status])

		for i in range(len(data)):
			self.m_dataViewListCtrl4.AppendItem(data[i])
		###

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def OnCarDoubleClick( self, event ):
		print(self.m_dataViewListCtrl4.GetItemData(event.GetItem()))
		print(self.m_dataViewListCtrl4.GetSelectedRow())
		rowNo = self.m_dataViewListCtrl4.GetSelectedRow()
		print(self.m_dataViewListCtrl4.GetValue(rowNo, 0))
		print(self.m_dataViewListCtrl4.GetValue(rowNo, 1))

	def OnCarSelection(self, event):
		rowNo = self.m_dataViewListCtrl4.GetSelectedRow()
		print(rowNo)
		if rowNo == -1:
			return None
		return self.m_dataViewListCtrl4.GetValue(rowNo, 0)

	def OnCarEnterClick( self, event ):
		if self.m_radioBtn8.GetValue() == True:
			ticketNo = self.m_dataViewListCtrl4.GetItemCount()
			status = 'on lot'
			self.m_dataViewListCtrl4.AppendItem([str(ticketNo), status])
			print('entering with ticket:', ticketNo)
			self.m_radioBtn8.SetValue(False)

		elif self.m_radioBtn9.GetValue() == True:
			keycardNo = self.m_textCtrl31.Value
			items = self.m_dataViewListCtrl4.GetItemCount()
			for i in range(items):
				if keycardNo == self.m_dataViewListCtrl4.GetValue(i, 0):
					if self.m_dataViewListCtrl4.GetValue(i, 1) == 'off lot':
						self.m_dataViewListCtrl4.SetValue('on lot', i, 1)
						return
					else:
						print('keycard already in used. enter another')
						return

			status = 'on lot'
			self.m_dataViewListCtrl4.AppendItem([keycardNo, status])
			print('entering with keycard:', keycardNo)
			self.m_radioBtn9.SetValue(False)
			self.m_staticText41.Disable()
			self.m_textCtrl31.Disable()
			self.m_textCtrl31.Value = ''
		else:
			print('select ticket or keycard')

	def OnTicketEnterBtn( self, event ):
		self.m_textCtrl31.Value = self.m_textCtrl31.GetLineText(0)
		self.m_staticText41.Disable()
		self.m_textCtrl31.Disable()

	def OnKeycardEnterBtn( self, event ):
		self.m_staticText41.Enable()
		self.m_textCtrl31.Enable()
		self.m_textCtrl31.Value = self.m_textCtrl31.GetLineText(0)

	def OnCarExitClick( self, event ):
		# print(event.GetId())
		# print(self.OnCarSelection(event))
		if self.OnCarSelection(event) is None:
			print('select car first')
			return
		if self.m_radioBtn10.GetValue() == False and self.m_radioBtn11.GetValue() == False:
			print('Need to select keycard or ticket to exit')

	def OnKeycardExitBtn( self, event ):
		self.m_choice3.Disable()
		self.m_choice3.SetSelection(0)
		self.bSizer181.Clear(True)

	def OnTicketExitBtn( self, event ):
		self.m_choice3.Enable()

	def OnPaymentChoice( self, event ):
		print(event.GetSelection())
		if event.GetSelection() == 1:
			print('cash selected')
			self.bSizer181.Clear(True)
			self.bSizer181.Add((45, 0), 0, wx.EXPAND, 5)

			self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Enter amount:", wx.DefaultPosition, wx.DefaultSize, 0)
			self.m_staticText4.Wrap(-1)

			self.bSizer181.Add(self.m_staticText4, 0, wx.ALL, 5)

			self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
			self.bSizer181.Add(self.m_textCtrl3, 0, wx.ALL, 5)
			self.bSizer181.Layout()

		elif event.GetSelection() == 2:
			print('credit/debit selected')
			self.bSizer181.Clear(True)
			self.bSizer181.Add((45, 0), 0, wx.EXPAND, 5)

			self.m_button5 = wx.Button(self, wx.ID_ANY, u"Swipe card", wx.DefaultPosition, wx.DefaultSize, 0)
			self.bSizer181.Add(self.m_button5, 0, wx.ALL, 5)
			self.bSizer181.Layout()

	def OnGateOpenBtn(self, event):
		print('gate open')

	def OnGateCloseBtn(self, event):
		print('gate close')


def main():
	app = wx.App()
	mainFrame = MyFrame1(None)
	mainFrame.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()

