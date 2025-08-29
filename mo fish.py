# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 15:30:29 2025

@author: thou
"""
import pyautogui
import time

print(pyautogui.position())


# Function to perform the clicking and key presses
def automate_actions():
    # Step 1: Click at a specific location (e.g., coordinates x=2453, y=385)
    pyautogui.moveTo(2453, 385)
    pyautogui.click(x=2453, y=385)
    time.sleep(1)  # Short delay before starting the loop
    
    for i in range(500):  # Repeat 50 times
        # Step 2: Press the space key 120 times
        for _ in range(120):
            pyautogui.press('space')
            time.sleep(0.1)  # Delay between key presses

        # Step 3: Press the enter key
        pyautogui.press('enter')
        time.sleep(0.5)  # Short delay between actions

# Execute the function
automate_actions()
 
 
 

 
 


 

 




























# Function to perform the clicking and key presses
def perform_actions():
    for i in range(5):  # Repeat 50 times
        # Step 1: Click at a specific location (e.g., coordinates x=100, y=100)
        pyautogui.click(x=2483, y=386)
        time.sleep(0.5)  # Short delay between actions
        
        # Step 2: Press the space key 30 times
        for _ in range(6):
            pyautogui.press('space')
            time.sleep(0.1)  # Delay between key presses

        # Step 3: Press the enter key
        pyautogui.press('enter')
        time.sleep(0.5)  # Short delay between actions

        # Step 4: Press the space key 30 times again
        for _ in range(6):
            pyautogui.press('space')
            time.sleep(0.1)  # Delay between key presses

# Execute the function
perform_actions()


    
      
        
          
          

