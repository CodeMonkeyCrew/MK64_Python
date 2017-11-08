from serial import Serial
 
#Starting serial connection
serialPort = Serial
#Check if port failed to open
if (serialPort.isOpen() == False):
        serialPort.open()
 
#Flush before receiving or sending any data



def open_serial_port(port, rate):
    global serialPort
    serialPort =  Serial(port, baudrate=rate)
    serialPort.flushInput()
    serialPort.flushOutput()

def send_data(command, value):
    serialPort.write(command + ':' + value) 
    #print(data)

#def readlineCR():
#    rv = ""
#    while True:
#        ch = open_ser.read()
#        rv += ch
#        if ch == '\r' or ch == '':
#            return rv