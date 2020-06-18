import picamera
import time
from convert import convert
from gpiozero import Button
button = Button(2)

time_to_record = 2
name = (time.strftime("%Y-%m-%d_%H.%M.%S", time.gmtime()))+"_"+str(time_to_record)+"s"
with picamera.PiCamera() as picam:
    button.wait_for_press()
    print("Recording for "+str(time_to_record)+" seconds...")
    #picam.resolution = (2592,1994)

    #Estos 3 parametros se pueden ajustar con la vista previa activada
    #picam.ISO=500
    #picam.shutter_speed=300000
    #picam.brightness+60
    
    picam.start_preview()
    picam.start_recording('video_'+name+'.h264')
    #picam.start_recording('video_'+name+'.mp4', resize=(640,480))
    #picam.image_effect = 'negative' #negative, solarize, gpen
    picam.wait_recording(time_to_record)
    picam.stop_recording()
    picam.stop_preview()
    picam.close()
    convert(name)
