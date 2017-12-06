import n64_controller_input_reader as input_controller
import asyncio
import config_reader
from player import Player
from socket import error as SocketError
import  socket, errno
players = []
player = Player

# Read Settings
config = config_reader.read_config('settings.ini')

# Create Players from settingsmessage
def createPlayerFromConfig():
    curr_numb = 0
    for port in config['Controller']:
       # player = Player()
        global player
        input_port = config['Controller'][port]
        print(input_port)
        if input_port:
            player.number = curr_numb
            player.device = input_controller.init_input_device(input_port)
            players.append(player)
            curr_numb += 1



# Start
# Config Player
createPlayerFromConfig()

#setup socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #AF_INET = IPv4
serverSocket.bind((config['Server']['TCP_IP'], int(config['Server']['TCP_PORT'])))
serverSocket.listen(2) #allow up to 2 unaccepted connections
print ("Server started and waiting for players")

def dummyfill():
    for player in players:
        player.connection.send([0x40B2])

currplayer = 1
while len(clientList) < int(conf['General']['Number_of_Players']):
        conn, addr = serverSocket.accept()
        print ('Connection address:', addr)
        players[currplayer].connection = conn

#get loop
loop = asyncio.get_event_loop()

for player in players:
    asyncio.ensure_future(input_controller.read_input_events(player, dummyfills))

#start loop
loop.run_forever()
loop.close()