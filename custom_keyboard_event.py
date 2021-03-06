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


# def writeText():
#     global th_sta
#     i = 97
#     time.sleep(2)
#     print("Write")
#     while th_sta:
#         if i == 97+26:
#             pyautogui.press("return")
#             i = 97
#         else:
#             pyautogui.press(chr(i))
#             i += 1

# def getMousePos():
#     global th_sta
#     print("Track")
#     while th_sta:
#         x, y = pyautogui.position()
#         mouse_pos_str.set("x: {:04d} y: {:04d}".format(x, y))


def writeText(textData):
    global th_sta
    time.sleep(2)
    status_text.set(" Running")
    while th_sta:
        try:
            datalist = textData.split('\n')
            for data in datalist:
                key, runtime = data.split(' t=')
                print(key, runtime)
                pyautogui.press(key)
                time.sleep(float(runtime))
                if not th_sta:
                    break
        except:
            th_sta = False
            status_text.set(" Error")

def eventWrite():
    global th_sta
    if not th_sta:
        th_sta = True
        textData = TextArea.get("1.0","end-1c")  # 'end-1c' is delete '\n'
        th1 = threading.Thread(target=writeText, args=(textData, ))
        th1.setDaemon(True) # for app quit
        th1.start()
        status_text.set(" Start")
        TextArea.config(state=tk.DISABLED)

def eventStop():
    global th_sta
    th_sta = False
    status_text.set(" Stop")
    TextArea.config(state=tk.NORMAL)

# basic setting
window = tk.Tk()
window.attributes('-topmost', True)
window.title('AutoApp')
window.geometry('400x400')
window.resizable(False, False)

frame = tk.Frame(window, width=90, height=400)
frame.pack(side=tk.RIGHT)

pixelVirtual = tk.PhotoImage(width=1, height=1)

fontStyle = tkFont.Font(family='microsoft yahei', size=28, weight='bold')
fontStyle2 = tkFont.Font(family='microsoft yahei', size=16, weight='bold')
fontStyle3 = tkFont.Font(family='microsoft yahei', size=10, weight='bold')

l1 = tk.Label(frame, font=fontStyle2, text="Status:")
l1.place(x=0, y=0)

status_text = tk.StringVar()
status_text.set(" Preparing")
l2 = tk.Label(frame, font=fontStyle3, textvariable=status_text)
l2.place(x=0, y=30)

# add button
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