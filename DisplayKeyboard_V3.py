import argparse
import time  # time manipulation
import uuid  # UIDs manipulation
import sys 
import pyautogui
# import LSL's Stream Info and Outlet classes, data and sampling rate types
from pylsl import StreamInfo, StreamOutlet, IRREGULAR_RATE, cf_double64
from pynput import keyboard as kb  # for capturing the keyboard events

def on_press(key):
    print(f"Key : {key}")




if __name__ == "__main__":
    print ('START')
    UID = str(uuid.uuid4())
    info = StreamInfo(
        name = 'name',
        type="Markers",  # stream type
        channel_count=2,  # number of values to stream
        nominal_srate=IRREGULAR_RATE,  # sampling rate in Hz or IRREGULAR_RATE
        channel_format=cf_double64,  # data type sent (dobule, float, int, str)
        source_id=UID,  # unique identifier
    )    
    # event selected als variable
    outlet = StreamOutlet(info)
    
    press = on_press 

    with kb.Listener(on_press=press) as listener:
        listener.join()

    pyautogui.displayMousePosition()
    print ('END')