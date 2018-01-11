import n64_controller_input_reader as input_controller
import asyncio
import config_reader
from player import Player
from socket import error as SocketError
import  socket, errno
import atexit
#defines
players = []
player = Player

# Read Settings
config = config_reader.read_config('settings.ini')

# Helper to create the number of players defined in the settings
def createPlayerFromConfig():
    curr_numb = 0
    for port in config['Controller']:
        global player
        input_port = config['Controller'][port]
        if input_port:
            player.number = curr_numb
            player.device = input_controller.init_input_device(input_port)
            players.append(player)
            curr_numb += 1



# Start
# create Player
createPlayerFromConfig()

#setup socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #AF_INET = IPv4
serverSocket.bind((config['Server']['TCP_IP'], int(config['Server']['TCP_Port'])))
serverSocket.listen(int(config['General']['Number_of_Players'])) #max is max number of players
print ("Server started and waiting for players")


#wait for all connections to be established
connectionnumber = 0
if config['General']['Enable_Sockets']:
    while connectionnumber < int(config['General']['Number_of_Players']):
            conn, addr = serverSocket.accept()
            print ('Connection address:', addr)
            players[connectionnumber].connection = conn
            conn.send(str(player.number).encode())
            connectionnumber +=1

try:
    #get loop
    loop = asyncio.get_event_loop()

    #start listening for each player
    for player in players:
        asyncio.ensure_future(input_controller.read_input_events(player))

    #start loop
    loop.run_forever()
except KeyboardInterrupt:
    print("W: interrupt received, stopping...")
finally:
    print("Close Server ..")
    serverSocket.close()
    #on interrupt shut down
    loop.close()
    print("Server Closed!")