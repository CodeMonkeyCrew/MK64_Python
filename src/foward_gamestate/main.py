#start serial
import serial, socket, errno
import config_reader as reader
from socket import error as SocketError

#serial port
open_ser = serial
#client list
clientList= []
#read config
conf = reader.read_config("settings.ini")

#setup socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #AF_INET = IPv4
serverSocket.bind((conf['Server']['TCP_IP'], int(conf['Server']['TCP_PORT'])))
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
while True:
    while len(clientList) < int(conf['Server']['MAX_NO_OF_PLAYERS']):
        conn, addr = serverSocket.accept()
        print ('Connection address:', addr)
        clientList.append(conn)
        conn.send(str(len(clientList)).encode())


#to receive: data = conn.recv(BUFFER_SIZE)

    while 1:
        data = readlineCR()
        data = str("Hello").encode()
        if data:
            try:
                conn.send(data)  # echo back to client
            except SocketError as e:
                if e.errno != errno.ECONNRESET:
                    raise # Not error we are looking for
                pass # Handle error here.
    conn.close()
