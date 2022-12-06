import sys
import os
from pynput.mouse import Listener
from playsound import playsound


try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = sys._MEIPASS
    fart_noise_path = os.path.join(base_path, "sounds/fart.mp3")
except Exception:
    base_path = os.path.abspath(".")
    fart_noise_path = os.path.join(base_path, "click_to_fart/sounds/fart.mp3")



def on_click(x, y, button, pressed):
    playsound(fart_noise_path, block=False)


with Listener(on_click=on_click) as listener:
    listener.join()