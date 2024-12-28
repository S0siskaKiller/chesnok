# гайд как скачать чеснок

import os
import subprocess 
import webbrowser
import time 

print ("гайд как закачать чеснок на комп") 

webbrowser.get('firefox').open_new_tab('https://dvemorkovki.ru/upload/iblock/109/b679m89gzu9q4692lrgmobc23vizzl98/304232_5.jpg')
print ("скачка чеснока...") 
subprocess.Popen(
        ['mpv', 'ожидание.mp3'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
)
os.system ('curl -O https://i.imgur.com/zWphWZ6.png')
os.system ('mv zWphWZ6.png chesnoeb.png') 
os.system ('curl -O https://ia601209.us.archive.org/1/items/OMFGHello_20150908/OMFG%20-%20Hello.mp3')
os.system ('mv OMFG%20-%20Hello.mp3 music.mp3')
os.system ('killall mpv') 
os.system ('killall firefox') 
os.system ('mpv music.mp3 &') 
while True: 
    time.sleep(0.5)
    os.system('feh -F chesnoeb.png &') 
