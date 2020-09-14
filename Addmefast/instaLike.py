import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/instagram_likes')
    pg.press('enter')
    time.sleep(10)

for i in range(1):
    open_browser()
    time.sleep(7)
    pg.click(994, 823)
    time.sleep(10)
    pg.doubleClick(40, 314)
    time.sleep(10)

    for j in range(2):
        pg.hotkey('alt', 'f4')
        time.sleep(10)