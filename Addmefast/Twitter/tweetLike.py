import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    for i in range(2):
        pg.press('tab')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.typewrite('https://addmefast.com/free_points/twitter_likes')
pg.press('enter')
time.sleep(15)
press_button()

do_process()

altf4()
tweet_confirm()
carpi_kapat()