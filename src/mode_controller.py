from src.video_stream import VideoStream
from src.mode.magnet_cloud import CollectMagnetCloud
from src.mode.steel import CollectSteel
from src.mode.merge import Merge
from src.mode.anti_macro import DetectAntiMacro
from src.mode.anti_macro import ResolveAntiMacro
from src.mode.ad import is_mode_active as is_ad_active
import cv2
from time import sleep

test = 'default'


class ModeController:
    mode = 'default'
    portForStreaming = '5777'
    streamingUri = ''
    magnet_cloud_mode = None
    steel_mode = None
    mergeMode = None
    detect_anti_macro_mode = None

    number_of_frames_to_skip = 30
    skipped_frames = 0

    def __init__(self):
        self.streamingUri = 'tcp://127.0.0.1:' + self.portForStreaming
        self.magnet_cloud_mode = CollectMagnetCloud()
        self.steel_mode = CollectSteel()
        self.mergeMode = Merge()
        self.detect_anti_macro_mode = DetectAntiMacro()

    def control(self):
        stream = VideoStream(self.portForStreaming)
        stream.start()
        camera = cv2.VideoCapture(self.streamingUri)
        resolver = None

        while True:
            pass
            okay, frame = camera.read()
            if not okay:
                camera.release()
                cv2.destroyAllWindows()
                camera = cv2.VideoCapture(self.streamingUri)
                continue
            if self.detect_anti_macro_mode.is_mode_active(frame):
                if self.skipped_frames != self.number_of_frames_to_skip:
                    self.skipped_frames = self.skipped_frames + 1
                    continue
                else:
                    self.skipped_frames = 0
                    if resolver is None:
                        resolver = ResolveAntiMacro(frame)
                        resolver.start()
                    else:
                        if not resolver.isAlive():
                            resolver = None

            elif self.magnet_cloud_mode.is_mode_active(frame):
                self.magnet_cloud_mode.process_mode()
            elif self.steel_mode.is_mode_active(frame):
                self.steel_mode.process_mode()
            # elif is_ad_active(frame):
            #     pass
            else:
                if self.skipped_frames != self.number_of_frames_to_skip:
                    self.skipped_frames = self.skipped_frames + 1
                    continue
                # in other case, process it
                else:
                    self.skipped_frames = 0
                    self.mergeMode.process_mode(frame)
