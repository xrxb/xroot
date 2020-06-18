import os

def convert(x):
    os.system("MP4Box -add "+x+".h264 "+x+".mp4")
    print("OK")
