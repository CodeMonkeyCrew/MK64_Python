#start serial
import serial, socket

#serial port
open_ser
#socket
TCP_IP = '127.0.0.1'
TCP_PORT = 54321
BUFFER_SIZE = 1024
MAX_NO_OF_PLAYERS = 1
clientList= []


#setup socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #AF_INET = IPv4
serverSocket.bind((TCP_IP, TCP_PORT))
serverSocket.listen(2) #allow up to 2 unaccepted connections
print ("Server started and waiting for players")

#open serial
def open_serial_port(port, rate):
    global open_ser
    open_ser =  serial.Serial(port, baudrate=rate)

def readlineCR():
    rv = ""
    while True:
        ch = open_ser.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv  

while len(clientList) < MAX_NO_OF_PLAYERS:
    conn, addr = serverSocket.accept()
    print ('Connection address:', addr)
    clientList.append(conn)
    conn.send(str(len(clientList)).encode())


#to receive: data = conn.recv(BUFFER_SIZE)

while 1:
    data = readlineCR()
    if data:
        print ("received data:", data)
        conn.send(data)  # echo back to client

conn.close()