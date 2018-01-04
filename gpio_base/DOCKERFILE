# reference https://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/
FROM resin/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get -q update && \
    apt-get -qy install \
        python python-pip \
        python-dev python-pip gcc make

RUN pip install rpi.gpio
