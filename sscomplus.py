__author__ = 'Administrator'

import wx
import os
import device
import binascii
import threading
import rs232_UI
import string
import filestore
import time
import host
#configuration file
config = "conf.ini"

def call_after(func):
    def _wrapper(*args, **kwargs):
        return wx.CallAfter(func, *args, **kwargs)
    return _wrapper

def wxT(x):
    return x

def bytes_str(b_str):
    c_str = ""
    for n in b_str:
        c_str += chr(n)
    return c_str

def bytes_hex(b_str):
    h_str = ""
    for n in b_str:
        h_str += '{0:02X}'.format(n) + " "
        #h_str += hex(n) + " "
    return h_str
def hexstr_bytes(str):
    i =0
    t = ''
    bytes = bytearray()
    for n in str:
        i = i + 1
        t += n
        if len(t) == 2 or i == len(str):
            bytes.append(int(t.zfill(2),16))
            t = ''
    return bytes

class MyApp(rs232_UI.main):
    def __init__(self):
        rs232_UI.main.__init__(self, None)
        self.recv_data = ""
        self.portlist = ()
        self.reflash_port()
        self.SendLoopFlag = False
        self.SendLoopTime = 0
        self.timer = wx.Timer(self)
        self.send_count = 0
        self.read_count = 0
        self.SerialStatus = 'close'
        self.HexDisplay = False
        self.Hexrecv_chk.SetValue(False)
        self.HexSend = False
        self.HEXsend_chk.SetValue(False)
        self.NewLine = False
        self.RN_chk.SetValue(False)
        self.TPsend_chk.SetValue(False)
        self.RN_chk.SetValue(False)
        self.HOST.SetValue(False)
        self.HOST_Protocol = False
        self.ButtonStatus = 'send'
        dataConfig = filestore.loadConfig(config)
        print("configuration:",dataConfig)
        self.Baudrate_cmb.SetValue(dataConfig['baud'])
        self.Bytesize_cmb.SetValue(dataConfig['data'])
        self.Stopbits_cmb.SetValue(dataConfig['stop'])
        self.string1.SetValue(dataConfig['str1'])
        self.string2.SetValue(dataConfig['str2'])
        self.string3.SetValue(dataConfig['str3'])
        self.string4.SetValue(dataConfig['str4'])
        self.string5.SetValue(dataConfig['str5'])
        self.string6.SetValue(dataConfig['str6'])
        self.string7.SetValue(dataConfig['str7'])
        self.string8.SetValue(dataConfig['str8'])
        self.string9.SetValue(dataConfig['str9'])
        self.string10.SetValue(dataConfig['strA'])

    def StartTimer(self,cb,interval):
        self.Bind(wx.EVT_TIMER,cb,self.timer)
        self.timer.Start(interval)
    def StopTimer(self):
        self.timer.Stop()
    def reflash_port(self):
         list = device.reflash_port()
         if len(self.portlist) != len(list):
             self.portlist = list[:]
             self.Port_cmb.Clear()
             self.Port_cmb.Append(list)
    def PortDropdown(self,event):
        self.reflash_port()
    def GetData(self):
        SendData = self.Send_txt.GetValue()
        if self.HOST_Protocol:
            SendData = bytearray(SendData,'utf-8')
            SendData = host.urat_encode(SendData)
        elif self.NewLine and self.HexSend:
            SendData = hexstr_bytes(SendData)
            SendData.append(13)
            SendData.append(10)
        elif not self.NewLine and self.HexSend:
            SendData = hexstr_bytes(SendData)
        elif self.NewLine and not self.HexSend:
            SendData += '\r\n'
            SendData = bytearray(SendData,'utf-8')
        else:
            SendData = bytearray(SendData,'utf-8')
        return SendData

    def Open_port(self,event):
         if self.Port_cmb.GetCurrentSelection() == -1:
             return 0
         try:
             if self.SerialStatus == 'close':
                 self.ser = device.MyCom(Port      =   self.Port_cmb.GetValue(),
                                         BaudRate  =   self.Baudrate_cmb.GetValue(),
                                         ByteSize  =   self.Bytesize_cmb.GetValue(),
                                         Parity    =   self.Parity_cmb.GetValue(),
                                         Stopbits  =   self.Stopbits_cmb.GetValue())
                 if self.ser.start():
                     self.ser.waitEnd = threading.Event()
                     flow = self.Flow_cmb.GetValue()
                     if flow == "HW":
                         self.ser.l_serial.rtscts = True
                         self.ser.l_serial.xonxoff = False
                     elif flow == "SW":
                         self.ser.l_serial.xonxoff = True
                         self.ser.l_serial.rtscts = False
                     elif flow == "OFF":
                         self.ser.l_serial.rtscts = False
                         self.ser.l_serial.xonxoff = False
                     statue_name = self.ser.l_serial.port + wxT("已打开")
                     self.Statue_lab.SetLabel(statue_name)
                     self.Port_but.SetLabel(wxT("关闭串口"))
                     self.SerialStatus = 'open'
                     self.read_thread = threading.Thread(target=self.read)
                     self.read_thread.setDaemon(True)
                     self.read_thread.start()
                 else:
                     statue_name = self.ser.l_serial.port + wxT("打开失败")
                     self.Statue_lab.SetLabel(statue_name)
                     self.ser.stop()
             elif self.SerialStatus == 'open':
                 self.ser.SetStopEvent()
                 self.read_thread.join()
                 self.Statue_lab.SetLabel(wxT("准备"))
                 self.Port_but.SetLabel(wxT("打开串口"))
                 self.SerialStatus = 'close'
         except Exception as ex:
             print("Exception:Open_port()")
             statue_name = self.Port_cmb.GetValue() + wxT("打开失败")
             self.Statue_lab.SetLabel(statue_name)

    @call_after
    def UpdateReceiveTxt(self,receive,count):
        self.Recv_txt.AppendText(receive)
        self.Receive_num.SetLabel(str(count))
    def read(self):
        try:
             while self.ser.alive:
                 n = self.ser.l_serial.inWaiting()
                 if n:
                     msg = self.ser.l_serial.read(n)
                     if self.HOST_Protocol:
                         msg = host.urat_decode(msg)
                         if msg == None:
                             continue
                     if self.HexDisplay == True:
                         m = bytes_hex(msg)
                     else:
                         m = bytes_str(msg)
                     self.read_count = self.read_count + n
                     self.UpdateReceiveTxt(m,self.read_count)
                 time.sleep(0.001)
                 #end if
             #end while
        except:
             print("fault:read()")
             raise

    def write(self,event):
        try:
            if self.ser:
                send_data = self.GetData()
                self.send_count = self.send_count + len(send_data)
                self.Send_num.SetLabel(str(self.send_count))
                self.ser.l_serial.write(send_data)
        except:
            print("fault:write()")
            raise
        #end if

    def SendLoopClick( self, event ):
        if (self.TPsend_chk.GetValue() == True) and (self.Second_txt.GetValue().isdigit() == True):
            self.SendLoopFlag = True
            self.SendLoopTime = int(self.Second_txt.GetValue())
        else:
            self.TPsend_chk.SetValue(False)
            self.SendLoopFlag = False
            self.SendLoopTime = 0

    def TextSecondChange(self,event):
        if self.Second_txt.GetValue().isdigit() == False:
            self.TPsend_chk.SetValue(False)
            self.SendLoopFlag = False
            self.SendLoopTime = 0

    def HostClick(self,event):
        if self.HOST.GetValue() == True:
            self.HOST_Protocol = True
        else:
            self.HOST_Protocol = False

    def ExtraFunClick(self,event):
        if self.Extra_func.GetValue() == True:
            self.Extra_panel.Show()
            self.Layout()
        else:
            self.Extra_panel.Hide()
            self.Layout()

    def bt_send(self,event):
        SendData = self.Send_txt.GetValue()
        if SendData == '' or (not self.ser.alive):
            return
        if self.ButtonStatus == 'pause':
            self.StopTimer()
            self.ButtonStatus = 'send'
            self.Send_but.SetLabel(wxT("发送"))
        elif self.ButtonStatus == 'send' and self.SendLoopFlag:
            print('send loop')
            self.StartTimer(self.write,self.SendLoopTime)
            self.ButtonStatus = 'pause'
            self.Send_but.SetLabel(wxT("暂停"))
        else:
            self.write(None)

    def bt_clrsend(self,event):
        self.Send_txt.SetValue("")
    def bt_clrrecv(self,event):
        self.Recv_txt.SetValue("")
    def bt_hexsend(self,event):
        if self.HEXsend_chk.GetValue() == True:
            self.HexSend = True
        else:
            self.HexSend = False
    def bt_hexrecv(self,event):
        if self.Hexrecv_chk.GetValue() == True:
            self.HexDisplay = True
        else:
            self.HexDisplay = False
    def NewLineClick( self, event ):
        if self.RN_chk.GetValue() == True:
            self.NewLine = True
        else:
            self.NewLine = False
    def CH_DTR(self,event):
        if self.Port_but.GetLabel() == wxT("打开串口"):
            return
        if self.DTR_chk.GetValue() == True:
            self.ser.l_serial.dsrdtr = True
        else:
            self.ser.l_serial.dsrdtr = False
        #end if
    def CH_RTC(self,event):
        if self.Port_but.GetLabel() == wxT("打开串口"):
            return
        if self.RTC_chk.GetValue() == True:
            self.ser.l_serial.rtscts = True
        else:
            self.ser.l_serial.rtscts = False
        #end if
    def strButton1Click(self,event):
        tmp = self.string1.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str1",tmp)
    def strButton2Click(self,event):
        tmp = self.string2.GetValue()
        self.Send_txt.SetValue(tmp)
        print(tmp)
        filestore.writeConfig(config,"str2",tmp)
    def strButton3Click(self,event):
        tmp = self.string3.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str3",tmp)
    def strButton4Click(self,event):
        tmp = self.string4.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str4",tmp)
    def strButton5Click(self,event):
        tmp = self.string5.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str5",tmp)
    def strButton6Click(self,event):
        tmp = self.string6.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str6",tmp)
    def strButton7Click(self,event):
        tmp = self.string7.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str7",tmp)
    def strButton8Click(self,event):
        tmp = self.string8.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str8",tmp)
    def strButton9Click(self,event):
        tmp = self.string9.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"str9",tmp)
    def strButton10Click(self,event):
        tmp = self.string10.GetValue()
        self.Send_txt.SetValue(tmp)
        filestore.writeConfig(config,"strA",tmp)
    def openClick(self,event):
        dlg = wx.FileDialog(self, "打开",
                    os.getcwd(),
                    style = 0)
        if dlg.ShowModal() == (wx.ID_OK):
            self.filename = dlg.GetPath()
            print("Open file Ok:",self.filename)
            self.Statue_lab.SetLabel("已打开："+self.filename)
        dlg.Destroy()
    def clearClick(self,event):
        self.send_count = 0
        self.read_count = 0
        self.Send_num.SetLabel(str(self.send_count))
        self.Receive_num.SetLabel(str(self.read_count))



def main():
    #if __name__=='__main__':
    app = wx.App()
    FRAME = MyApp()
    FRAME.Save_but.SetLabel(wxT("保存"))
    FRAME.Show(True)
    app.MainLoop()

main()
