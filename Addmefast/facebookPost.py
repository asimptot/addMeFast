import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/facebook_post_share')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

open_browser()
pg.click(994, 820)
time.sleep(10)
pg.press('end')
time.sleep(2)
pg.click(436, 793)
time.sleep(2)
pg.click(76, 518)
time.sleep(13)

pg.hotkey('alt', 'f4')
time.sleep(5)
pg.click(348, 23)
time.sleep(5)