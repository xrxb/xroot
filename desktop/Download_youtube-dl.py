from __future__ import unicode_literals
import youtube_dl

a = input('Introduce la URL del video:\n')

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   ydl.download([a]) #ydl.download(['https://youtu.be/1RjkOWLrg3U'])
