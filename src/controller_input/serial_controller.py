import serial

open_ser: serial

def open_serial_port(port, rate):
    global open_ser
    open_ser =  serial.Serial(port, baudrate=rate)

def send_data(command, value):
    open_ser.write(command + ':' + value) 
    #print(data)

#def readlineCR():
#    rv = ""
#    while True:
#        ch = open_ser.read()
#        rv += ch
#        if ch == '\r' or ch == '':
#            return rv