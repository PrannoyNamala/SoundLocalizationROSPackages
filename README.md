# Sound Localization ROSberry Pi Package

## Prerequisites
#### Hardware
- Raspberry Pi with Buster OS
- MATRIX Creator microphone array
- Tyless iTalk - 02 microphone (or any other USB microphone)
#### Software
- ROSBerry Pi(Installation instructions linked [here](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi))
- Matrix ODAS Repository(Installation instruction given below)
- PicoVoice Wakeword Detection()Installation instructons given below)

### Matrix ODAS Installation
*Source: https://www.hackster.io/matrix-labs/direction-of-arrival-for-matrix-voice-creator-using-odas-b7a15b

Some of the instructions at the source link mentioned above will give installation errors. The commands below have been tested for the prerequisites above.
```
cd ~/
curl https://s3.amazonaws.com/apt.matrix.one/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://s3.amazonaws.com/apt.matrix.one/raspbian buster main" | sudo tee /etc/apt/sources.list.d/matrixlabs.list

sudo apt-get update
sudo apt-get upgrade

sudo apt install matrixio-creator-init
sudo apt install libmatrixio-creator-hal
sudo apt install libmatrixio-creator-hal-dev

sudo reboot

sudo apt install matrixio-kernel-modules

sudo reboot

sudo apt-get install g++ git cmake
sudo apt-get install libfftw3-dev
sudo apt-get install libconfig-dev
sudo apt-get install libasound2-dev
sudo apt install libjson-c-dev

cd ~/
git clone https://github.com/matrix-io/odas.git
cd odas
git checkout yc/add-matrix-demo
mkdir build
cd build
cmake ..
make
```

### PicoVoice Installation
*Source: https://github.com/Picovoice/porcupine

Run the following instructions to install the wakeword detection package.

```
cd ~/
git clone --recurse-submodules git@github.com:Picovoice/porcupine.git
sudo pip3 install pvporcupinedemo
```

For running the wakeword detection, you will need a PicoVoice access key and the index of the microphone used for listening for the wakeword. Access Key can be obtained by logging in [here](https://console.picovoice.ai/login). For microphone index, run ```porcupine_demo_mic --show_audio_devices```. In the output of the following command, note the index number of the USB microphone used in the setup.

For the detection purposes, default wakeword **Porcupine** is used.

## Running the Package
Place the ```init_odas.py``` in the ```~/odas/bin``` folder

First intitialize the Sound Localization
```
cd ~/odas/bin
python3 init_odas.py
```

Open Another terminal. In this terminal we will build the ROS Packages and run ```roscore```. We will assume that you have a catkin workspace setup on your Raspberry Pi(named ```catkin_ws``` here). In the ```src``` folder of the ```catkin_ws```, place the folder ```localize_sound```. After that, follow the steps mentioned below.
```
cd catkin_ws
source devel/setup.bash
catkin_make -j1
roscore
```

Open another terminal. In this terminal, we will track the output from the localization process.
```
cd ~/catkin_ws/src/localize_sound
python3 read_output.py
```
Now we will run the wkeword detection process. . Before we run it, update the ```access_key``` and the ```audio_device_index``` in the ```run_wakeword.py``` noted earlier. Open another terminal. In this terminal, run the following commands
```
cd ~/catkin_ws/src/localize_sound
python3 run_wakeword.py
```
Lastly, in another terminal we will run the ROS service which will
```
cd ~/catkin_ws/
source devel/setup.bash
rosrun localize_sound angle_server.py
```

In the final terminal, you will see the output for the angle of the wakeword when the word has been called.
