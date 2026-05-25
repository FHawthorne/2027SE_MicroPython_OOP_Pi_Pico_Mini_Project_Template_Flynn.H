from machine import Pin
from time import sleep
from led_light import Led_Light

red_light = Led_Light(3)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
