from serial import Serial
from message import createMessage
from command import Commands
ser = None
_port = 0
_rate = 0

def open_serial_port(port, rate):
   global _port
   _port = port
   global rate
   _rate = rate

def send_data(message):
    print(_port)
    print(_rate)
    if(ser.isOpen() == False):
        ser.open()
    ser.flushInput()
    ser.flushOutput()
    ser.write(message) 

#def readlineCR():
#    rv = ""
#    while True:
#        ch = open_ser.read()
#        rv += ch
#        if ch == '\r' or ch == '':
#            return rv