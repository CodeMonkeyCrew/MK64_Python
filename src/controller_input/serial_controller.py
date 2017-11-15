from serial import Serial
from message import createMessage
from command import Commands
import config_reader


config = config_reader.read_config('settings.ini')
_port = config["Serial"]["Serial_Port"]
_rate =  config["Serial"]["Baudrate"]
ser = Serial(_port, _rate, timeout=1)
 

def send_data(message):
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