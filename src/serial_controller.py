import serial

open_ser: serial

def open_serial_port(port, rate):
    global open_ser
    open_ser =  serial.Serial(port, baudrate=rate)

async def receive_data():
    while True: 
     rcv = readlineCR()
     print(rcv)

def send_data(data):
    open_ser.write(data) 

def readlineCR():
    rv = ""
    while True:
        ch = open_ser.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv