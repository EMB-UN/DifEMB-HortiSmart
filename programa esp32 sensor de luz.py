import ltr390
from machine import Pin, I2C
import utime

sensor_i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)
ltr = ltr390.LTR390(sensor_i2c)
ltr.set_uvs()
ltr.set_gain(ltr390.eGain18)
ltr.set_measure_rate(ltr390.e20bit, ltr390.e1000ms)

while True:
    v = ltr.uvs()
    print(f"V: {v}")
    utime.sleep_ms(500)