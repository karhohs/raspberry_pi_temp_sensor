import os
import time
from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:////root/data/temperature.db")    
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Measurement(Base):
    __tablename__ = 'measurements'

    id = Column(Integer, primary_key=True)

    time = Column(String)

    temperature = Column(Numeric)

    humidity = Column(Numeric)

def data_logging_demo():
# The user of the Docker container is root. The root directory is `/root`.
# Be sure to mount a volume to /root from the host system.
    data_logging_demo_csv()

def data_logging_demo_sqlite():

    fake_data = [
        [10, 20],
        [11, 20],
        [15, 15],
        [20, 40],
        [19, 25]
        ]

    session = Session()

    for i in range(5):
        now = datetime.now()

        fake_data_list = fake_data[i]

        meas_obj = Measurements(
            time=now,
            temperature=fake_data_list[0],
            humidity=fake_data_list[1]
        )

        session.add(meas_obj)

        session.commit()

        time.sleep(5)

def data_logging_demo_csv():
    with open("/root/data/temperature.csv", "a") as f:
        for i in range(5):
            now = datetime.now()
            print(str(now))
            f.write(', '.join([str(now)])+"\n")
            time.sleep(5)

if __name__ == "__main__":
    data_logging_demo()