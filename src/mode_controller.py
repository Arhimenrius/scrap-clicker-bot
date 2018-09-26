from src.mode_detector import ModeDetector
import threading

test = 'default'


class ModeController():
    modes = []
    isDetectorUp = False

    def __init__(self):
        pass

    def control(self):
        detector = ModeDetector()
        if self.isDetectorUp == False:
            detector.start()
            self.isDetectorUp = True
        print(detector.currentMode())
