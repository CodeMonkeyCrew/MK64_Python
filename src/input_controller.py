""" Reads the controller input and forward it """
from evdev import InputDevice, categorize, ecodes, KeyEvent
from n64_keymap import getButtonName, getStickNameAndValue
import asyncio, evdev

# TODO: Async Input from diffrent controller

def init_input_device(port):
    return evdev.InputDevice(port)


def start_listening(devices, forward_methode):
    while True:
        for device in devices:
            forward_event(device, forward_methode)



async def forward_event(device, forward_methode):
    while True:
        async for event in device.async_read_loop():
            if event.type == ecodes.EV_KEY:
                #print(getButtonName(event.code))
                forward_methode(getButtonName(event.code))
                return
            if event.type == ecodes.EV_ABS:
                if event.code != ecodes.ABS_Z:
                    forward_methode(getStickNameAndValue(event.code, event.value))
                    return
