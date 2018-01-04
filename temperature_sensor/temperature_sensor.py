import os
import time
from datetime import datetime

def temperature_sensor():
    with open("temperature_log") as f:
        for i in range(5):
            now = datetime.now()
            f.write(str(now))
            time.sleep(5)

if __name__ == "__main__":
    temperature_sensor()