# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Mar 23 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 648,387 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Lot A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer5.Add( self.m_staticText4, 0, wx.ALIGN_CENTER, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Car enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Car exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Gate arm open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Gate arm close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button81 = wx.Button( self, wx.ID_ANY, u"Add new car", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button81, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.ALIGN_CENTER, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.m_textCtrl3, 1, wx.ALL, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Search car", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button13, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer10, 0, wx.ALIGN_CENTER, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )

		# Grid
		self.m_grid2.CreateGrid( 10, 4 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.SetColSize( 0, 100 )
		self.m_grid2.SetColSize( 1, 100 )
		self.m_grid2.SetColSize( 2, 100 )
		self.m_grid2.SetColSize( 3, 99 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"Ticket Number" )
		self.m_grid2.SetColLabelValue( 1, u"Space Number" )
		self.m_grid2.SetColLabelValue( 2, u"Status" )
		self.m_grid2.SetColLabelValue( 3, u"Validation" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 1 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer12.Add( self.m_grid2, 0, wx.ALIGN_CENTER, 5 )


		bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# dummy data
		self.m_grid2.SetCellValue(0, 0, '362839')
		self.m_grid2.SetCellValue(0, 1, '21')
		self.m_grid2.SetCellValue(0, 2, 'On Lot')
		self.m_grid2.SetCellValue(0, 3, 'Yes')

		self.m_grid2.SetCellValue(1, 0, '18923')
		self.m_grid2.SetCellValue(1, 1, '1')
		self.m_grid2.SetCellValue(1, 2, 'On Lot')
		self.m_grid2.SetCellValue(1, 3, 'No')

		self.m_grid2.SetCellValue(2, 0, '93439')
		self.m_grid2.SetCellValue(2, 1, '32')
		self.m_grid2.SetCellValue(2, 2, 'Away')
		self.m_grid2.SetCellValue(2, 3, 'Yes')

		self.m_grid2.SetCellValue(3, 0, '32444')
		self.m_grid2.SetCellValue(3, 1, '10')
		self.m_grid2.SetCellValue(3, 2, 'On Lot')
		self.m_grid2.SetCellValue(3, 3, 'No')

		self.m_grid2.SetCellValue(4, 0, '569843')
		self.m_grid2.SetCellValue(4, 1, '11')
		self.m_grid2.SetCellValue(4, 2, 'Away')
		self.m_grid2.SetCellValue(4, 3, 'Yes')

	def __del__( self ):
		pass


def main():
	app = wx.App()
	mainFrame = MyFrame1(None)
	mainFrame.Show()
	app.MainLoop()

if __name__ == '__main__':
    main()

