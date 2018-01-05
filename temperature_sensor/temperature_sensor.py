import os
import time
from datetime import datetime
import RPi.GPIO as GPIO

def temperature_sensor():
    with open("/root/temperature_log.csv") as f:
        for i in range(5):
            now = datetime.now()
            f.write(str(now))
            time.sleep(5)

if __name__ == "__main__":
    temperature_sensor()