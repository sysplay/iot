import snowboydecoder

def detected_callback():
	print "Hotword Detected"

print("Please say \"SysPlay\" to activate me.")
detector = snowboydecoder.HotwordDetector("sysplay.pmdl", sensitivity=0.6, audio_gain=1)
detector.start(detected_callback)
