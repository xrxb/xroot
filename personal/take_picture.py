import picamera
import time

name = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
#print("About to take a picture in 5 seconds...")
#time.sleep(3)
with picamera.PiCamera() as camera:
    #camera.resolution = (1280,720)
    camera.capture("/home/pi/Desktop/" + name + ".jpg")
print("Picture taken.")
