from time import sleep
from lib.controller import Controller
from lib.led_light import LedLight
from lib.pedestrian_button import PedestrianButton
from lib.audio_notification import AudioNotification

led_pedestrian_red = LedLight(19, True, False)
led_pedestrian_green = LedLight(17, False, False)
led_traffic_red = LedLight(3, False, False)
led_traffic_amber = LedLight(5, False, False)
led_traffic_green = LedLight(6, False, False)
pedestrian_button = PedestrianButton(22, False)
buzzer = AudioNotification(27, True)


controller = Controller(
    led_pedestrian_red,
    led_pedestrian_green,
    led_traffic_red,
    led_traffic_amber,
    led_traffic_green,
    pedestrian_button,
    buzzer,
    True,
)

while True:
    controller.update()
    sleep(0.1)-+
