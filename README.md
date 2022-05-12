# Hand Raise Detection using Zed Camera

## Prerequisites
#### Hardware
- Zed 2i Stereo Camera
#### Software
- Ubuntu OS
- ROS(Have ROS version based on the Ubuntu Version)
- Zed SDK and its dependencies(Installation instructions can be found [here](https://www.stereolabs.com/developers/release/))

## Running the Package
Place the contents of this branch of the ```src``` folder of the Zed ROS catkin_ws(assumed here as zed_ws). After that run the following commands
```
cd zed_ws
source devel/setup.bash
roslaunch zed_wrapper zed2i.launch
```

In another terminal, run the hand raise detection script
```
cd zed_ws
source devel/setup.bash
rosrun find_raised_hand find_raised_hand 
```
