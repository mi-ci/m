from ctypes import *
import time
import random
import winsound
import pyautogui
import os

dd_dll = windll.LoadLibrary('.\dd202x.8.x64.dll')

st = dd_dll.DD_btn(0) #classdd 초기설정

if st==1:
    print("OK")
else:
    print("Error")
    exit(101)
###########################################################
def fl() :
    if pyautogui.locateOnScreen('rf.png', region=(0, 31, 1365, 769), confidence=0.8) != None:
        winsound.Beep(330, 200)
        os.system("pause")
        dd_dll.DD_mov(653, 881)
        time.sleep(random.uniform(.1, .125))
        dd_dll.DD_btn(1)
        dd_dll.DD_btn(2)
        time.sleep(5)
    if pyautogui.locateOnScreen('gf.png', region=(0, 31, 1365, 769), confidence=0.8) != None:
        winsound.Beep(330, 200)
        os.system("pause")
        dd_dll.DD_mov(653, 881)
        time.sleep(random.uniform(.1, .125))
        dd_dll.DD_btn(1)
        dd_dll.DD_btn(2)
        time.sleep(5)
    if pyautogui.locateOnScreen('pf.png', region=(0, 31, 1365, 769), confidence=0.8) != None:
        winsound.Beep(330, 200)
        os.system("pause")
        dd_dll.DD_mov(653, 881)
        time.sleep(random.uniform(.1, .125))
        dd_dll.DD_btn(1)
        dd_dll.DD_btn(2)
        time.sleep(5)
    if pyautogui.locateOnScreen('bg.png', region=(0, 31, 1365, 769), confidence=0.7) != None:
        winsound.Beep(330, 200)
        os.system("pause")
        dd_dll.DD_mov(653, 881)
        time.sleep(random.uniform(.1, .125))
        dd_dll.DD_btn(1)
        dd_dll.DD_btn(2)
        time.sleep(4.5)

def ra() :
    dd_dll.DD_key(712, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(712, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(712, 1)
    time.sleep(random.uniform(random.uniform(2.065, 2.085), random.uniform(2.11, 2.22)))
    dd_dll.DD_key(712, 2)
    time.sleep(random.uniform(random.uniform(2.065, 2.085), random.uniform(2.11, 2.22)))
    a=0
    b=0
    while a<7:
        dd_dll.DD_key(710, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(710, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        fl()
        a = a + 1
    while b < 6:
        dd_dll.DD_key(712, 1)
        time.sleep(random.uniform(random.uniform(.1, 0.11), random.uniform(.111, .12)))
        dd_dll.DD_key(712, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        b = b + 1
def st() :
        dd_dll.DD_key(711, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.13, .14)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(711, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))

        a = 0
        b = 0
        while a < 6:
            dd_dll.DD_key(710, 1)
            time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
            dd_dll.DD_key(600, 1)
            time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
            dd_dll.DD_key(600, 2)
            time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .12)))
            dd_dll.DD_key(710, 2)
            time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
            fl()
            a = a + 1

        dd_dll.DD_key(709, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 2)
        time.sleep(random.uniform(random.uniform(.085, 0.095), random.uniform(.11, .22)))
        dd_dll.DD_key(712, 1)
        time.sleep(random.uniform(0.59, 0.595))
        dd_dll.DD_key(712, 2)

        while b < 5:
            dd_dll.DD_key(712, 1)
            time.sleep(random.uniform(random.uniform(.109, 0.11), random.uniform(.12, .122)))
            dd_dll.DD_key(712, 2)
            time.sleep(random.uniform(random.uniform(.109, 0.11), random.uniform(.12, .122)))
            dd_dll.DD_key(709, 1)
            time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
            dd_dll.DD_key(709, 2)
            time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
            b = b + 1
def ti():
    a=0
    b=0
    while a<7:
        dd_dll.DD_key(710, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(710, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        fl()
        a = a + 1
    dd_dll.DD_key(712, 1)
    time.sleep(random.uniform(random.uniform(.265, 0.285), random.uniform(.381, .382)))
    dd_dll.DD_key(712, 2)

    while b < 4:
        dd_dll.DD_key(712, 1)
        time.sleep(random.uniform(random.uniform(.109, 0.11), random.uniform(.12, .122)))
        dd_dll.DD_key(712, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.0665), random.uniform(.0711, .0722)))
        dd_dll.DD_key(709, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        b = b + 1

def fo():
    a=0
    b=0
    while a<6:
        dd_dll.DD_key(710, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(710, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        fl()
        a = a + 1

    while b < 2:
        dd_dll.DD_key(712, 1)
        time.sleep(random.uniform(0.11, 0.12))
        dd_dll.DD_key(712, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        b = b + 1

def ro():
    dd_dll.DD_key(711, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(711, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    fl()
    dd_dll.DD_key(711, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(711, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))

    a=0
    b=0
    while a<5:
        dd_dll.DD_key(710, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(710, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        fl()
        a = a + 1

    while b < 2:
        dd_dll.DD_key(712, 1)
        time.sleep(random.uniform(random.uniform(.109, 0.11), random.uniform(.12, .122)))
        dd_dll.DD_key(712, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        b = b + 1

def do():
    dd_dll.DD_key(711, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(600, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(711, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    fl()

    a=0
    b=0
    while a<5:
        dd_dll.DD_key(710, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(710, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        fl()
        a = a + 1

    dd_dll.DD_key(712, 1)
    time.sleep(random.uniform(random.uniform(.965, 0.985), random.uniform(1.081, 1.082)))
    dd_dll.DD_key(712, 2)
    while b < 6:
        dd_dll.DD_key(712, 1)
        time.sleep(random.uniform(random.uniform(.109, 0.11), random.uniform(.12, .122)))
        dd_dll.DD_key(712, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(709, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        b = b + 1
def la():
    a=0
    while a<4:
        dd_dll.DD_key(710, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 1)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(600, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        dd_dll.DD_key(710, 2)
        time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
        fl()
        a = a + 1
    time.sleep(2)
    dd_dll.DD_key(502, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(502, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(712, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(712, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(313, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(313, 2)


def mo():
    dd_dll.DD_key(307, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(307, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(307, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(307, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_mov(random.randint(72, 102), random.randint(505, 535))
    time.sleep(random.uniform(.1, .125))
    dd_dll.DD_btn(1)
    dd_dll.DD_btn(2)
    time.sleep(3)
    dd_dll.DD_key(100, 1)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))
    dd_dll.DD_key(100, 2)
    time.sleep(random.uniform(random.uniform(.065, 0.085), random.uniform(.11, .22)))



##########################################################
time.sleep(2)

while 1==1 :
    ra()
    time.sleep(3)
    st()
    time.sleep(3)
    ti()
    time.sleep(3)
    fo()
    time.sleep(3)
    ro()
    time.sleep(3)
    do()
    time.sleep(3)
    la()
    time.sleep(7)
    mo()