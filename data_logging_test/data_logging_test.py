import os
import time
from datetime import datetime

def data_logging_demo():
# The user of the Docker container is root. The root directory is `/root`.
# Be sure to mount a volume to /root from the host system.
    with open("/root/data/temperature_log.csv") as f:
        for i in range(5):
            now = datetime.now()
            print(str(now))
            f.write(str(now))
            time.sleep(5)

if __name__ == "__main__":
    data_logging_demo()