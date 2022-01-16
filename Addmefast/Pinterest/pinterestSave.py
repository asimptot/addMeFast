import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.click(1382, 301)
    time.sleep(10)

open_browser()
pg.typewrite('https://addmefast.com/free_points/pinterest_save')
pg.press('enter')
time.sleep(15)
pinterest_press_button()

do_process()

altf4()
carpi_kapat()