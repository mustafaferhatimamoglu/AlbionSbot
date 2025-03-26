import os
import sys
import time
import random
from pyautogui import *
import pyautogui
import keyboard
import numpy
import win32api, win32con

print ("start delay 2 sacond")
time.sleep(2)
while keyboard.is_pressed('F12') == False:
    if pyautogui.pixel(1000,200)[0] == 31:
        click(1000,200)
        print ("Clicked")
        time.sleep(2)

    print ("END")
    time.sleep(2)



def click(x,y):
    win32api.SetCursor(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
