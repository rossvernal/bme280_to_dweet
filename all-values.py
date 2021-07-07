#!/usr/bin/env python

import time
import dweepy
from smbus import SMBus
from bme280 import BME280
from datetime import datetime, timedelta

print("""all-values.py - Read temperature, pressure, and humidity
Press Ctrl+C to exit!
""")

# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

while True:
    temperature = bme280.get_temperature()
    temperaturePrint = "{:05.2f}".format(temperature)
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    print('{:05.2f}*C {:05.2f}hPa {:05.2f}%'.format(temperature, pressure, humidity))

    dweepy.dweet_for('ingeniuus_ross_room', {'temperature': temperaturePrint })
    {
        u'content': {u'temperature': temperaturePrint},
        u'created': datetime.now() + timedelta(hours=1),
        u'thing': u'ingeniuus_ross_room'
    }

    time.sleep(10)