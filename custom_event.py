"""
Control computer event by pyautogui

@author: Jacky Gao
@date: 2021.03.06
"""

import pyautogui
import threading
import time
import tkinter as tk
import tkinter.font as tkFont

global th_sta
th_sta = False


def writeText(textData):
    global th_sta
    time.sleep(2)
    print("Write")
    while th_sta:
        try:
            datalist = textData.split('\n')
            for data in datalist:
                key, runtime = data.split(' t=')
                print(key, runtime)
                pyautogui.press(key)
                time.sleep(float(runtime))
                if not th_sta:
                    print("break")
                    break
        except:
            th_sta = False
            print("Error")

def eventWrite():
    global th_sta
    if not th_sta:
        th_sta = True
        textData = TextArea.get("1.0","end-1c")  # 'end-1c' is delete '\n'
        th1 = threading.Thread(target=writeText, args=(textData, ))
        th1.setDaemon(True) # for app quit
        th1.start()
        print("Start th1")
        TextArea.config(state=tk.DISABLED)

def eventStop():
    global th_sta
    th_sta = False
    print("Stop th")
    TextArea.config(state=tk.NORMAL)

# basic setting
window = tk.Tk()
window.attributes('-topmost', True)
window.title('AutoApp')
window.geometry('400x400')
window.resizable(False, False)

frame = tk.Frame(window, width=90, height=400)
frame.pack(side=tk.RIGHT)

fontStyle = tkFont.Font(family='microsoft yahei', size=28, weight='bold')
fontStyle2 = tkFont.Font(family='microsoft yahei', size=16, weight='bold')

# add button
pixelVirtual = tk.PhotoImage(width=1, height=1)
b0 = tk.Button(frame, text='start', font=fontStyle2,
               image=pixelVirtual, height=60, width=80, compound="c",
               command=eventWrite)
b0.place(x=0, y=240)

b2 = tk.Button(frame, text='stop', font=fontStyle2,
               image=pixelVirtual, height=60, width=80, compound="c",
               command=eventStop)
b2.place(x=0, y=320)

# add custom script
TextArea = tk.Text(window, wrap="none", font=fontStyle)
ScrollBarX = tk.Scrollbar(window, orient=tk.HORIZONTAL)
ScrollBarY = tk.Scrollbar(window)
ScrollBarX.config(command=TextArea.xview)
ScrollBarY.config(command=TextArea.yview)
TextArea.config(xscrollcommand=ScrollBarX.set)
TextArea.config(yscrollcommand=ScrollBarY.set)
ScrollBarX.pack(side=tk.BOTTOM, fill=tk.X)
ScrollBarY.pack(side=tk.RIGHT, fill=tk.Y)
TextArea.pack(expand=tk.YES, fill=tk.BOTH)

# run GUI
window.mainloop()