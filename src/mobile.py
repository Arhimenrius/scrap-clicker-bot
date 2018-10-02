from struct import pack
from sys import stdout
import random

# Event types
EV_SYN = 0x00
EV_KEY = 0x01
EV_REL = 0x02
EV_ABS = 0x03
EV_MSC = 0x04
EV_SW = 0x05
EV_LED = 0x11
EV_SND = 0x12
EV_REP = 0x14
EV_FF = 0x15
EV_PWR = 0x16
EV_FF_STATUS = 0x17

# Synchronization events.
SYN_REPORT = 0
SYN_CONFIG = 1
SYN_MT_REPORT = 2
SYN_DROPPED = 3

# Absolute
ABS_X = 0x00
ABS_Y = 0x01
ABS_Z = 0x02
ABS_RX = 0x03
ABS_RY = 0x04
ABS_RZ = 0x05
ABS_THROTTLE = 0x06
ABS_RUDDER = 0x07
ABS_WHEEL = 0x08
ABS_GAS = 0x09
ABS_BRAKE = 0x0a
ABS_HAT0X = 0x10
ABS_HAT0Y = 0x11
ABS_HAT1X = 0x12
ABS_HAT1Y = 0x13
ABS_HAT2X = 0x14
ABS_HAT2Y = 0x15
ABS_HAT3X = 0x16
ABS_HAT3Y = 0x17
ABS_PRESSURE = 0x18
ABS_DISTANCE = 0x19
ABS_TILT_X = 0x1a
ABS_TILT_Y = 0x1b
ABS_TOOL_WIDTH = 0x1c
ABS_VOLUME = 0x20
ABS_MISC = 0x28
ABS_MT_SLOT = 0x2f
ABS_MT_TOUCH_MAJOR = 0x30
ABS_MT_TOUCH_MINOR = 0x31
ABS_MT_WIDTH_MAJOR = 0x32
ABS_MT_WIDTH_MINOR = 0x33
ABS_MT_ORIENTATION = 0x34
ABS_MT_POSITION_X = 0x35
ABS_MT_POSITION_Y = 0x36
ABS_MT_TOOL_TYPE = 0x37
ABS_MT_BLOB_ID = 0x38
ABS_MT_TRACKING_ID = 0x39
ABS_MT_PRESSURE = 0x3a
ABS_MT_DISTANCE = 0x3b
ABS_MT_TOOL_X = 0x3c
ABS_MT_TOOL_Y = 0x3d

KEY_HOME = 102
BTN_TOOL_FINGER = 0x145
DOWN = 1
UP = 0

def packEvent(type, code, value):
    return pack('<IIHHi', 0, 0, type, code, value)
    pass

def outputEvent(type, code, value):
    stdout.buffer.write(packEvent(type, code, value))
    pass

def initTouch():
    outputEvent(EV_ABS, ABS_MT_SLOT, 0)
    outputEvent(EV_ABS, ABS_MT_TRACKING_ID, random.randint(1, 100000))

def clearTouch():
    outputEvent(EV_ABS, ABS_MT_TRACKING_ID, -1)
    outputEvent(EV_SYN, SYN_REPORT, 0)
    stdout.buffer.flush()

def actionDuringTouch(x, y):
    outputEvent(EV_ABS, ABS_MT_POSITION_X, x)
    outputEvent(EV_ABS, ABS_MT_POSITION_Y, y)
    outputEvent(EV_SYN, SYN_REPORT, 0)
    stdout.buffer.flush()
