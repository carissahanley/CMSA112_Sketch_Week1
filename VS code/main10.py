import mock_m5stick as stick
import tools
import time

#BooLeans
awake = False

def update_display():
    if awake:
        device.display_message("Hello.")
    else:
        device.erase_screen()

while True:
        if device.button_pressed():
            awake = not awake
            update_display()
        time.sleep(0.5)



