from lib.led_light import LedLight
from lib.controller import PedestrianLightSubsystem
from lib.pedestrian_button import PedestrianButton
from lib.audio_notification import AudioNotification
from time import sleep

red = LedLight(19, True, True)
green = LedLight(17, False, True)
button = PedestrianButton(22, True)
buzzer = AudioNotification(27, True)
light = PedestrianLightSubsystem(red, green, button, buzzer, True)


def Pedestrian_subsystem_driver():
    print("Testing Pedestrian subsystem in 5 seconds")
    sleep(5)
    light.show_stop()
    print("Pass if Red: ON, Green: OFF")
    sleep(10)
    light.show_walk()
    print("Pass if Green: ON, Red: OFF")
    sleep(10)
    light.show_warning()
    print("Pass if Red: flashing, Green: OFF, Buzzer beeps")
    sleep(10)


def test_button():
    print("Press button within 5 seconds")
    sleep(5)
    if light.is_button_pressed():
        print("Test passed!")
        light.reset_button()
        button_pressed = True
    else:
        print("Test failed check button!")
    if button_pressed:
        print("Press button within 5 seconds to test the reset function")
        sleep(5)

        light.reset_button()

        if light.is_button_pressed is False:
            print("Test passed")
        elif light.is_button_pressed is True:
            print("Test failed check code")


Pedestrian_subsystem_driver()
test_button()
