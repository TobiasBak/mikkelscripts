import pyautogui
import config
import easyocr
import time
from utils import leftclick, leftclick_at
import mouse


Config = config.Config
crunch_key = Config["keybindings"]["crunch"]

last_trade_time = time.time() - 1000

def auto_crunch(reader: easyocr.Reader):
    
    crunch_value = read_crunch_value(reader)
    if crunch_value is None:
        return

    value_float = convert_crunchvalue_to_float(crunch_value)
    min_value = Config["crunch"]["min_value"]
    print(f"Crunch value: {value_float}, min value: {min_value}")

    if value_float > Config["crunch"]["min_value"]:
        crunch()

def read_crunch_value(reader: easyocr.Reader) -> str:
    delay_in_seconds = Config["crunch"]["delay_in_seconds"]
    global last_trade_time

    seconds_since_last_trade = time.time() - last_trade_time
    if last_trade_time is None or seconds_since_last_trade < (delay_in_seconds):
        return

    print("[Crunch Value] Start")
    pyautogui.press(crunch_key)

    startpos = Config["crunch"]["start_pos"]
    endpos = Config["crunch"]["end_pos"]

    # Create image to feed ocr
    image = pyautogui.screenshot(region=(startpos[0], startpos[1], endpos[0] - startpos[0], endpos[1] - startpos[1]))
    image.save("src/tmp/test.jpg")

    # use ocr to read the value
    result = reader.readtext("src/tmp/test.jpg", detail = 0)
    if result == []:
        print("[Crunch Value] No value found")
        return None
    
    result = result[0]

    print("[Crunch Value] Done")
    time.sleep(0.5)
    pyautogui.press("esc")
    last_trade_time = time.time()
    return result

def convert_crunchvalue_to_float(value: str) -> float:
    # The value will be in example "1.09 I". This means 1.09 million
    # We need to convert this to a float.
    # We can times the number with 1 million if the last character is "I"

    if value[-1] == "I":
        return float(value[:-2]) * 1000000
    else:
        return float(value)
    
def crunch():
    crunch_pos = Config["crunch"]["crunch_button"]
    x, y = crunch_pos
    pyautogui.press(crunch_key)
    time.sleep(0.01)
    leftclick_at(x, y)
    leftclick()