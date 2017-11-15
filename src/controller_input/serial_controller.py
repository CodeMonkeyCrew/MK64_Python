from serial import Serial
from message import createMessage
from command import Commands
import config_reader

ser = None
_port = 0
_rate = 0


config = config_reader.read_config('settings.ini')

def open_serial_port(port, rate):
    _port = config["Serial"]["Serial_Port"]
    _rate =  config["Serial"]["Baudrate"]
 

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