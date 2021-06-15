import time
import subprocess
import pyautogui as pg

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)

def press_button():
    pg.click(992, 825)
    time.sleep(10)

def confirm():
    pg.click(960, 835)
    time.sleep(10)

def carpi_kapat():
    pg.click(348, 23)
    time.sleep(5)

def altf4():
    pg.hotkey('alt', 'f4')
    time.sleep(5)

def ekran_goruntusu():
    pg.screenshot('Capture.png')