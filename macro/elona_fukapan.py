from macro.macro_util import *

def main(watcher):
    #金貨がある位置のアルファベット
    coin_alpha = "g"

    pre_elona()
    for i in range(30):
        time.sleep(1)
        click_key_sleep("2",1.0)
        click_key_sleep("i",1.0)
        click_key_sleep("left",0.5)
        click_key_sleep(coin_alpha,0.8)
        click_key_sleep("left",0.3)
        click_key_sleep("a",0.5)
        time.sleep(1.5)
        renda_sec("3",0.4)


