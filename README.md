# ROS2 Based Intelligent Vision Robot
 ![alt text](https://github.com/noshluk2/ROS2-Raspberry-PI-Intelligent-Vision-Robot/blob/main/images/r2_rpi.png)
- **[[Get course Here]](https://www.udemy.com/course/draft/2265374/?couponCode=MAY_LEARN)**
----

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Link-to-the-Course">Link to the Course</a></li>
    <li><a href="#Commands">Link to the Course</a></li>
    <li><a href="#Notes">Notes</a></li>
    <li><a href="#Instructors">Instructors</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>


## About this Repository
This repository is for a mobile robot which is a **2 wheel differential drive with a caster** . We will First build the robot using *3D printed parts*. All electronics is going to be explained for proper connections .

**Raspberry Pi 4** is going to be main brain for this robot . *ROS2 foxy and humble* both are going to be utilized using this course . WiFi Communication between laptop and Raspberry Pi will be done .

We will look into image data transmission  and **bandwidth optimization** for our computer vision based projects . 



----
## Using this Repository
* Move into your workspace/src folder
 ```
 cd path/to/ros2_ws/src/
##e.g cd ~/ros2_ws/src/
  ```
* Clone the repository in your workspace
```
git clone https://github.com/noshluk2/ROS2-Raspberry-PI-Intelligent-Vision-Robot
```


* Perform make and build through colcon
 ```
 cd /path/to/workspace_root/
 ##e.g ~/ros2_ws_ws/
 colcon build
 ```

* Source your Workspace in any terminal you open to Run files from this workspace ( which is a basic thing of ROS )
```
source /path/to/ros2_ws/install/setup.bash
```
- (Optional for Power USERs only) Add source to this workspace into bash file
 ```
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
 ```
  **NOTE:** This upper command is going to add the source file path into your ~/.bashrc file ( Only perform it once and you know what you are doing).This will save your time when running things from the Workspace

---
## Features
* **Robot Controller Driving**
  -  ![alt text](https://github.com/noshluk2/ROS2-Raspberry-PI-Intelligent-Vision-Robot/blob/main/images/controller_drive.gif)
* **Maze Solving through QR with Opencv**
  -  ![alt text](https://github.com/noshluk2/ROS2-Raspberry-PI-Intelligent-Vision-Robot/blob/main/images/qr_maze.gif)
* **Line Following Robot using Computer Vision**
  -  ![alt text](https://github.com/noshluk2/ROS2-Raspberry-PI-Intelligent-Vision-Robot/blob/main/images/line_following.gif)
* **Surveillance based on AI robot**
  -  ![alt text](https://github.com/noshluk2/ROS2-Raspberry-PI-Intelligent-Vision-Robot/blob/main/images/ai_bot.gif)

----
## Pre-Course Requirments

**Software**
- Ubuntu 22.04
- Opencv 4
- TensorFlow 2
- ROS 2
- Motivated mind for a huge programming Project :)

**Hardware**

- Raspberrypi 4
- Two Geared Dc motors 12V
- 12V lipo Battery
- 3D print parts provided
- Power Bank
- Jumper Wires
- L298D motor Driver
---
## Link to the Course
Below is a discounted coupon for people who want to take the course in which more explaination to this code has been added

**[[Get course Here]](https://www.udemy.com/course/draft/2265374/?couponCode=MAY_LEARN)**

----
## Commands
- export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
---
## Instructors

Muhammad Luqman (ROS Simulation and Control Systems) - [Profile Link](https://www.linkedin.com/in/muhammad-luqman-9b227a11b/)

----
## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.
