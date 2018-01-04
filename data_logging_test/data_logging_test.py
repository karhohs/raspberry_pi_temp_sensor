import os
import time
from datetime import datetime

def data_logging_demo():
    for i in range(5):
        now = datetime.now()
        print(str(now))
        time.sleep(5)

if __name__ == "__main__":
    data_logging_demo()