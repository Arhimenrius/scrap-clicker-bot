from src.video_stream import VideoStream
from src.mode.collect_magnet_cloud import CollectMagnetCloud
from src.mode.collect_steel import CollectSteel
from src.mode.merge import Merge
from src.mode.resolve_anti_macro import ResolveAntiMacro
import cv2
import time

test = 'default'


class ModeController:
    mode = 'default'
    portForStreaming = '5777'
    streamingUri = ''
    collectMagnetCloudMode = None
    collectSteelMode = None
    mergeMode = None
    resolveAntiMacroMode = None

    def __init__(self):
        self.streamingUri = 'tcp://127.0.0.1:' + self.portForStreaming
        self.collectMagnetCloudMode = CollectMagnetCloud()
        self.collectSteelMode = CollectSteel()
        self.mergeMode = Merge()
        self.resolveAntiMacroMode = ResolveAntiMacro()

    def control(self):
        video1 = VideoStream(self.portForStreaming)
        video1.start()
        time.sleep(1)
        camera = cv2.VideoCapture(self.streamingUri)
        while True:
            pass
            okay, frame = camera.read()
            if not okay:
                continue
            cv2.imshow('test', frame)
            cv2.waitKey(1)
            if self.resolveAntiMacroMode.is_mode_active(frame):
                self.resolveAntiMacroMode.process_mode()
            elif self.collectMagnetCloudMode.is_mode_active(frame):
                self.collectMagnetCloudMode.process_mode()
            elif self.collectSteelMode.is_mode_active(frame):
                self.collectSteelMode.process_mode()
            else:
                self.mergeMode.process_mode(frame)
