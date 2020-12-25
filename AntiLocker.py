#!/usr/bin/env python
import pyautogui
import keyboard
from time import sleep, gmtime, strftime

screenWidth, screenHeight = pyautogui.size()            # Get the size of the primary monitor.
list_m = ['0','4','8','2','6']

def pressed_keys(e):sleep(100);keyboard.unhook(pressed_keys)

def main():
    try:
        print("Script is running!")
        while True:
            currentMouseX, currentMouseY = pyautogui.position() # Get X&Y coords.
            keyboard.hook(pressed_keys)                         # If key is down sleep 
            newMouseX,newMouseY = pyautogui.position()          # Get new X&Y coords.
            if currentMouseX != newMouseX and currentMouseY != newMouseY:sleep(60)
            else:[keyboard.press_and_release('alt') for minute in list_m if strftime("%M",gmtime())[1] == minute];sleep(100)
                
    except KeyboardInterrupt:
        pass 
        
if __name__ == '__main__':
    main()
