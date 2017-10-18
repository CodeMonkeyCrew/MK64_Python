from enum import Enum
'''
{
	('EV_MSC', 4L): [('MSC_SCAN', 4L)],
	('EV_KEY', 1L): 
		[
		(['BTN_JOYSTICK', 'BTN_TRIGGER'], 288L),
		('BTN_THUMB', 289L), ('BTN_THUMB2', 290L), 
		('BTN_TOP', 291L), 
		('BTN_TOP2', 292L), 
		('BTN_PINKIE', 293L), 
		('BTN_BASE', 294L), 
		('BTN_BASE2', 295L), 
		('BTN_BASE3', 296L), 
		('BTN_BASE4', 297L), 
		('BTN_BASE5', 298L), 
		('BTN_BASE6', 299L)
		], 
	('EV_ABS', 3L): 
		[
		(('ABS_X', 0L), AbsInfo(value=128, min=0, max=255, fuzz=0, flat=15, resolution=0)), 			(('ABS_Y', 1L), AbsInfo(value=128, min=0, max=255, fuzz=0, flat=15, resolution=0)), 			(('ABS_Z', 2L), AbsInfo(value=129, min=0, max=255, fuzz=0, flat=15, resolution=0)), 			(('ABS_RZ', 5L), AbsInfo(value=128, min=0, max=255, fuzz=0, flat=15, resolution=0)), 			(('ABS_HAT0X', 16L), AbsInfo(value=0, min=-1, max=1, fuzz=0, flat=0, resolution=0)), 			(('ABS_HAT0Y', 17L), AbsInfo(value=0, min=-1, max=1, fuzz=0, flat=0, resolution=0))
		], 
	('EV_SYN', 0L): [
		('SYN_REPORT', 0L), ('SYN_CONFIG', 1L), ('SYN_DROPPED', 3L), ('?', 4L)
		]
}
'''
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


def getButtonName(keyvalue):
    return N64_KEYS(keyvalue).name

def getStickNameAndValue(keyvalue, value):
    response = ""
    response = N64_KEYS(keyvalue).name
    if keyvalue == 1:
        if value < 120:
            return response + " UP: " + str(value)
        if value > 130:
            return response + " DOWN: " + str(value)
    elif keyvalue == 0:
        if value < 120:
            return response + " LEFT " + str(value)
        if value > 130:
            return response + " RIGHT " + str(value)
    elif keyvalue == 16:
        if value == 1:
            return response + " RIGHT"
        if value  < 0:
            return response + " LEFT"
    else:
        if value == 1:
            return response + " DOWN"
        if value  < 0:
            return response + " UP"


