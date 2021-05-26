import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/twitter_likes')
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.click(994, 865)
time.sleep(10)

for j in range(2):
    pg.press('tab')
time.sleep(2)
pg.press('enter')
time.sleep(20)

pg.hotkey('alt', 'f4')
time.sleep(5)
pg.click(348, 23)
time.sleep(5)