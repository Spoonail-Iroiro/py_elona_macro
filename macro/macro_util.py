import pyautogui
import time
import concurrent.futures as confu
import ctypes

def renda_sec(key, sec, interval=0.033):
    start = time.time()
    while True:
        if time.time() - start > sec:
            break
        pyautogui.keyDown(key,pause=interval)
        pyautogui.keyUp(key,pause=interval)

def click_key(key, interval=0.1):
    pyautogui.keyDown(key,pause=interval)
    pyautogui.keyUp(key,pause=interval)

def click_key_sleep(key, sleep, interval=0.1):
    pyautogui.keyDown(key,pause=interval)
    pyautogui.keyUp(key,pause=interval)
    time.sleep(sleep)

def check_exception(future):
    try:
        ex = future.exception(1)
        return True
    except confu.TimeoutError:
        return False
        pass

def pre_elona():
    prom = pyautogui.prompt(text="OKを押してマクロスタート")
    if prom is None:
        quit()

    handle = ctypes.windll.user32.FindWindowW("hspwnd0",None)
    if handle != 0:
        ctypes.windll.user32.SetForegroundWindow(handle)
        pass
    else:
        raise Exception("Elonaが起動されていません")


