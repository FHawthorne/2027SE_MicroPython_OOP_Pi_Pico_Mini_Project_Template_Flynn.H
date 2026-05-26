from lib.pedestrian_button import pedestrian_button
from time import sleep

button = pedestrian_button(22, debug=True)

print("Please press and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    if button.button_state():  # Call the method correctly
        pressed = True
        break
    sleep(0.1)
if pressed:
    print("Button press detected: .button_state passed")
else:
    print("Button press not detected: .button_state failed")

print("Testing button_state setter (reset to false)")
button.button_state(False)  # Call the setter method correctly
sleep(0.1)
if button.button_state() is False:  # Call the getter method correctly
    print(".button_state setter passed")
else:
    print(".button_state setter failed")

print("Manual test complete")
