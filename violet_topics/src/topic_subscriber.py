#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):   # callback function for receiving messages
	print(msg.data)  # prints to Terminal

rospy.init_node('topic_subscriber')# initialize node

sub = rospy.Subscriber('counter', Int32, callback)# subscribe

rospy.spin()         # waits for node to be shut down