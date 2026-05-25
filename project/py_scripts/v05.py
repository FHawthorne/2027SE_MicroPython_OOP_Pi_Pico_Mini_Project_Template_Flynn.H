from lib.pedestrian_button import pedestrian_button
from time import sleep

button = pedestrian_button(22, debug=True)

print("Please press and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    if button.button_state:
        pressed = True
        break
