import pyautogui
import keyboard
import mouse
import easyocr

import trading, config
import autoscripts

reader: easyocr.Reader = easyocr.Reader(['ch_sim','en'], gpu=False)


def main():
    Config = config.Config

    # Click on game, to focus
    mouse.move(800,600)
    pyautogui.click()

    while not keyboard.is_pressed(Config["keybindings"]["stop_running"]):
        # Add methods below
        #trading.trading_main()
        autoscripts.auto_crunch(reader)
        


def print_coordinates() -> dict:
    out = {}
    print('Press Ctrl-Shift-F10 to quit.')
    while not keyboard.is_pressed('ctrl+shift+f10'):
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' RGB: ' + str(pyautogui.screenshot().getpixel((x, y)))
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        if mouse.is_pressed():
            out[(x, y)] = pixel_color
    
    return out


if __name__ == "__main__":
    print('Starting Scripts')
    saved_coordinates = print_coordinates()
    if saved_coordinates != {}:
        for coordinate, color in saved_coordinates.items():
            print(f"Coordinate: {coordinate}, Color: {color}")
    
    print('Press Ctrl-Shift-F11 to quit.')
    try:
        main()
        print('Quitting Scripts')
    except KeyboardInterrupt:
        print('Quitting Scripts')
    

