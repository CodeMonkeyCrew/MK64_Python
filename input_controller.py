""" Reads the controller input and forward it """
from evdev import InputDevice, categorize, ecodes, KeyEvent
from zigbee import send_command
from n64_keymap import getButtonName, getStickNameAndValue
import asyncio, evdev

# TODO: Async Input from diffrent controller


def get_available_devices():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    return devices


def get_capabilities_for(device):
    return evdev.InputDevice(device).capabilities(verbose=True)


def start_listening(devices, forward_methode):
    for device in devices:
        asyncio.ensure_future(forward_event(device, forward_methode))
    loop = asyncio.get_event_loop()
    loop.run_forever()



async def forward_event(device, forward_methode):
    while True:
        async for event in device.async_read_loop():
            if event.type == ecodes.EV_KEY:
                #print(getButtonName(event.code))
                forward_methode(getButtonName(event.code))
            if event.type == ecodes.EV_ABS:
                if event.code != ecodes.ABS_Z:
                    forward_methode(getStickNameAndValue(event.code, event.value))
