import argparse
import time  # time manipulation
import uuid  # UIDs manipulation
import sys 

# import LSL's Stream Info and Outlet classes, data and sampling rate types
from pylsl import StreamInfo, StreamOutlet, IRREGULAR_RATE, cf_double64
from pynput import keyboard as kb  # for capturing the keyboard events

def check_key(key):
    checked = None
    try:
        checked = key.char
    except AttributeError:
        # not a char, then remove Key. from e.g. Key.up
        checked = key
        checked = str(checked).split(".")[1]
    if checked != "esc":
        return checked
    else: 
        return False  # leave
    
def key_event_answer(key):
    if key:
        print(f"Key {action}: {key}")
    
    else:  # ESC pressed/released
        print(f"Key {action}: ESC")
        print("Script terminated.")
        return False

def on_press(key):
    # pressed = check_key(key)
    return key_event_answer(key)




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
    
    key_event = "press"
    action = f"{key_event}ed" if key_event == "press" else f"{key_event}d"
    press = on_press if key_event == "press" else None

    with kb.Listener(on_press=press) as listener:
        listener.join()

    print ('END')