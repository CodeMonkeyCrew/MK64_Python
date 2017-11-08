import input_controller
import serial_controller
import asyncio
import config_reader
import time
from player import Player

players = []
player = Player

# Read Settings
config = config_reader.read_config('../settings.ini')


# Create Players from settings
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

# Init Serial
serial_controller.open_serial_port(config['Serial']['Serial_Port'],config['Serial']['Baudrate'])

# Start
# Config Player
createPlayerFromConfig()

#get loop
loop = asyncio.get_event_loop()

for player in players:
    asyncio.ensure_future(input_controller.read_input_events(player,serial_controller.send_data()))
#start loop
loop.run_forever()
loop.close()