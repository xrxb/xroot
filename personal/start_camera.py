import picamera
import time

camera = picamera.PiCamera()

##camera.rotation = 180
camera.start_preview()
time.sleep(15)
camera.stop_preview()
