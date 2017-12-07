from evdev import InputDevice, categorize, ecodes, KeyEvent
from n64_keymap import N64_KEYS
import asyncio, evdev
from spi_controller import send_receive_over_spi
from enum import Enum
import time

class Commands(Enum):
    DIRECTION = 1
    ACCELERATE = 2
    THROTTLE = 3
    START = 4
    USE = 5
    NOC = 6

#create a new input device
def init_input_device(port):
    return evdev.InputDevice(port)

#create array for keycommand
def message_to_hex(keycode, keyvalue):
    return [keycode, keyvalue]


#dummy methode to test the sending over socket
def dummysend(player):
    input = 0x2206
    currentstate = []
    if currentstate != input:
        currentstate = input
        data = str(currentstate).encode()
        print(data)
        player.connection.send(data)
   
    
#create a message in hex for button events
def detect_button(event):
    tmp_command = 10
    keycode = event.code
    if(keycode == N64_KEYS.A.value):
        tmp_command = Commands.ACCELERATE
    elif(keycode == N64_KEYS.B.value):
        tmp_command = Commands.THROTTLE
    elif(keycode == N64_KEYS.START.value):
        tmp_command = Commands.START
    elif(keycode == N64_KEYS.Z.value):
        tmp_command = Commands.USE 
    if tmp_command.value <10:
        return message_to_hex(tmp_command.value, event.value)

#create a message in hex for a direction event
def detect_direction(event):
    if event.code != ecodes.ABS_Z:
        tmp_command = 0
        keycode = event.code
        #direction left right
        if keycode == 0:
            return message_to_hex(Commands.DIRECTION.value, event.value)



#read input events from controller
#send the last command over and over again
async def read_input_events(player):
    async for event in player.device.async_read_loop(): 
        #nothing happened already message
        message = message_to_hex(Commands.NOC, 0) 
        if event.type == ecodes.EV_KEY:
            message = detect_button(event)
        elif event.type == ecodes.EV_ABS:
            message =  detect_direction(event)
        print(message)
        if message:
           #send_receive_over_spi(player, message)
           dummysend(player)

