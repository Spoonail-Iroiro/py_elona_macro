#手持ちの収穫の魔法書で願いの杖厳選するマクロ
import pyautogui
from macro.macro_util import *

def main(watcher):
    pre_elona()

    time.sleep(3)

    #魔法書切れ判定用
    fail_count = 0
    exit_flag = False
    while True:
        renda_sec("3",0.6)
        renda_sec("u",0.8)
        renda_sec("3",0.6)
        renda_sec("u",0.8)
        renda_sec("3",0.6)
        time.sleep(0.5)
        click_key_sleep("n",0.8)
        click_key_sleep("up",0.8)
        click_key_sleep("down",1.3)
        click_key_sleep("n",1.3)
        click_key_sleep("7",1.0)

        start = time.time()
        while (time.time() - start) < 89:
            click_key("6",interval=0.033)
            if ("そのまま" in watcher.ocr_result) or ("におちた" in watcher.ocr_result):
                print("Sleep")
                break
            if ("法はもう" in watcher.ocr_result) or ("使えない" in watcher.ocr_result):
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
                    print("[Stock is over]")
                    break
        if exit_flag is True:
            break
        time.sleep(2)
        click_key_sleep("n",0.8)
        click_key_sleep("up",0.8)
        click_key_sleep("down",1.3)
        click_key_sleep("f2",0.5)
        click_key_sleep("f2",0.5)
        click_key_sleep("y",1)
        click_key_sleep("f1",0.8)
        click_key_sleep("shift",0.5)
        click_key_sleep("shift",0.5)
        click_key_sleep("shift",0.5)
        click_key_sleep("f2",0.5)
        click_key_sleep("f2",0.5)
