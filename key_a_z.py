"""
Control computer event by pyautogui
* typing a - z
* tracking mouse

@author: Jacky Gao
@date: 2021.03.06
"""

import pyautogui
import threading
import tkinter as tk
import time

global th1_sta, th2_sta
th1_sta = False
th2_sta = False


def writeText():
    global th1_sta
    i = 97
    time.sleep(2)
    print("Write")
    while th1_sta:
        if i == 97+26:
            pyautogui.press("return")
            i = 97
        else:
            pyautogui.press(chr(i))
            i += 1

def getMousePos():
    global th2_sta
    print("Track")
    while th2_sta:
        x, y = pyautogui.position()
        mouse_pos_str.set("x: {:04d} y: {:04d}".format(x, y))
          
def eventWrite():
    global th1_sta
    if not th1_sta:
        th1_sta = True
        th1 = threading.Thread(target=writeText)
        th1.setDaemon(True) # 守護執行緒
        th1.start()
        print("Start th1")
          
def eventTrack():
    global th2_sta
    if not th2_sta:
        th2_sta = True
        th2 = threading.Thread(target=getMousePos)
        th2.setDaemon(True) # 守護執行緒
        th2.start()
        print("Start th2")

def eventStop():
    global th1_sta, th2_sta
    th1_sta = False
    th2_sta = False
    print("Stop th1 th2")

# basic setting
window = tk.Tk()
window.attributes('-topmost', True)
window.title('AutoApp')
window.geometry('250x25')

frame = tk.Frame(window, width=220, height=25)
frame.pack()

# check mouse position
mouse_pos_str = tk.StringVar()
mouse_pos_str.set("x: 0000 y: 0000")

label = tk.Label(frame, textvariable=mouse_pos_str)
label.place(x=120, y=0)

# add button
bn0 = tk.Button(frame, text='a-z', command=eventWrite)
bn0.place(x=0, y=0)

bn1 = tk.Button(frame, text='track', command=eventTrack)
bn1.place(x=30, y=0)

bn2 = tk.Button(frame, text='stop', command=eventStop)
bn2.place(x=70, y=0)

# run GUI
window.mainloop()