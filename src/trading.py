import pyautogui as pya
import time

import config

#Change these values
Config = config.Config

trade_key = Config["keybindings"]["trade"]
delay_in_seconds = Config["trading"]["delay_in_seconds"]

last_trade_time = time.time() - 1000

def trading_main(): 
    global last_trade_time

    seconds_since_last_trade = time.time() - last_trade_time

    if last_trade_time is None or seconds_since_last_trade > (delay_in_seconds):
        print("Trading")
        
        # Open trade ui
        pya.press(trade_key)
        
        # Run code
        locate_red_gems()

        # Close trade ui
        last_trade_time = time.time()
        pya.press(trade_key)

def locate_red_gems():
    # This method has to go over the screen coordinates covering the column of purchasable
    # If any item is red, it will save the coordinates of the red gem. 
    # A gem is red if the pixel color is (255, 0, 68)
    # Any pixels close to a red pixel found should never be checked again
    # Instead of checking all pixels on screen, we check every 10 pixels

    pixel_gap = 10
    screen_area = Config["settings"]["region"]

    screen = pya.screenshot(region=screen_area)
    width, height = screen.size

    positions = []
    
    for x in range(0, width, pixel_gap):
        for y in range(0, height, pixel_gap):
            color = screen.getpixel((x, y))
            if color == (255, 0, 68):
                print(f"Red gem found at {x}, {y}")
                # Click on the red gem
                positions.append((x, y))
    
    print(f"Red gems found at: {positions}")
