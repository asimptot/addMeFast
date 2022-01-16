import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.click(131, 131)
    time.sleep(2)
    pg.press('tab')
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.typewrite('https://addmefast.com/free_points/twitter_tweets')
pg.press('enter')
time.sleep(15)
press_button()

do_process()

altf4()
confirm()
carpi_kapat()