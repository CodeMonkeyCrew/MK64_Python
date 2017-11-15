from enum import Enum

class N64_KEYS(Enum):
     A = 293
     B = 292
     C_UP = 288 
     C_RIGHT = 289
     C_LEFT = 291
     C_DOWN = 290
     START = 297
     Z = 296
     L = 294
     R = 295
     JOYSTICK_X = 0 
     JOYSTICK_Y = 1
     CROSS_X = 16
     CROSS_Y = 17

# Init Serial
#serial_controller.open_serial_port(config['Serial']['Serial_Port'],config['Serial']['Baudrate'])