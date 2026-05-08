from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd


def setup_lcd():
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    devices = i2c.scan()

    if not devices:
        print("No I2C devices found.")
        return None

    i2c_addr = devices[0]
    print("LCD found at:", hex(i2c_addr))
    return I2cLcd(i2c, i2c_addr, 2, 16)


def main():
    lcd = setup_lcd()
    if lcd is None:
        return

    while True:
        lcd.clear()
        lcd.putstr("Hello world!")
        print("hello world")
        sleep(5)

        lcd.clear()
        print("clearing")
        sleep(1)


main()
