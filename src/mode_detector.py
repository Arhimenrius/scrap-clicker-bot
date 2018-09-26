import random

mode = 'default'


class ModeDetector():
    def __init__(self):
        pass

    def detect(self):
        global mode
        print('xx')
        while True:
            randval = random.randint(1, 10)
            if randval < 3:
                mode = 'steel'
            elif randval >= 3 and randval < 6:
                mode = 'magnet_cloud'
            elif randval >= 6 and randval < 8:
                mode = 'antymacro'
            else:
                mode = 'default'

    def currentMode(self):
        global mode
        return mode
