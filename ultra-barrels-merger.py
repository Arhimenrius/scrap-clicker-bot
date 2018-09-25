#!/usr/bin/env python3

import subprocess
from time import sleep
#subprocess.run(["adb", "exec-out", "screenrecord", "--bit-rate=1m", "--output-format=h264", ",--size 640x480" "-", "|", "nc", "-t", "-l", "-p", "5777"])
#subprocess.Popen(["adb exec-out screenrecord --bit-rate=1m --output-format=h264 --size 640x480 - | nc -t -l -p 5777"])

def keepMobileVideoStreamingAlive():
	global video
	if(video == 0 or video.poll() != None):
		video = subprocess.Popen(["adb", "exec-out", "screenrecord", "--bit-rate=1m", "--output-format=h264", "--size=640x480", "-"], stdout=subprocess.PIPE, shell=False )
	subprocess.Popen(('nc -t -l -p 5777'), shell=True, stdin=video.stdout, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	pass

video = 0
output = 0
while True:
	keepMobileVideoStreamingAlive()
	pass