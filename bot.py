from pynput.mouse import Listener as MouseListener
# from pynput.keyboard import Listener as KeyboardListener

import pyautogui as gui
from time import sleep
import random as r



def comment(i):
    # clicking reply txt
    gui.moveTo(1539, 519, duration=0)
    gui.click()

    # Clicking msg block
    gui.moveTo(1636, 1006, duration=0)
    gui.click()
    gui.typewrite(str(i))

    # clicking post
    gui.moveTo(1876, 1006)
    gui.click()
    sleep(5 + r.random())

print(gui.size())

def test():
    sleep(5)
    comment(0)

def main():
    sleep(5)
    # Limit is 150
    for i in range (150):
        comment(i)


# Debugging Zone
def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    print('x = ', x)
    print('y = ', y)
    print('key = ', button)
    print('pressing = ', pressed)

def on_scroll(x, y, dx, dy):
    pass

def listen():
    with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()



# One time test
test()

# Execute Script
# main()

# Debugging Listener
# listen()