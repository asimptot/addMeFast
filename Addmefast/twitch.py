import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/twitch_followers')
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.click(992, 886)
time.sleep(10)

pg.click(948, 951)
time.sleep(10)


pg.hotkey('alt', 'f4')
time.sleep(5)
pg.click(348, 23)
time.sleep(5)