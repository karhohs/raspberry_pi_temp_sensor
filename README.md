https://www.losant.com/blog/getting-started-with-the-raspberry-pi-zero-w-without-a-monitor

1. Follow the instructions for downloading Raspbian onto an SD card and setting up wireless.

1. SSH into the pi.
   * username: pi
   * password: raspberry

1. `wget https://repo.continuum.io/miniconda/Miniconda-3.5.5-Linux-armv6l.sh`

1. `bash Miniconda-3.5.5-Linux-armv6l.sh`
   1. add miniconda to the PATH when prompted.
      1. `export PATH=/home/pi/miniconda/bin:$PATH`
