from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True)

    name = Column(String)


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)

    name = Column(String)


class Measurement(Base):
    __tablename__ = 'measurement'

    id = Column(Integer, primary_key=True)

    time = Column(String)

    temperature = Column(Numeric)

    humidity = Column(Numeric)

    sensor_id = Column(Integer, ForeignKey("sensor.id"))

    sensor = relationship(Sensor)

    location_id = Column(Integer, ForeignKey("location.id"))

    location = relationship(Location)

def make_database():
    engine = create_engine('sqlite:////root/data/temperature.db')
    
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    make_database()