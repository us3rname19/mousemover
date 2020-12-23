#!/usr/bin/env python
import pyautogui
from time import sleep

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

while True:
	
	currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
	pyautogui.moveTo(currentMouseX-5, currentMouseY) 
	sleep(1)
	newMouseX, newMouseY = pyautogui.position() # Get the XY position of the mouse.
	if currentMouseX != newMouseX and currentMouseY != newMouseY:continue
	else: pyautogui.moveTo(currentMouseX, currentMouseY) 
	sleep(10)
