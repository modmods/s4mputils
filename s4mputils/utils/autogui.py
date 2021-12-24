import pyautogui
import os
import time


class Autogui():
    
    def findAndClick(self, imagename, grayscale = True, confidence = 0.9):
        time.sleep(1)
        path = os.path.join(os.path.dirname(__file__), 'resources', imagename)
        print(path)
        coords = self.retry(pyautogui.locateCenterOnScreen, 10, .5, path, grayscale = grayscale, confidence = confidence)
        if not coords:
            return None
        print(coords[0])
        print(coords[1])
        pyautogui.click(coords[0], coords[1])
        
    def writeAndEnter(self, text):
        pyautogui.write(text)
        pyautogui.press('enter')

    def retry(self, func, retries, wait, *args, **kwargs):
        r = retries
        rt = None
        while not rt and r > 0:
            rt = func(*args, **kwargs)
            r -= 1
            time.sleep(wait)
        return rt
