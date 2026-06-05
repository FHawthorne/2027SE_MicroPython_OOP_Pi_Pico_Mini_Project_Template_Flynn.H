from lib.led_light import LedLight
from lib.controller import TrafficLightSubsystem
from lib.controller import PedestrianLightSubsystem
from time import sleep

red = LedLight(3, False, True)
amber = LedLight(5, False, True)
green = LedLight(6, False, True)


light = TrafficLightSubsystem(red, amber, green, True)


def Traffic_Subsystem_driver():
    print("Testing Traffic Light in 5 seconds")
    sleep(5)
    light.show_red()
    print("Pass if: Red ON, Amber, OFF and Green OFF")
    sleep(10)
    light.show_amber()
    print("Pass if: Amber ON, Red, OFF and Green OFF")
    sleep(10)
    light.show_green()
    print("Pass if: Green ON, Amber, OFF and Red OFF")
    sleep(10)


Traffic_Subsystem_driver()
