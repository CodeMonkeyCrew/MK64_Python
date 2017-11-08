""" Reads the controller input and forward it """
from evdev import InputDevice, categorize, ecodes, KeyEvent
from n64_keymap import readButtonCommand, readCommandLeftOrRight
import asyncio, evdev

# TODO: Async Input from diffrent controller

player_devices = []

def init_input_device(port):
    return evdev.InputDevice(port)

async def read_input_events(player, forwardmethode):
    async for event in player.device.async_read_loop():
            if event.type == ecodes.EV_KEY:
                    readButtonCommand(event.code, player, forwardmethode)
            elif event.type == ecodes.EV_ABS:
                if event.code != ecodes.ABS_Z:
                    readCommandLeftOrRight(event.code, event.value,player, forwardmethode)
            
