__author__ = 'Administrator'

import serial
from  serial.tools import list_ports

global mycom
class MyCom(object):
    def __init__(self, Port=None, BaudRate="9600", ByteSize="8", Parity = "N", Stopbits="1"):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.baudrate = BaudRate
        self.bytesize = int(ByteSize)
        self.parity = Parity
        self.stopbits = int(Stopbits)

    def start(self):
        print("start self.port=",self.port)
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = self.baudrate
        self.l_serial.bytesize = int(self.bytesize)
        self.l_serial.parity = self.parity
        self.l_serial.stopbits = int(self.stopbits)
        self.l_serial.timeout = 2
        self.l_serial.open()

        if self.l_serial.isOpen():
            self.alive = True
            return True
        else:
            return False

    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()
    def SetStopEvent(self):
        print(" self.waitEnd=",self.waitEnd)
        if not self.waitEnd is None:
            self.waitEnd.set()
            print("self.waitEnd.isSet()=",self.waitEnd.isSet())
        self.alive = False
        self.stop()

    def stop(self):
        self.alive = False
        if self.l_serial.isOpen():
            self.l_serial.close()


def reflash_port():
    comlist = []
    for com in list_ports.comports():
        strCom = com[0] + ": " + com[1][:-7]
        if com[0] == "COM1":
            strCom = com[0] + ": 通讯端口"
        #print("com[0]=",com[0])
        comlist.append(com[0])
    return comlist

def handle_baudrate(data):
    return data
def handle_bytesize(data):
    data = int(data)
    if data == 5:
        return serial.FIVEBITS
    elif data == 6:
        return serial.SIXBITS
    elif data == 7:
        return serial.SEVENBITS
    elif data == 8:
        return serial.EIGHTBITS
def handle_stopbits(data):
    data = int(data)
    if data == 1:
        return serial.STOPBITS_ONE
    elif data == 1.5:
        return serial.STOPBITS_ONE_POINT_FIVE
    elif data == 2:
        return serial.STOPBITS_TWO
def handle_parity(data):
    print("serial.PARITY_NONE=",serial.PARITY_NONE,data)
    if data == "None":
        return serial.PARITY_NONE
    elif data == "Even":
        return serial.PARITY_EVEN
    elif data == "Odd":
        return serial.PARITY_ODD
    elif data == "Mark":
        return serial.PARITY_MARK
    elif data == "Space":
        return serial.PARITY_SPACE

