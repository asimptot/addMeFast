import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/soundcloud_likes')
    time.sleep(2)
    pg.press('delete')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

for i in range(1):
    open_browser()
    time.sleep(7)
    pg.click(994, 791)
    time.sleep(20)

    for j in range(18):
        pg.press('tab')
    time.sleep(2)
    pg.press('enter')
    time.sleep(13)

    for j in range(2):
        pg.hotkey('alt', 'f4')
        time.sleep(10)