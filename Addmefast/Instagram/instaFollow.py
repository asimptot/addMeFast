import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.click(497, 194)
    time.sleep(4)
    pg.press(['tab', 'enter'])
    time.sleep(13)

open_browser()
pg.typewrite('https://addmefast.com/free_points/instagram')
pg.press('enter')
time.sleep(10)
insta_press_button()

do_process()

altf4()
confirm()
carpi_kapat()