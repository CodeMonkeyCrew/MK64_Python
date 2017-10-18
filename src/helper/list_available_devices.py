from evdev import InputDevice, categorize, ecodes, KeyEvent
import evdev

def get_available_devices():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    return devices

print('Avaible Input Devices:')
print(get_available_devices())