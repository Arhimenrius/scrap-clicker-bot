#!/usr/bin/env python3

from src.video_stream import VideoStream

portToStream = '5777'
video1 = VideoStream(portToStream)
# video2 = VideoStream('5778')

while True:
    video1.keep_mobile_video_streaming_alive()
    # video2.keep_mobile_video_streaming_alive()
    pass
