from concurrent.futures import ThreadPoolExecutor
import concurrent.futures as confu
import time
from ocr_watcher import OCRWatcher
import pyautogui
import ctypes
from macro.macro_util import *
from macro.elona_harvest import main

def macro_test(watcher):
    pre_elona()
    from ctypes import cdll
    dll = cdll.LoadLibrary(r"C:\Users\spoon\App\elona_omake\ElonaExtenderHE\EExHE_Shared.dll")
    print(dll.GetHP())

if __name__ == "__main__":
    macro_main = main
    watcher = OCRWatcher()
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix="thread") as executor:
        try:
            future = executor.submit(watcher.watch)
            if check_exception(future) is True:
                future.result()
            #以降、watcher.ocr_resultで監視場所のOCR結果がわかるように

            macro_main(watcher)

        finally:
            watcher.stop()
            print("stop!")
    print("main end")

