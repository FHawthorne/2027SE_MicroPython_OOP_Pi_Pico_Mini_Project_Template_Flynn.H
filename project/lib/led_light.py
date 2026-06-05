from machine import Pin
from time import sleep, time


class LedLight(Pin):
    """
    simple class to turn an led on or off on a rasberry pico.

    args:
    pin (int): GPIO pin number for the LED

    Example:
    led = LedPico(25) # Onboard LED
    led.SET(True) # Turn on
    led.set(False) # Turn off
    """

    def __init__(self, pin, flashing=False, debug=False):
        """Initializes the LED.

        Args:
            pin (int): GPIO pin number for the LED.
            flashing (bool, optional): If True, enables flashing mode. Defaults to False.
            debug (bool, optional): If True, prints debug messages. Defaults to False.
        """
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.led_light_state
        self.__last_toggle_time = time()

    @property
    def led_light_state(self):
        """Gets the current state of the LED.

        Returns:
            int: 1 if the LED is on, 0 if off.
        """

        # Getter method
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        """
        set the LED on or off.

        Args:
            State (bool): True to turn on, False to turn off.
        """
        # Setter method
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def on(self):
        """
        Turns LED on
        """
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        """
        Turns the LED off
        """
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        """
        toggle the LED state
        """
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    def flash(self):
        # Non-blocking flash: toggles LED every 0.05s for the given duration

        """Flash the LED on and off every 0.5s if flashing is enabled"""
        if not self.__flashing:
            return

        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
