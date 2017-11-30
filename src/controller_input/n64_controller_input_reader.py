from evdev import InputDevice, categorize, ecodes, KeyEvent
from n64_keymap import N64_KEYS
import asyncio, evdev
from message_creator import message_to_hex
from spi_controller import send_command_over_spi
from enum import Enum

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

async def read_input_events(player):
    async for event in player.device.async_read_loop(): 
        message = [0,0] 
        if event.type == ecodes.EV_KEY:
            message = detect_button(event)
        elif event.type == ecodes.EV_ABS:
            message =  detect_direction(event)
        if message:
           send_command_over_spi(message)