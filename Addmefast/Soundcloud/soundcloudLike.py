import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    for j in range(18):
        pg.press('tab')
    time.sleep(2)
    pg.press('enter')
    time.sleep(13)


open_browser()
pg.typewrite('https://addmefast.com/free_points/soundcloud_likes')
time.sleep(2)
pg.press('enter')
time.sleep(10)
press_button()

do_process()

altf4()
carpi_kapat()