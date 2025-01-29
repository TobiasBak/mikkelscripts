import time
import mouse
import pyautogui

import config
from utils import leftclick

#Change these values
Config = config.Config

trade_key = Config["keybindings"]["trade"]
delay_in_seconds = Config["trading"]["delay_in_seconds"]

last_trade_time = time.time() - 1000

def trading_main(): 
    global last_trade_time

    seconds_since_last_trade = time.time() - last_trade_time

    if last_trade_time is None or seconds_since_last_trade > (delay_in_seconds):
        # Open trade ui
        pyautogui.press(trade_key)
        time.sleep(0.5)
        
        # Run code
        gem_locations: list = locate_red_gems()
        start_gem_trades(gem_locations)
        refresh_trades()

        # Close trade ui
        last_trade_time = time.time()
        pyautogui.press(trade_key)

def locate_red_gems() -> list:
    # This method has to go over the screen coordinates covering the column of purchasable
    # If any item is red, it will save the coordinates of the red gem. 
    # A gem is red if the pixel color is (255, 0, 68)
    # Any pixels close to a red pixel found should never be checked again
    # Instead of checking all pixels on screen, we check every 10 pixels

    out: list = []

    screen_area = Config["settings"]["region"]
    trading_coordinates_list: list = Config["trading"]["trading_coordinates"]
    screen = pyautogui.screenshot(region=screen_area)

    start_pos_delta_x = 610
    print(f"Checking for red gems at: {trading_coordinates_list}")
    
    for coordinate in trading_coordinates_list:
        x, y = coordinate
        print(f"Checking pixel at: {x}, {y}")

        # check if pixel is red
        pixel_color = screen.getpixel((x, y))
        print(f"Pixel color: {pixel_color}")
        if not pixel_color == (255, 0, 68):
            continue
            
        start_pixel_color = screen.getpixel((x + start_pos_delta_x, y))
        if start_pixel_color == (255, 241, 210):
            out.append(coordinate)
        
    
    print(f"Red gems found at: {out}")
    return out


def start_gem_trades(list_of_gem_locations: list):
    if not list_of_gem_locations:
        return
    
    print(f"Starting trades for gems at: {list_of_gem_locations}")
    
    delta_x = 610
    for coordinate in list_of_gem_locations:
        x,y = coordinate
        mouse.move((x + delta_x), y)
        leftclick()

def refresh_trades():
    screen_area = Config["settings"]["region"]
    trading_coordinates_list = Config["trading"]["trading_coordinates"]
    screen = pyautogui.screenshot(region=screen_area)

    delta_x = 610

    print(f"Checking if trades need to be refreshed at: {trading_coordinates_list}")

    refresh = False

    for coordinate in trading_coordinates_list:
        x, y = coordinate
        print(f"Checking pixel at: {x + delta_x}, {y}")
        print(screen.getpixel((x + delta_x, y)))
        if screen.getpixel((x + delta_x, y)) == (255, 241, 210) or screen.getpixel((x + delta_x, y)) == (200, 189, 165):
            refresh = True
            break
    
    print(f"Refreshing trades: {refresh}")

    if refresh:
        mouse.move(450, 840)
        leftclick()