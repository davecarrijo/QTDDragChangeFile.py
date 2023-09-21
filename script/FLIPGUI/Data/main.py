import time
import pyautogui as pg
from pynput import keyboard

screenWidth, screenHeight = pg.size()

# The key combinations to look for
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=65)}  # shift + a (see below how to get vks)A
]


def execute():
    """ My function to execute when a combination is pressed """
    pg.moveTo(750, 300)
    pg.click()
    #rotate 90'n degress
    def Rotate90D():
        pg.rightClick()
        pg.move(20, 5)
        pg.rightClick()

    for i in range(2):
        Rotate90D()

    # FLip the canvas horizontal
    def flipHorizontal():
        pg.rightClick()
        pg.move(40,75)
        pg.rightClick()

    flipHorizontal()
    pg.moveTo(100, 700)

    # Stationary mouse mode
    for i in range(2):
        pg.click

    print("Do Something")


# The currently pressed keys (initially empty)
pressed_vks = set()


def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    """ Check if a combination is satisfied using the keys pressed in pressed_vks """
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    """ When a key is pressed """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in COMBINATIONS:  # Loop though each combination
        if is_combination_pressed(combination):  # And check if all keys are pressed
            execute()  # If they are all pressed, call your function
            break  # Don't allow execute to be called more than once per key press


def on_release(key):
    """ When a key is released """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Join the listener thread to the current thread so we don't exit before it stops