import random

def set_screen_color(r, g, b):
    print("Screen color set to {},{},{}".format(r, g, b))

def erase_screen():
    set_screenColor(0, 0, 0)

def display_message(msg):
    print(msg)

def button_pressed():
    global pressed
    state = pressed
    pressed = not pressed 
    return state
