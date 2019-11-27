from macro.macro_util import *

salesman_direction = "down"

def main(watcher):
    pre_elona()

    time.sleep(1)

    while True:
        for i in range(5):
            time.sleep(0.5)
            click_key_sleep(salesman_direction,0.3)
            renda_sec("space",2)
            renda_sec("shift",1)
            salesman_sleep_check = "がある" in watcher.ocr_result or "われる" in watcher.ocr_result or "合成" in watcher.ocr_result
            if salesman_sleep_check is True:
                renda_sec("u",2)
                continue
            for i in range(7):
                click_key_sleep("2",0.3)
                renda_sec("space",1)
                renda_sec("shift",0.3)
        else:
            renda_sec("3",0.5)

