# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc

###########################################################################
## Class main
###########################################################################

class main ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"sscomplus v1.0", pos = wx.DefaultPosition, size = wx.Size( 778,496 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSleft = wx.BoxSizer( wx.VERTICAL )
		
		bSport = wx.BoxSizer( wx.VERTICAL )
		
		self.Port_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"串口号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Port_lab.Wrap( -1 )
		self.Port_lab.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSport.Add( self.Port_lab, 1, wx.ALL|wx.EXPAND, 5 )
		
		Port_cmbChoices = []
		self.Port_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, Port_cmbChoices, 0 )
		self.Port_cmb.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSport.Add( self.Port_cmb, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Port_but = wx.Button( self.m_panel1, wx.ID_ANY, u"打开串口", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSport.Add( self.Port_but, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.DTR_chk = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"DTR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.DTR_chk, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.RTC_chk = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"RTC", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.RTC_chk, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSport.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		
		bSleft.Add( bSport, 1, wx.EXPAND, 5 )
		
		bSarg = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Baudrate_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"波特率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Baudrate_lab.Wrap( -1 )
		bSizer5.Add( self.Baudrate_lab, 1, wx.ALL|wx.EXPAND, 5 )
		
		Baudrate_cmbChoices = [ u"110", u"300", u"600", u"1200", u"2400", u"4800", u"9600", u"14400", u"19200", u"38400", u"56000", u"57600", u"115200", u"128000", u"256000", u"230400", u"460800", u"921600" ]
		self.Baudrate_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"1200", wx.DefaultPosition, wx.DefaultSize, Baudrate_cmbChoices, 0 )
		self.Baudrate_cmb.SetSelection( 3 )
		bSizer5.Add( self.Baudrate_cmb, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSarg.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Bytesize_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"数据位", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Bytesize_lab.Wrap( -1 )
		bSizer51.Add( self.Bytesize_lab, 1, wx.ALL|wx.EXPAND, 5 )
		
		Bytesize_cmbChoices = [ u"5", u"6", u"7", u"8" ]
		self.Bytesize_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, Bytesize_cmbChoices, 0 )
		bSizer51.Add( self.Bytesize_cmb, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSarg.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Stopbits_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"停止位", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Stopbits_lab.Wrap( -1 )
		bSizer52.Add( self.Stopbits_lab, 1, wx.ALL|wx.EXPAND, 5 )
		
		Stopbits_cmbChoices = [ u"1", u"1.5", u"2" ]
		self.Stopbits_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, Stopbits_cmbChoices, 0 )
		bSizer52.Add( self.Stopbits_cmb, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSarg.Add( bSizer52, 1, wx.EXPAND, 5 )
		
		bSizer53 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Parity_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"校验位", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Parity_lab.Wrap( -1 )
		bSizer53.Add( self.Parity_lab, 1, wx.ALL|wx.EXPAND, 5 )
		
		Parity_cmbChoices = [ u"N", u"O", u"E", u"M", u"S" ]
		self.Parity_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"N", wx.DefaultPosition, wx.DefaultSize, Parity_cmbChoices, 0 )
		bSizer53.Add( self.Parity_cmb, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSarg.Add( bSizer53, 1, wx.EXPAND, 5 )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Flow_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"流控制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Flow_lab.Wrap( -1 )
		bSizer54.Add( self.Flow_lab, 1, wx.ALL|wx.EXPAND, 5 )
		
		Flow_cmbChoices = [ u"HW", u"SW", u"OFF" ]
		self.Flow_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, Flow_cmbChoices, 0 )
		self.Flow_cmb.SetSelection( 2 )
		bSizer54.Add( self.Flow_cmb, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSarg.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		
		bSleft.Add( bSarg, 1, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSleft, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSright = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"接收区" ), wx.VERTICAL )
		
		bSizer257 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer265 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText98 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )
		bSizer265.Add( self.m_staticText98, 1, wx.ALL, 5 )
		
		
		bSizer257.Add( bSizer265, 1, 0, 5 )
		
		bSizer331 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Hexrecv_chk = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"HEX显示", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.Hexrecv_chk, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Save_but = wx.Button( self.m_panel1, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.Save_but, 0, 0, 5 )
		
		self.Clrrecv_but = wx.Button( self.m_panel1, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.Clrrecv_but, 0, 0, 5 )
		
		
		bSizer257.Add( bSizer331, 0, 0, 5 )
		
		
		sbSizer2.Add( bSizer257, 0, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.Recv_txt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer2.Add( self.Recv_txt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer2.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		bSright.Add( sbSizer2, 5, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"发送区" ), wx.VERTICAL )
		
		bS_send = wx.BoxSizer( wx.VERTICAL )
		
		bSizer531 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer251 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.TPsend_chk = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"循环发送", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TPsend_chk.SetValue(True) 
		bSizer251.Add( self.TPsend_chk, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Second_txt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer251.Add( self.Second_txt, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Sec_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"ms/次", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Sec_lab.Wrap( -1 )
		bSizer251.Add( self.Sec_lab, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.HEXsend_chk = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"HEX发送", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer251.Add( self.HEXsend_chk, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.RN_chk = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"新行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RN_chk.SetValue(True) 
		bSizer251.Add( self.RN_chk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer531.Add( bSizer251, 1, wx.EXPAND, 5 )
		
		
		bS_send.Add( bSizer531, 0, wx.EXPAND, 5 )
		
		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Send_txt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.Send_txt, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Clrsend_but = wx.Button( self.m_panel1, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.Clrsend_but, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Send_but = wx.Button( self.m_panel1, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.Send_but, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bS_send.Add( bSizer521, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bS_send, 1, wx.EXPAND, 5 )
		
		
		bSright.Add( sbSizer1, 2, wx.EXPAND, 5 )
		
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"字符串定义" ), wx.VERTICAL )
		
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.strButton1 = wx.Button( self.m_panel1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.strButton1.SetMinSize( wx.Size( 30,-1 ) )
		self.strButton1.SetMaxSize( wx.Size( 100,-1 ) )
		
		bSizer112.Add( self.strButton1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.string1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.string1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.strButton2 = wx.Button( self.m_panel1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.strButton2.SetMinSize( wx.Size( 30,-1 ) )
		
		bSizer112.Add( self.strButton2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.string2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.string2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.strButton3 = wx.Button( self.m_panel1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.strButton3.SetMinSize( wx.Size( 30,-1 ) )
		
		bSizer112.Add( self.strButton3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.string3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.string3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer17.Add( bSizer112, 1, wx.EXPAND, 5 )
		
		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.strButton4 = wx.Button( self.m_panel1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.strButton4.SetMaxSize( wx.Size( 30,-1 ) )
		
		bSizer113.Add( self.strButton4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.string4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.string4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.strButton5 = wx.Button( self.m_panel1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.strButton5.SetMaxSize( wx.Size( 30,-1 ) )
		
		bSizer113.Add( self.strButton5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.string5 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.string5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.strButton6 = wx.Button( self.m_panel1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.strButton6.SetMaxSize( wx.Size( 30,-1 ) )
		
		bSizer113.Add( self.strButton6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.string6 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.string6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer17.Add( bSizer113, 1, wx.EXPAND, 5 )
		
		
		bSright.Add( sbSizer17, 2, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSright, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer24.Add( bSizer26, 1, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer24.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.Statue_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"准备", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Statue_lab.Wrap( -1 )
		sbSizer3.Add( self.Statue_lab, 13, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Send_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"已发送：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Send_lab.Wrap( -1 )
		sbSizer3.Add( self.Send_lab, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Send_num = wx.StaticText( self.m_panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Send_num.Wrap( -1 )
		sbSizer3.Add( self.Send_num, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Receive_lab = wx.StaticText( self.m_panel1, wx.ID_ANY, u"已接收：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Receive_lab.Wrap( -1 )
		sbSizer3.Add( self.Receive_lab, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Receive_num = wx.StaticText( self.m_panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Receive_num.Wrap( -1 )
		sbSizer3.Add( self.Receive_num, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Clear_but = wx.Button( self.m_panel1, wx.ID_ANY, u"清零", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Clear_but.SetMinSize( wx.Size( 50,25 ) )
		
		sbSizer3.Add( self.Clear_but, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer24.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer24 )
		self.m_panel1.Layout()
		bSizer24.Fit( self.m_panel1 )
		bSizer25.Add( self.m_panel1, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Port_cmb.Bind( wx.EVT_COMBOBOX_DROPDOWN, self.PortDropdown )
		self.Port_but.Bind( wx.EVT_BUTTON, self.Open_port )
		self.DTR_chk.Bind( wx.EVT_CHECKBOX, self.CH_DTR )
		self.RTC_chk.Bind( wx.EVT_CHECKBOX, self.CH_RTC )
		self.Hexrecv_chk.Bind( wx.EVT_CHECKBOX, self.bt_hexrecv )
		self.Clrrecv_but.Bind( wx.EVT_BUTTON, self.bt_clrrecv )
		self.TPsend_chk.Bind( wx.EVT_CHECKBOX, self.SendLoopClick )
		self.Second_txt.Bind( wx.EVT_TEXT, self.TextSecondChange )
		self.HEXsend_chk.Bind( wx.EVT_CHECKBOX, self.bt_hexsend )
		self.Clrsend_but.Bind( wx.EVT_BUTTON, self.bt_clrsend )
		self.Send_but.Bind( wx.EVT_BUTTON, self.bt_send )
		self.strButton1.Bind( wx.EVT_BUTTON, self.strButton1Click )
		self.strButton2.Bind( wx.EVT_BUTTON, self.strButton2Click )
		self.strButton3.Bind( wx.EVT_BUTTON, self.strButton3Click )
		self.strButton4.Bind( wx.EVT_BUTTON, self.strButton4Click )
		self.strButton5.Bind( wx.EVT_BUTTON, self.strButton5Click )
		self.strButton6.Bind( wx.EVT_BUTTON, self.strButton6Click )
		self.Clear_but.Bind( wx.EVT_BUTTON, self.clearClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def PortDropdown( self, event ):
		event.Skip()
	
	def Open_port( self, event ):
		event.Skip()
	
	def CH_DTR( self, event ):
		event.Skip()
	
	def CH_RTC( self, event ):
		event.Skip()
	
	def bt_hexrecv( self, event ):
		event.Skip()
	
	def bt_clrrecv( self, event ):
		event.Skip()
	
	def SendLoopClick( self, event ):
		event.Skip()
	
	def TextSecondChange( self, event ):
		event.Skip()
	
	def bt_hexsend( self, event ):
		event.Skip()
	
	def bt_clrsend( self, event ):
		event.Skip()
	
	def bt_send( self, event ):
		event.Skip()
	
	def strButton1Click( self, event ):
		event.Skip()
	
	def strButton2Click( self, event ):
		event.Skip()
	
	def strButton3Click( self, event ):
		event.Skip()
	
	def strButton4Click( self, event ):
		event.Skip()
	
	def strButton5Click( self, event ):
		event.Skip()
	
	def strButton6Click( self, event ):
		event.Skip()
	
	def clearClick( self, event ):
		event.Skip()
	

