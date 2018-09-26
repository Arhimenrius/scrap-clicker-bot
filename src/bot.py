#!/usr/bin/env python3
from src.video_stream import VideoStream
from src.mode_controller import ModeController


def play():
    # portToStream = '5777'
    # video1 = VideoStream(portToStream)
    mode_controller = ModeController()
    while True:
        mode_controller.control()
        # video1.keep_mobile_video_streaming_alive()
        pass
