import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.doubleClick(40, 314)
    time.sleep(10)

open_browser()
pg.typewrite('https://addmefast.com/free_points/instagram_likes')
pg.press('enter')
time.sleep(15)
insta_press_button()

do_process()

altf4()
confirm()
carpi_kapat()