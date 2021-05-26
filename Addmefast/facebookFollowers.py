import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/facebook_subscribes')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.click(994, 791)
time.sleep(10)
pg.click(541, 552)
time.sleep(13)

pg.hotkey('alt', 'f4')
time.sleep(5)
pg.click(348, 23)
time.sleep(5)