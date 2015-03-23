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

#configuration file
config = "conf.ini"
def wxT(x):
    return x

def bytes_str(b_str):
    c_str = ""
    for n in b_str:
        c_str += chr(n)
    return c_str

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
        self.TPsend_chk.SetValue(False)
        self.RN_chk.SetValue(False)
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

    def StartTimer(self,cb,interval):
        self.Bind(wx.EVT_TIMER,cb,self.timer)
        self.timer.Start(interval)

    def StopTimer(self):
        self.timer.Stop()
        #for k,v in self.timers.items():
        #    if v["cb"] == cb:
        #        v["t"].Stop()
        #        del self.timers[k]
        #        break
            #end if
        # #end for

    def reflash_port(self):
         list = device.reflash_port()
         if len(self.portlist) != len(list):
             self.portlist = list[:]
             self.Port_cmb.Clear()
             self.Port_cmb.Append(list)
             #self.frame.port.SetValue(list[0])
         #self.reflash_thread = threading.Thread(target=self.reflash_port)
         #self.reflash_thread.setDaemon(True)
         #self.reflash_thread.start()
    def PortDropdown(self,event):
        self.reflash_port()

    def Open_port(self,event):
         #print('func open_port event=',event)
         if self.Port_cmb.GetCurrentSelection() == -1:
             return 0
         openname = self.Port_but.GetLabel()
         try:
             if openname == wxT("打开串口"):
                 self.ser = device.MyCom(Port      =   self.Port_cmb.GetValue(),
                                         BaudRate  =   self.Baudrate_cmb.GetValue(),
                                         ByteSize  =   self.Bytesize_cmb.GetValue(),
                                         Parity    =   self.Parity_cmb.GetValue(),
                                         Stopbits  =   self.Stopbits_cmb.GetValue())
                 if self.ser.start():
                     self.ser.waitEnd = threading.Event()
                     tmp_flow = self.Flow_cmb.GetValue()
                     print("tmp_flow=",tmp_flow)
                     if tmp_flow == "HW":
                         self.ser.l_serial.rtscts = True
                         self.ser.l_serial.xonxoff = False
                     elif tmp_flow == "SW":
                         self.ser.l_serial.xonxoff = True
                         self.ser.l_serial.rtscts = False
                     elif tmp_flow == "OFF":
                         self.ser.l_serial.rtscts = False
                         self.ser.l_serial.xonxoff = False
                     #end if

                     #print("##########self.ser.l_serial=",self.ser.l_serial)
                     statue_name = self.ser.l_serial.port + wxT("已打开")
                     self.Statue_lab.SetLabel(statue_name)
                     self.Port_but.SetLabel(wxT("关闭串口"))
                     self.read_thread = threading.Thread(target=self.read)
                     self.read_thread.setDaemon(True)
                     self.read_thread.start()
                 else:
                     statue_name = self.ser.l_serial.port + wxT("打开失败")
                     self.Statue_lab.SetLabel(statue_name)
                     print("start fail")
                     self.ser.stop()
                 #end if
             else:
                 print("SetStopEvent")
                 self.Statue_lab.SetLabel(wxT("准备"))
                 self.ser.SetStopEvent()
                 self.read_thread.join()
                 self.Port_but.SetLabel(wxT("打开串口"))
                 print("close wenzi")
         except Exception as ex:
                 print("Exception")
                 statue_name = self.Port_cmb.GetValue() + wxT("打开失败")
                 self.Statue_lab.SetLabel(statue_name)
                 self.Port_but.SetLabel(wxT("关闭串口"))
         #end if

    def read(self):
             while self.ser.alive:
                 try:
                     n = self.ser.l_serial.inWaiting()
                     if n:
                         msg = self.ser.l_serial.read(n)
                         m = bytes_str(msg)
                         #print(msg)
                         m = self.Recv_txt.GetValue() + m
                         self.Recv_txt.SetValue(m)
                         self.Recv_txt.SetInsertionPointEnd()
                         self.read_count = self.read_count + n
                         self.Receive_num.SetLabel(str(self.read_count))
                     time.sleep(0.001)
                 except:
                     raise

             #end if
         #end while

    def write(self,send_data):
        if self.ser:
            send_data = bytearray(send_data,'utf-8')
            self.send_count = self.send_count + len(send_data)
            self.Send_num.SetLabel(str(self.send_count))
            self.ser.l_serial.write(send_data)
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

    def bt_send(self,event):
        send_type = isinstance(event,wx._core.CommandEvent)
        #print("event=",event,isinstance(event,wx._core.CommandEvent))
        send_data = self.Send_txt.GetValue()
        send_name = self.Send_but.GetLabel()
        print(send_name,send_type,not (send_name == wxT("暂停") and send_type == True))
        if self.Port_but.GetLabel() == wxT("关闭串口") and send_data != '' :
            if not (send_name == wxT("暂停") and send_type == True):
                if self.HEXsend_chk.GetValue() == True:
                    send_data = binascii.unhexlify(send_data).decode()
                #end if
                if self.RN_chk.GetValue() == True:
                    send_data = send_data + "\r\n"
                #end if

                tmp = self.Second_txt.GetValue()
                self.write(send_data)
                if (self.TPsend_chk.GetValue() == True) and (tmp != '') and (self.timer.IsRunning() == False) :
                     print("StartTimer")
                     self.Send_but.SetLabel(wxT("暂停"))
                     self.StartTimer(self.bt_send,int(tmp))
                #end if
            else:
                self.StopTimer()
                self.Send_but.SetLabel(wxT("发送"))
            #end if else
        #end if



    def bt_clrsend(self,event):
        self.Send_txt.SetValue("")
    def bt_clrrecv(self,event):
        self.Recv_txt.SetValue("")
    def bt_hexsend(self,event):
        #print("bt_hexsend event",event,self.HEXsend_chk.GetValue())
        if self.HEXsend_chk.GetValue() == True:
            tmp = self.Send_txt.GetValue()
            tmp = binascii.hexlify(tmp.encode()).decode()
            self.Send_txt.SetValue(tmp)
        else:
            tmp = self.Send_txt.GetValue()
            tmp = binascii.unhexlify(tmp).decode()
            self.Send_txt.SetValue(tmp)
        #end if
    def bt_hexrecv(self,event):
        #print("bt_hexsend event",event)
        if self.Hexrecv_chk.GetValue() == True:
            tmp = self.Recv_txt.GetValue()
            tmp = binascii.hexlify(tmp.encode()).decode()
            self.Recv_txt.SetValue(tmp)
        else:
            tmp = self.Recv_txt.GetValue()
            tmp = binascii.unhexlify(tmp).decode()
            self.Recv_txt.SetValue(tmp)
        #end if
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
