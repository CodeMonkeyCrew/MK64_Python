import input_controller
import asyncio
import config_reader
from player import Player
from serial_controller import open_serial_port


players = []
player = Player

# Read Settings
config = config_reader.read_config('settings.ini')

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



# Start
# Config Player
createPlayerFromConfig()

#get loop
loop = asyncio.get_event_loop()

for player in players:
    asyncio.ensure_future(input_controller.read_input_events(player))

#start loop
loop.run_forever()
loop.close()