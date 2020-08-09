import pyautogui as pg
import time
import subprocess

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('https://addmefast.com/free_points/instagram')
    time.sleep(2)
    pg.press('delete')
    time.sleep(2)
    pg.press('enter')
    time.sleep(10)

def maximize():
    pg.hotkey('alt', 'space')
    time.sleep(2)
    for j in range(5):
        pg.press('down')
    time.sleep(2)
    pg.press('enter')

for i in range(90):
    open_browser()
    time.sleep(2)
    maximize()
    time.sleep(5)
    pg.click(1011, 869)
    time.sleep(10)

    pg.press(['tab', 'enter'])
    time.sleep(10)

    for j in range(2):
        pg.hotkey('alt', 'f4')
        time.sleep(10)

