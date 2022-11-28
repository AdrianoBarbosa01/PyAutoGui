import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('Google')
pyautogui.press('enter')
#time.sleep(1)
pyautogui.write('https://github.com')
pyautogui.press('enter')