# Please read the 'readme.md' file


from pynput.mouse import Listener as MouseListener

import pyautogui as gui
from time import sleep
import random as r


# Comment function
def comment(i):
    # clicking reply txt
    gui.moveTo(1539, 519, duration=0)
    gui.click()

    # clicking msg block
    gui.moveTo(1636, 1006, duration=0)
    gui.click()

    # typing text
    gui.typewrite(str(i))

    # clicking post
    gui.moveTo(1876, 1006)
    gui.click()

    # sleep for 5 +- less than 1 to avoid bot detection(dont know if it worked)
    sleep(5 + r.random())

def test():
    sleep(5)
    comment(0)

def main():
    print('please open your browser with member\'s tiktok video in maximum window size')
    sleep(5)
    print('turn off bookmark bar by pressing \'ctrl + shift + b\'')
    sleep(5)
    print('get ready in 5')
    sleep(1)
    print('get ready in 4')
    sleep(1)
    print('get ready in 3')
    sleep(1)
    print('get ready in 2')
    sleep(1)
    print('get ready in 1')
    sleep(1)
    print('script started')

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
# test()

# Execute Full Script
main()

# Debugging Listener (to edit mouse position for each machine)
# listen()