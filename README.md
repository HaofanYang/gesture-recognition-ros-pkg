### Hand Gesture Recognition

#### Dependencies Overview
* OpenCV
* ROS Kinetic (Python 2.7 is required)
* A Camera connected to your device

#### How to Run
1. Copy this package into your workspace and run `catkin_make`.

2. Simply Run `roslaunch gesture_teleop teleop.launch`. A window showing real time video from your laptop webcam will be activated. Place your hand into the region of interest (the green box) and your robot will take actions based on the number of fingers you show.
	1. Two fingers: Drive forward
	2. Three fingers: Turn left
	3. Four fingers: Turn right
	4. Other: Stop 

![f5](/images/1.png)

![f4](/images/2.png)

![f3](/images/3.png)

![f2](/images/4.png)
