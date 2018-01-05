# reference https://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/
FROM resin/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get -q update && \
    apt-get -qy install \
        python python-pip \
        python-dev python-pip gcc make \
        build-essential git \
        sqlite3 libsqlite3-dev \
        unzip

RUN pip install rpi.gpio \
        sqlalchemy
