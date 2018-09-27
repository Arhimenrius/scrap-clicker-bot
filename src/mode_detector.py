import random
import threading
from src.video_stream import VideoStream


class ModeDetector(threading.Thread):
    mode = 'default'
    portForStreaming = '5777'
    streamingUri = ''

    def __init__(self):
        self.streamingUri = 'tcp://127.0.0.1:' + self.portForStreaming
        threading.Thread.__init__(self)
        pass

    def run(self):
        video1 = VideoStream(self.portForStreaming)
        video1.start()
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
