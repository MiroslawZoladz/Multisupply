import sys
sys.path.append('../lib')
import machine
from ssd1306 import SSD1306_I2C
from display import Display
import time

i2c=machine.SoftI2C(sda=machine.Pin(20), scl=machine.Pin(21), freq=100000)

display = Display(i2c)

while True:
    for i in range(5):
        display.show(i, i + i*0.789, i + i*0.321)
        time.sleep(1)