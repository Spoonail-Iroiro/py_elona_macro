#手持ちの収穫の魔法書を読み切るマクロ
import pyautogui
from macro.macro_util import *

def main(watcher):
    pre_elona()

    time.sleep(3)

    #魔法書切れ判定用
    fail_count = 0
    exit_flag = False
    for i in range(2000):

        renda_sec("3",0.6)
        renda_sec("u",1.3)
        renda_sec("3",0.6)
        renda_sec("u",1.3)
        renda_sec("3",0.6)
        time.sleep(0.5)
        click_key("7")
        time.sleep(1)

        start = time.time()
        while (time.time() - start) < 70:
            click_key("6",interval=0.033)
            if ("法はもう" in watcher.ocr_result):
                if (time.time() - start) < 7:
                    if fail_count >= 3:
                        exit_flag = True
                        break
                    fail_count += 1
                    time.sleep(0.5)
                    click_key("f2")
                    time.sleep(0.5)
                    break
                else:
                    fail_count = 0
                    print("Book Expired")
                break
        if exit_flag is True:
            break
        time.sleep(0.5)
        click_key("f1")
        time.sleep(0.5)
        click_key("f1")
        time.sleep(0.5)
        click_key("n")
        time.sleep(0.5)
        click_key("F2")
