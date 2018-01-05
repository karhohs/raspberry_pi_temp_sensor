# Introduction
This project details the software and hardware required to create a data logging temperature sensor with a Raspberry Pi Zero W.

## Motivation
In late 2017 and early 2018, the Boston area was hit by a historically cold stretch of weather and a bomb-cyclone. In the first stretch of overnight single digit Fahrenheit temperatures my plumbing froze inside an unfinished basement. I patched some holes in the brick walls, added insulation around the pipes, and ran a space heater to thaw everything out (thankfully no broken pipes!). However, even though I could manage the situation, I wanted to further understand the relationship between the temperature outside and the temperature inside the basement. I thought it would be fascinating to quantify how quickly the basement loses heat to the outside. To avoid running up the electric bill, could I find an overnight-low threshold that would indicate when I should use the space heater in the basement? How much did the space heater raise the temperature in the basement? How insulating are the brick walls? I believed I could answer these questions with the help of a Raspberry Pi while having some fun, so I set out to create a battery-powered temperature sensor.

# Parts List
1. Raspberry Pi Zero W
1. DHT22 temperature sensor
1. Lexar 16GB SD card
1. Anker PowerCore+ mini 3350
1. Amazon USB to USB micro 3ft
1. Hammond project box
1. Small parts such as:
   1. Standoffs
   1. Foam
   1. Screws
   1. Rubber feet
   1. Labels

# Getting Started
## Configuring the Raspberry Pi Zero W
*Reboot as needed with `sudo reboot`*

1. Follow the [instructions](https://www.losant.com/blog/getting-started-with-the-raspberry-pi-zero-w-without-a-monitor) for downloading Raspbian onto an SD card and setting up wireless.
   1. This entails creating an `ssh` file on the boot image and setting up wireless.
   1. The link is not an official documentation, but it is well written and has more details.
   1. [Ethcher](https://etcher.io/) is such an awesome tool for Raspberry Pi.

1. SSH into the pi, e.g. `ssh pi@raspberrypi.local`; the default hostname is *raspberrypi*. Alternatively, the IP can be used, but the IP is typically designated dynamically. Log in to a home router to find the IP with the Raspberry Pi device name or hostname.
   * first time username and password...
   * username: pi
   * password: raspberry

1. Change the password to prevent getting hacked. `passwd`

1. Update the hostname to something distinct.
   1. `sudo nano /etc/hosts`
   1. `sudo nano /etc/hostname`

1. Update and upgrade the OS.
   ```bash
   sudo apt-get update
   sudo apt-get upgrade -y
   ```

 1. Reduce gpu memory dedicated to the os, because it is run in headless mode and does need to support a desktop gui.
    1. `sudo nano /boot/config.txt`
       1. add the line `gpu_mem=16`

1. [Install docker](https://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/).
   ```bash
   curl -sSL https://get.docker.com | sh
   sudo systemctl enable docker
   sudo usermod -aG docker pi
   ```
   1. reboot

1. Install some helpful packages.

   ```bash
   sudo apt-get install -y git \
   tmux
   ```

1. Clone the temperature sensor repo `git clone https://github.com/karhohs/raspberry_pi_temperature_sensor`

1. Within the github repo, build the base Docker image and test it. The data_logging_test can be run without having to connect the temperature sensor the Raspberry Pi Zero W. 5 timepoints will be saved at 5 second intervals. This is a sanity check to make sure the gpio_base image is working as expected.
   ```bash
   cd ./raspberry_pi_temperature_sensor/gpio_base
   docker build -t gpio_base .
   mkdir -p /home/pi/data
   cd ../data_logging_test
   docker build -t data_logging_test .
   docker run -d -v /home/pi/data:/root/data -i data_logging_test:latest
   # wait about 30 seconds
   cat /home/pi/data/temperature.csv
   ```
   1. To interact with a container try `docker run -it gpio_base:latest bash`
   1. To do some trouble shooting leave off the `-d` flag for the command `docker run`. Otherwise the container is detached from the command line after it is created. `docker ps` will show any running docker containers.

1.

# Supplemental Information

## Numpy and the Raspberry Pi Zero W
I sunk some time into trying to get numpy running on the Raspberry Pi Zero W. I never could get past the `pip install numpy` step, because it would freeze. My troubleshooting was focused on finding a missing dependency in the host system, but I couldn't find a fix. After Googling around I developed the sense that numpy is too demanding for the Raspberry Pi Zero W. I thought I might use it to do some math before logging the data, but in the end I didn't think it was worth the trouble when once the system started pushing back. The moral of the story is I think the Raspberry Pi Zero W is perfect for collecting data, but even light analysis should be avoided if possible.

## Exploring Anaconda on Raspberry Pi Zero W
I like to typically work with Anaconda to manage programming environments, but the armv6l processor within the Raspberry Pi Zero W is not well supported. Ultimately, I found I could accomplish what I wanted through Docker, but here a few notes in case it is helpful in the future.

1. `wget https://repo.continuum.io/miniconda/Miniconda-3.5.5-Linux-armv6l.sh`

1. `bash Miniconda-3.5.5-Linux-armv6l.sh`
   1. add miniconda to the PATH when prompted.
      1. `export PATH=/home/pi/miniconda/bin:$PATH`

   1. Creating a test environment...
   ```bash
   conda create -n demo python=2.7
   source activate demo
   conda install -c rpi numpy
   conda list
   ```
