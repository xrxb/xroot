import picamera
import time

from gpiozero import Button
button = Button(2)


dwell = 1
name = (time.strftime("%Y-%m-%d_%H.%M.%S", time.gmtime()))
with picamera.PiCamera() as picam:

    button.wait_for_press()
    

    #picam.resolution = (2592,1994)
    #Estos 3 parametros se pueden ajustar con la vista previa activada
    #picam.ISO=500
    #picam.shutter_speed=300000
    #picam.brightness+60
    print("Take photo in "+str(dwell)+"...")
    picam.resolution = (2592,1944)
        #(1920,1080)#HD
    picam.start_preview()
    time.sleep(dwell)
    picam.capture('IMG_'+name+'.jpeg')
    #picam.start_recording('video_'+name+'.mp4', resize=(640,480))
    #picam.image_effect = 'negative' #negative, solarize, gpen
    
    picam.stop_preview()
    picam.close()
