import picamera
import time
name = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
with picamera.PiCamera() as picam:
    #picam.resolution = (2592,1994)
    picam.start_preview()
    picam.start_recording('video_'+name+'.h264', resize=(640,480))
    picam.image_effect = 'negative'
    picam.wait_recording(5)
    picam.stop_recording()
    picam.stop_preview()
    picam.close()
