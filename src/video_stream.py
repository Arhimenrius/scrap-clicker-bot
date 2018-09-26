import subprocess


class VideoStream:
    video = 0
    server = 0
    port = None

    def __init__(self, port):
        self.port = port
        self.initialize_video()
        self.initialize_tcp_server()

    def keep_mobile_video_streaming_alive(self):
        if self.video == 0 or self.video.poll() is not None:
            self.initialize_video()
        if self.server == 0 or self.server.poll() is not None:
            self.initialize_tcp_server()

    def initialize_video(self):
        self.video = subprocess.Popen(
            ["adb", "exec-out", "screenrecord", "--bit-rate=1m", "--output-format=h264", "--size=640x480", "-"],
            stdout=subprocess.PIPE, shell=False
        )

    def initialize_tcp_server(self):
        self.server = subprocess.Popen(
            ('nc -l ' + self.port),
            shell=True,
            stdin=self.video.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
