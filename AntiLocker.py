#!/usr/bin/env python
import pyautogui
import keyboard
from time import sleep, gmtime, strftime

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
list_m = ['0','4','8','2','6']

while True:
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(currentMouseX-1, currentMouseY)
    newMouseX,newMouseY = pyautogui.position()
    
    if currentMouseX != newMouseX and currentMouseY != newMouseY:sleep(200)
    else: 
        pyautogui.moveTo(currentMouseX, currentMouseY)
        for minute in list_m:
            if keyboard.read_key(): break
            if strftime("%M",gmtime())[1] == minute: 
                keyboard.press('alt')
                break
        sleep(200)
