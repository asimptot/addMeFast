import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/telegram_subscribers')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.click(1000, 867)
time.sleep(10)
pg.click(515, 819)
time.sleep(13)

pg.hotkey('alt', 'f4')
time.sleep(5)
pg.click(348, 23)
time.sleep(5)