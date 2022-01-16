import time
import subprocess
import pyautogui as pg

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)

def press_button():
    pg.click(975, 841)
    time.sleep(10)

def insta_press_button():
    pg.click(975, 879)
    time.sleep(10)

def pinterest_press_button():
    pg.click(975, 790)
    time.sleep(10)

def confirm():
    pg.click(964, 901)
    time.sleep(10)

def tweet_confirm():
    pg.click(964, 857)
    time.sleep(10)

def carpi_kapat():
    pg.click(348, 23)
    time.sleep(5)

def altf4():
    pg.hotkey('alt', 'f4')
    time.sleep(5)

def ekran_goruntusu():
    pg.screenshot('Capture.png')