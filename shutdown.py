from colorama import Fore, Back, Style
from pynput import keyboard
import time
import os

def prompt(text,color):
    print(getattr(Fore, color)+''+Style.RESET_ALL+getattr(Back, color)+text+Style.RESET_ALL+getattr(Fore, color)+''+Style.RESET_ALL+'\n')

prompt("Do you want to ⏻ shutdown your OS? (y/n)","MAGENTA")

with keyboard.Events() as events:
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('y'):
        prompt("⏻ Shutting down...","RED")
        time.sleep(0.5)
        os.system("shutdown /f /s /t 0")
    else:
        prompt(" Shutdown aborted","BLUE")
        time.sleep(0.5)