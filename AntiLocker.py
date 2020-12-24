#!/usr/bin/env python
import pyautogui
import keyboard
from time import sleep, gmtime, strftime

screenWidth, screenHeight = pyautogui.size()            # Get the size of the primary monitor.
list_m = ['0','4','8','2','6']

def main():
    try:
        print("Script is running!")
        while True:
            currentMouseX, currentMouseY = pyautogui.position() # Get X&Y coords.
            pyautogui.moveTo(currentMouseX-1, currentMouseY)    # Move X - 1 pic
            newMouseX,newMouseY = pyautogui.position()

            if currentMouseX != newMouseX and currentMouseY != newMouseY: sleep(200)
            else: 
                pyautogui.moveTo(currentMouseX, currentMouseY)  # Move mouse back

                for minute in list_m:
                    if strftime("%M",gmtime())[1] == minute: 
                        keyboard.press('alt')
                        break
                sleep(200)
                
    except KeyboardInterrupt:
        pass 
        
if __name__ == '__main__':
    main()
