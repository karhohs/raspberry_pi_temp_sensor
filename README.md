https://www.losant.com/blog/getting-started-with-the-raspberry-pi-zero-w-without-a-monitor

https://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/

Reboot as needed with `sudo reboot`

1. Follow the instructions for downloading Raspbian onto an SD card and setting up wireless.
   1. This entails creating an `ssh` file on the boot image and setting up wireless.

1. SSH into the pi.
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

1. Install docker
   ```bash
   curl -sSL https://get.docker.com | sh
   sudo systemctl enable docker
   sudo usermod -aG docker pi
   ```
   1. reboot

1. Install some packages.

   ```bash
   sudo apt-get install -y git \
   tmux
   ```

1. Clone the temperature sensor repo `git clone https://github.com/karhohs/raspberry_pi_temperature_sensor`

1. Within the github repo, build the base Docker image and test it. The data_logging_test can be run without having to connect the temperature sensor the Raspberry Pi Zero W.
   ```bash
   cd ./raspberry_pi_temperature_sensor/gpio_base
   docker build -t gpio_base .
   mkdir -p /home/pi/data
   cd ../data_logging_test
   docker build -t data_logging_test .
   docker run -d -v /home/pi/data:/root/data -i data_logging_test:latest

   ```
   1. To interact with a container try `docker run -it gpio_base:latest bash`

1.
   1. Note that I like to typically work with Anaconda to manage programming environments, but the armv6l processor within the Raspberry Pi Zero W is not well supported. The deal breaker was not being able to run python 3 or jupyter notebook. I think working outside of typical

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
