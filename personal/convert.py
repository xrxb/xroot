import os

def convert(x):
    os.system("MP4Box -add "+x+" "+x+".mp4")
