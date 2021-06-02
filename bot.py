from pynput.mouse import Listener as MouseListener
# from pynput.keyboard import Listener as KeyboardListener

import pyautogui as gui
from time import sleep
import random as r



def comment(i):
    # clicking reply txt
    gui.moveTo(1562, 485, duration=0)
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
    sleep(2)
    comment(0)

def main():
    sleep(2)
    for i in range (50):
        comment(i)



# gui.typewrite('Bello')
# gui.typewrite(["enter"])

# gui.typewrite('Kaning is Special')

# gui.moveTo(1876, 1004, duration = 1)


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



# test()
main()