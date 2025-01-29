import pyautogui as pya
import mouse
import time

def leftclick():
    """Simulate a left click."""
    pya.mouseDown()
    time.sleep(0.01)
    pya.mouseUp()

def leftclick_at(x: int, y: int):
    """Simulate a left click at a specific position."""
    mouse.move(x, y)
    time.sleep(0.01)
    leftclick()

def keypress(key: str):
    """Simulate a key press."""
    pya.keyDown(key)
    time.sleep(0.01)
    pya.keyUp(key)