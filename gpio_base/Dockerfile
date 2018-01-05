# reference https://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/
FROM resin/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get -q update && \
    apt-get -qy install \
        python python-pip \
        python-dev python-pip gcc make \
        build-essential git cmake \
        sqlite3 libsqlite3-dev \
        libblas-dev liblapack-dev \
        libatlas-base-dev gfortran

RUN pip install rpi.gpio \
        numpy \
        pandas \
        scipy \
        sqlalchemy

RUN echo "COMPLETE!"
