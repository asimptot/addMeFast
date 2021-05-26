import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.click(1139, 587)
    time.sleep(13)

open_browser()
pg.typewrite('https://addmefast.com/free_points/soundcloud_follow')
pg.press('enter')
time.sleep(10)
press_button()

do_process()

altf4()
ekran_goruntusu()
carpi_kapat()