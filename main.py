import keyboard
import test
import time

alpha_metric = test.control()

start = time.time()
while time.time() - start < 60000:
    alpha_metric = test.control()
    if alpha_metric > 0.7:
        keyboard.press_and_release('UP')
    elif alpha_metric < 0.5:
        keyboard.press_and_release('DOWN')



