import pyautogui as pya
import time
import mouse

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
        gem_locations: list = locate_red_gems()
        start_gem_trades(gem_locations)
        refresh_trades()

        # Close trade ui
        last_trade_time = time.time()
        pya.press(trade_key)

def locate_red_gems() -> list:
    # This method has to go over the screen coordinates covering the column of purchasable
    # If any item is red, it will save the coordinates of the red gem. 
    # A gem is red if the pixel color is (255, 0, 68)
    # Any pixels close to a red pixel found should never be checked again
    # Instead of checking all pixels on screen, we check every 10 pixels

    out: list = []

    screen_area = Config["settings"]["region"]
    trading_coordinates_list = Config["trading"]["trading_coordinates"]
    screen = pya.screenshot(region=screen_area)

    start_pos_delta_x = 610
    
    for coordinate in trading_coordinates_list:
        x, y = coordinate

        # check if pixel is red
        pixel_color = screen.getpixel((x, y))
        if not pixel_color == (255, 0, 68):
            return
            
        start_pixel_color = screen.getpixel((x + start_pos_delta_x, y))
        if start_pixel_color == (255, 241, 210):
            out.append(coordinate)
        
    
    print(f"Red gems found at: {out}")
    return out


def start_gem_trades(list_of_gem_locations: list):
    if not list_of_gem_locations:
        return
    
    delta_x = 610
    for coordinate in list_of_gem_locations:
        x,y = coordinate
        mouse.move((x + delta_x), y)
        pya.click()

def refresh_trades():
    screen_area = Config["settings"]["region"]
    trading_coordinates_list = Config["trading"]["trading_coordinates"]
    screen = pya.screenshot(region=screen_area)

    delta_x = 610

    refresh = False

    for coordinate in trading_coordinates_list:
        x, y = coordinate
        if screen.getpixel((x + delta_x, y)) == (255, 241, 210) or screen.getpixel((x + delta_x, y)) == (200, 189, 165):
            refresh = True
            break
    
    if refresh:
        mouse.move(450, 840)
        pya.click()