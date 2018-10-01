from src.video_stream import VideoStream
from src.mode.collect_magnet_cloud import CollectMagnetCloud
from src.mode.collect_steel import CollectSteel
from src.mode.merge import Merge
from src.mode.resolve_anti_macro import ResolveAntiMacro
import cv2
import time
import logging

test = 'default'


class ModeController:
    mode = 'default'
    portForStreaming = '5777'
    streamingUri = ''
    collectMagnetCloudMode = None
    collectSteelMode = None
    mergeMode = None
    resolveAntiMacroMode = None

    number_of_frames_to_skip_for_merge = 30
    skipped_frames_for_merge = 0
    number_of_frames_to_skip_after_anti_macro = 120
    skipped_frames_after_anti_macro = 0

    def __init__(self):
        self.streamingUri = 'tcp://127.0.0.1:' + self.portForStreaming
        self.collectMagnetCloudMode = CollectMagnetCloud()
        self.collectSteelMode = CollectSteel()
        self.mergeMode = Merge()
        self.resolveAntiMacroMode = ResolveAntiMacro()

    def control(self):
        stream = VideoStream(self.portForStreaming)
        stream.start()
        time.sleep(1)
        camera = cv2.VideoCapture(self.streamingUri)
        anti_macro_resolved = False

        while True:
            pass
            okay, frame = camera.read()
            if not okay:
                camera.release()
                cv2.destroyAllWindows()
                camera = cv2.VideoCapture(self.streamingUri)
                continue
            cv2.imshow('test', frame)
            cv2.waitKey(1)
            if anti_macro_resolved:
                if self.skipped_frames_after_anti_macro < self.number_of_frames_to_skip_after_anti_macro:
                    self.skipped_frames_after_anti_macro = self.skipped_frames_after_anti_macro + 1
                    continue
                else:
                    self.skipped_frames_after_anti_macro = 0
                    anti_macro_resolved = False

            if self.resolveAntiMacroMode.is_mode_active(frame):
                self.resolveAntiMacroMode.process_mode(frame)
                anti_macro_resolved = True
            elif self.collectMagnetCloudMode.is_mode_active(frame):
                self.collectMagnetCloudMode.process_mode()
            elif self.collectSteelMode.is_mode_active(frame):
                self.collectSteelMode.process_mode()
            else:
                if self.skipped_frames_for_merge != self.number_of_frames_to_skip_for_merge:
                    self.skipped_frames_for_merge = self.skipped_frames_for_merge + 1
                    continue
                # in other case, process it
                else:
                    self.skipped_frames_for_merge = 0
                    self.mergeMode.process_mode(frame)
