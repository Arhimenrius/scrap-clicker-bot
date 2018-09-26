import random
import threading


class ModeDetector(threading.Thread):
    mode = 'default'

    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        while True:
            randval = random.randint(1, 10)
            if randval < 3:
                ModeDetector.mode = 'steel'
            elif randval >= 3 and randval < 6:
                ModeDetector.mode = 'magnet_cloud'
            elif randval >= 6 and randval < 8:
                ModeDetector.mode = 'antymacro'
            else:
                ModeDetector.mode = 'default'

    def currentMode(self):
        return ModeDetector.mode
