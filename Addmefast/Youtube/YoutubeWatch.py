import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    time.sleep(160)

open_browser()
pg.typewrite('https://addmefast.com/free_points/youtube_views')
pg.press('enter')
time.sleep(10)
press_button()

do_process()
ekran_goruntusu()

altf4()
carpi_kapat()