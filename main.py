import pyautogui
import time
import ctypes

w,h = pyautogui.size()

prom = pyautogui.prompt(text="OKを押してマクロスタート")

if prom is None:
    quit()

handle = ctypes.windll.user32.FindWindowW("hspwnd0",None)

if handle != 0:
    ctypes.windll.user32.SetForegroundWindow(handle)
    pass

time.sleep(3)

keys = ["6"]*10

#pyautogui.typewrite(keys,interval=0.100)
#pyautogui.press(keys,pause=0.5)

for i in range(100):
    pyautogui.keyDown("u",pause=0.05)
    pyautogui.keyUp("u",pause=0.05)

