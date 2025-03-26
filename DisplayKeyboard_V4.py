import argparse
import time  # time manipulation
import uuid  # UIDs manipulation
import sys 
import pyautogui
# import LSL's Stream Info and Outlet classes, data and sampling rate types
from pylsl import StreamInfo, StreamOutlet, IRREGULAR_RATE, cf_double64
from pynput import keyboard as kb  # for capturing the keyboard events

def on_press(key):
    pressedKey = None
    try:
        pressedKey = key.name
    except:
        pressedKey = key
    if pressedKey=="esc":
        print(f"Key : {pressedKey}")
        print("Script terminated.")
        return False
    if pressedKey == "f2":
        print(f"Key Special_F2 : {pressedKey}")
        pyautogui.keyDown("win")
        time.sleep(0.01)
        pyautogui.keyDown("shift")
        time.sleep(0.01)
        pyautogui.keyDown("s")
        time.sleep(0.01)
        pyautogui.keyUp("win")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("s")
    else:
        print(f"Key : {pressedKey}")




if __name__ == "__main__":
    print ('START')
    
    press = on_press 

    with kb.Listener(on_press=press) as listener:
        listener.join()

    print(pyautogui.position())
    # pyautogui.mouseInfo()
    # pyautogui.displayMousePosition()
    print ('END')