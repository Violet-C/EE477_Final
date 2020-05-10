#!/usr/bin/env python
import rospy                         # python client library for ROS
from std_msgs.msg import Int32       # standard int

def callback(msg):                   # callback function for receiving messages
	print(msg.data)                  # print message to Terminal

rospy.init_node('topic_subscriber')  # initialize node

sub = rospy.Subscriber('counter', Int32, callback)  # subscribe

rospy.spin()                         # wait for messages until node is shut down