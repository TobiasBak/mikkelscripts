import pyautogui
import keyboard
import mouse

import trading, config

def main():
    Config = config.Config

    # Click on game, to focus
    mouse.move(800,600)
    pyautogui.click()

    while not keyboard.is_pressed(Config["keybindings"]["stop_running"]):
        # Add methods below
        trading.trading_main()


        


def print_coordinates():
    print('Press Ctrl-Shift-F10 to quit.')
    while not keyboard.is_pressed('ctrl+shift+f10'):
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)


if __name__ == "__main__":
    print('Starting Scripts')
    print_coordinates()
    
    print('Press Ctrl-Shift-F11 to quit.')
    try:
        main()
    except KeyboardInterrupt:
        print('Quitting Scripts')
    

