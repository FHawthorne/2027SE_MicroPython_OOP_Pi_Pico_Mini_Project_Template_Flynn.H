from time import sleep
from lib.led_light import LedLight

red_light = LedLight(3, True, True)

while True:
    red_light.flash()
    print(1)
    sleep(0.1)
