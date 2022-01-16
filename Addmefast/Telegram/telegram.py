import pyautogui as pg
import time
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Addmefast')
from init import *

def do_process():
    pg.press('end')
    time.sleep(2)
    pg.click(378, 763)
    time.sleep(3)
    pg.click(488, 824)
    time.sleep(3)

open_browser()
pg.typewrite('https://addmefast.com/free_points/telegram_subscribers')
pg.press('enter')
time.sleep(10)
press_button()

do_process()

altf4()
carpi_kapat()