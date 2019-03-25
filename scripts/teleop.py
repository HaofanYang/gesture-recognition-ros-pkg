#!/usr/bin/env python

import rospy
#!/usr/bin/env python

from geometry_msgs.msg import Twist
from std_msgs.msg import String

fingers = 0
def callback(data):
	global fingers
	fingers = data.data

rospy.init_node('teleop')
rospy.Subscriber("num_of_fingers", String, callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(20)


while not rospy.is_shutdown():
	twist = Twist()
	if fingers == '2':
		twist.linear.x = 0.6
		rospy.loginfo("driving forward")
	elif fingers == '3':
		twist.angular.z = 1
		rospy.loginfo("turning left")
	elif fingers =='4':
		twist.angular.z = 1
		rospy.loginfo("turning right")
	else:
		rospy.loginfo("stoped")
	cmd_vel_pub.publish(twist)
	rate.sleep()
