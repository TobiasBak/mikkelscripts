import pyautogui as pya
import time

def leftclick():
    """Simulate a left click."""
    pya.mouseDown()
    time.sleep(0.01)
    pya.mouseUp()