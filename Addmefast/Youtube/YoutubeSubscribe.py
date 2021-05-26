import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    for j in range(10):
        pg.press('tab')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.typewrite('https://addmefast.com/free_points/youtube_subscribe')
pg.press('enter')
time.sleep(10)
press_button()

do_process()

altf4()
ekran_goruntusu()
carpi_kapat()