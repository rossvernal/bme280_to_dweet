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
    temperaturePrint = "{:05.2f}*C".format(temperature)
    pressure = bme280.get_pressure()
    pressurePrint =  "{:05.2f}hPa".format(pressure)
    humidity = bme280.get_humidity()
    humidityPrint = "{:05.2f}%".format(humidity)
    print('{:05.2f}*C {:05.2f}hPa {:05.2f}%'.format(temperature, pressure, humidity))

    dweepy.dweet_for('ingeniuus_ross_room', {'temperature': temperaturePrint, 'pressure': pressurePrint, 'humidity': humidityPrint })
    {
        u'content': {u'temperature': temperaturePrint, u'pressure': pressurePrint, u'humidity': humidityPrint},
        u'created': datetime.now() + timedelta(hours=1),
        u'thing': u'ingeniuus_ross_room'
    }

    #Update every 5 mins
    time.sleep(300)
