from ctypes import *
import time
from pyautogui import *
import pyautogui
import random
import winsound
mouseleftdown = 1
mouseleftup = 2
mouserightdown = 4
mouserightup = 8
mousewheeldown = 16
mousewheelup = 32

dd_dll = windll.LoadLibrary('.\dd202x.8.x64.dll')

st = dd_dll.DD_btn(0) #classdd 초기설정

if st==1:
    print("OK")
else:
    print("Error")
    exit(101)
###########################################################
time.sleep(2)
i=0
j=0
k=0
while 1==1 :
    i=0
    j=0
    k=0
    z=0
    e=0
    h=0
    if pyautogui.locateOnScreen('lla.png', region=(600, 450, 300, 250), confidence=0.4) != None:
        winsound.Beep(440, 10000)
    while i < 5:
        i=i+1
        dd_dll.DD_key(712, 1)
        dd_dll.DD_key(500, 1)
        time.sleep(0.1)
        dd_dll.DD_key(500, 2)
        dd_dll.DD_key(712, 2)
        e=0
        while e<6 :
            e=e+1

            if pyautogui.locateOnScreen('1sml.png', region=(770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1sml.png', region=(240,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1smr.png', region = (770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1smr.png', region = (240,530,500,130), confidence = 0.4) != None :
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wml.png', region=(770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wml.png', region=(240,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wmr.png', region = (770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wmr.png', region = (240,530,500,130), confidence = 0.4) != None :
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.pixel(502,840)[2] > 100:
                dd_dll.DD_key(703, 1)
                time.sleep(0.5)
                dd_dll.DD_key(703, 2)

    while z < 5:
        z=z+1
        dd_dll.DD_key(710, 1)
        dd_dll.DD_key(500, 1)
        time.sleep(0.1)
        dd_dll.DD_key(500, 2)
        dd_dll.DD_key(710, 2)
        h=0
        while h<6 :
            h=h+1

            if pyautogui.locateOnScreen('1sml.png', region=(770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1sml.png', region=(240,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1smr.png', region = (770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1smr.png', region = (240,530,500,130), confidence = 0.4) != None :
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wml.png', region=(770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wml.png', region=(240,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wmr.png', region = (770,530,500,130), confidence = 0.4) != None:
                dd_dll.DD_key(712, 1)
                time.sleep(0.3)
                dd_dll.DD_key(712, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.locateOnScreen('1wmr.png', region = (240,530,500,130), confidence = 0.4) != None :
                dd_dll.DD_key(710, 1)
                time.sleep(0.3)
                dd_dll.DD_key(710, 2)
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
                time.sleep(0.1)

            if pyautogui.pixel(502,840)[2] > 100:
                dd_dll.DD_key(703, 1)
                time.sleep(0.5)
                dd_dll.DD_key(703, 2)

    while 1==1:
        v = pyautogui.locateOnScreen('center.png', region = (44,120,145,80), confidence=0.55)
        a = pyautogui.center(v)
        if a[0] <106:
            dd_dll.DD_key(712, 1)
            time.sleep(0.2)
            dd_dll.DD_key(712, 2)
            time.sleep(0.1)
        elif a[0] > 106 :
            dd_dll.DD_key(710, 1)
            time.sleep(0.2)
            dd_dll.DD_key(710, 2)
            time.sleep(0.1)
        else :
            dd_dll.DD_key(709, 1)
            dd_dll.DD_key(602, 1)
            time.sleep(0.5)
            dd_dll.DD_key(602, 2)
            dd_dll.DD_key(709, 2)
            dd_dll.DD_key(709, 1)
            dd_dll.DD_key(602, 1)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(602, 2)
            time.sleep(1.1)
            dd_dll.DD_key(709, 2)
            dd_dll.DD_key(712, 1)
            dd_dll.DD_key(500, 1)
            time.sleep(0.1)
            dd_dll.DD_key(500, 2)
            dd_dll.DD_key(712, 2)
            if pyautogui.locateOnScreen('lla.png', region=(600, 450, 300, 250), confidence=0.4) != None:
                winsound.Beep(440, 10000)
            break

    ###########################################################

    while j < 8:
        j=j+1

        if pyautogui.locateOnScreen('sml.png', region=(680,400,500,170), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('sml.png', region=(180,400,500,170), confidence = 0.5) != None:
            dd_dll.DD_key(710, 1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('smr.png', region = (680,400,500,170), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('smr.png', region = (180,400,500,170), confidence = 0.5) != None :
            dd_dll.DD_key(710, 1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wml.png', region=(680,400,500,170), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wml.png', region=(180,400,500,170), confidence = 0.5) != None:
            dd_dll.DD_key(710, 1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wmr.png', region = (680,400,500,170), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wmr.png', region = (180,400,500,170), confidence = 0.5) != None :
            dd_dll.DD_key(710, 1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.pixel(502,840)[2] > 100:
            dd_dll.DD_key(703, 1)
            time.sleep(0.5)
            dd_dll.DD_key(703, 2)

    dd_dll.DD_key(712, 1)
    dd_dll.DD_key(500, 1)
    time.sleep(0.1)
    dd_dll.DD_key(500, 2)
    dd_dll.DD_key(712, 2)
    time.sleep(0.5)
    dd_dll.DD_key(712, 1)
    dd_dll.DD_key(500, 1)
    time.sleep(0.1)
    dd_dll.DD_key(500, 2)
    dd_dll.DD_key(712, 2)
    time.sleep(0.5)
    dd_dll.DD_key(710, 1)
    dd_dll.DD_key(500, 1)
    time.sleep(0.1)
    dd_dll.DD_key(500, 2)
    dd_dll.DD_key(710, 2)
    time.sleep(0.5)
    dd_dll.DD_key(710, 1)
    dd_dll.DD_key(500, 1)
    time.sleep(0.1)
    dd_dll.DD_key(500, 2)
    dd_dll.DD_key(710, 2)

    while 1==1:
        v = pyautogui.locateOnScreen('center.png', region = (64,120,125,80), confidence=0.6)
        a = pyautogui.center(v)
        if a[0] > 106 :
            dd_dll.DD_key(710, 1)
            dd_dll.DD_key(710, 2)
            if pyautogui.locateOnScreen('sml.png', region=(180, 400, 500, 170), confidence=0.5) != None:
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
            if pyautogui.locateOnScreen('smr.png', region=(180, 400, 500, 170), confidence=0.5) != None:
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
            if pyautogui.locateOnScreen('wml.png', region=(180, 400, 500, 170), confidence=0.5) != None:
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)
            if pyautogui.locateOnScreen('wmr.png', region=(180, 400, 500, 170), confidence=0.5) != None:
                dd_dll.DD_key(600, 1)
                time.sleep(0.5)
                dd_dll.DD_key(600, 2)                
            dd_dll.DD_key(710, 1)
            time.sleep(0.2)
            dd_dll.DD_key(710, 2)
        else :
            dd_dll.DD_key(709, 1)
            dd_dll.DD_key(602, 1)
            time.sleep(1)
            dd_dll.DD_key(602, 2)
            dd_dll.DD_key(709, 2)
            dd_dll.DD_key(709, 1)
            dd_dll.DD_key(602, 1)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(710, 1)
            time.sleep(0.1)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(712, 1)
            time.sleep(0.1)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(602, 2)
            time.sleep(2)
            dd_dll.DD_key(709, 2)
            dd_dll.DD_key(712, 1)
            dd_dll.DD_key(500, 1)
            time.sleep(0.1)
            dd_dll.DD_key(500, 2)
            dd_dll.DD_key(712, 2)
            break


    ###########################################################

    while k < 15:
        k=k+1

        if pyautogui.locateOnScreen('sml.png', region=(680,400,500,260), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.4)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('sml.png', region=(180,400,500,260), confidence = 0.5) != None:
            dd_dll.DD_key(710, 1)
            time.sleep(0.4)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('smr.png', region = (680,400,500,260), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.4)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('smr.png', region = (180,400,500,260), confidence = 0.5) != None :
            dd_dll.DD_key(710, 1)
            time.sleep(0.4)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wml.png', region=(680,400,500,260), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.4)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wml.png', region=(180,400,500,260), confidence = 0.5) != None:
            dd_dll.DD_key(710, 1)
            time.sleep(0.4)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wmr.png', region = (680,400,500,260), confidence = 0.5) != None:
            dd_dll.DD_key(712, 1)
            time.sleep(0.4)
            dd_dll.DD_key(712, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.locateOnScreen('wmr.png', region = (180,400,500,260), confidence = 0.5) != None :
            dd_dll.DD_key(710, 1)
            time.sleep(0.4)
            dd_dll.DD_key(710, 2)
            dd_dll.DD_key(600, 1)
            time.sleep(0.5)
            dd_dll.DD_key(600, 2)
            time.sleep(0.1)

        if pyautogui.pixel(502,840)[2] > 100:
            dd_dll.DD_key(703, 1)
            time.sleep(0.5)
            dd_dll.DD_key(703, 2)

    while 1==1:
        v = pyautogui.locateOnScreen('center.png', region = (64,120,125,80), confidence=0.6)
        a = pyautogui.center(v)
        if a[0] >100:
            dd_dll.DD_key(710, 1)
            dd_dll.DD_key(500, 1)
            time.sleep(0.1)
            dd_dll.DD_key(500, 2)
            dd_dll.DD_key(710, 2)
        if a[0] <90:
            dd_dll.DD_key(712, 1)
            time.sleep(0.2)
            dd_dll.DD_key(712, 2)
            time.sleep(0.1)
        if a[0] > 90 :
            dd_dll.DD_key(710, 1)
            time.sleep(0.5)
            dd_dll.DD_key(710, 2)
            time.sleep(0.1)
        else :
            dd_dll.DD_key(711, 1)
            dd_dll.DD_key(602, 1)
            time.sleep(0.1)
            dd_dll.DD_key(602, 2)
            dd_dll.DD_key(711, 2)
            time.sleep(2.9)
            break