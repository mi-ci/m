from ctypes import *
import time
import random
import keyboard
import easyocr
from PIL import ImageGrab
import winsound
import requests
import json

def ka() :
    TOKEN = "6903985619:AAGZ0MCrq8JVwBiQ1gqB56qaIBxsJGRZJwI"
    chat_id = "6303269590"
    message = final
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
def now():
    for bbox, text, conf in result:
        if 19 <= bbox[2][1] - bbox[0][1] <= 51:
            for c in text :
                if ord('가') <= ord(c) <= ord('힣') :
                    winsound.Beep(330, 200)
                    ka()
                    break

dd_dll = windll.LoadLibrary('.\dd202x.8.x64.dll')

st = dd_dll.DD_btn(0) #classdd 초기설정

reader = easyocr.Reader(['ko', 'en'])

if st==1:
    print("OK")
else:
    print("Error")
    exit(101)
###########################################################
dd_dll.DD_mov(653, 881)
time.sleep(random.uniform(.1, .125))
dd_dll.DD_btn(1)
dd_dll.DD_btn(2)
time.sleep(random.uniform(1,1.1))
dd_dll.DD_mov(1106, 17)
while keyboard.is_pressed('i') == False:
    dd_dll.DD_key(705, 1)
    time.sleep(random.uniform(random.uniform(.065,0.085), random.uniform(.11,.22)))
    dd_dll.DD_key(705, 2)
    time.sleep(random.uniform(0.9,1.1))
    dd_dll.DD_key(709, 1)
    time.sleep(random.uniform(random.uniform(.065,0.085), random.uniform(.11,.22)))
    dd_dll.DD_key(709, 2)
    time.sleep(random.uniform(0.9,1.1))
    dd_dll.DD_key(708, 1)
    time.sleep(random.uniform(random.uniform(.065,0.085), random.uniform(.11,.22)))
    dd_dll.DD_key(708, 2)
    img = ImageGrab.grab(bbox=(50, 65, 800, 500))
    time.sleep(0.2)
    img.save('3.png')
    result = reader.readtext('3.png')
    str_list = [i[1] for i in result]
    final = ' '.join(str(s) for s in str_list)
    now()
    time.sleep(random.uniform(0.9,1.1))
    dd_dll.DD_key(707, 1)
    time.sleep(random.uniform(random.uniform(.065,0.085), random.uniform(.11,.22)))
    dd_dll.DD_key(707, 2)
    time.sleep(random.uniform(0.9,1.1))
    img = ImageGrab.grab(bbox=(50, 65, 800, 500))
    time.sleep(0.2)
    img.save('3.png')
    result = reader.readtext('3.png')
    str_list = [i[1] for i in result]
    final = ' '.join(str(s) for s in str_list)
    now()
    time.sleep(0.2)
    dd_dll.DD_key(709, 1)
    time.sleep(random.uniform(random.uniform(.065,0.085), random.uniform(.11,.22)))
    dd_dll.DD_key(709, 2)
    time.sleep(random.uniform(0.9,1.1))
    i = 0
    while i < 36:
        img = ImageGrab.grab(bbox=(50, 65, 800, 490))
        time.sleep(0.5)
        img.save('3.png')
        result = reader.readtext('3.png')
        str_list = [i[1] for i in result]
        final = ' '.join(str(s) for s in str_list)
        now()
        time.sleep(0.5)
        i = i + 1
    time.sleep(random.uniform(0.7,0.8))