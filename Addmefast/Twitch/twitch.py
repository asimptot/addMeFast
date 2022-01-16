import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.click(913, 951)
    time.sleep(10)

open_browser()
pg.typewrite('https://addmefast.com/free_points/twitch_followers')
pg.press('enter')
time.sleep(10)
press_button()

do_process()

altf4()
carpi_kapat()