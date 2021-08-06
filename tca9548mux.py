#!/usr/bin/env python
import board
import busio
import adafruit_tca9548a
import adafruit_drv2605

i2c = busio.I2C(board.SCL, board.SDA)

tca = adafruit_tca9548a.TCA9548A(i2c)
drv1 = adafruit_drv2605.DRV2605(tca[0])
drv2 = adafruit_drv2605.DRV2605(tca[1])

while True:
        drv1.sequence[0] = adafruit_drv2605.Effect(1)
        drv1.play()
        drv2.sequence[0] = adafruit_drv2605.Effect(47)
        drv2.play()


