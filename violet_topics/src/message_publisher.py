#!/usr/bin/env python    
import rospy                           # python client library for ROS
from violet_topics.msg import Complex  # custom message type
from random import random              # to generate rand. #s

rospy.init_node('message_publisher')   # initialize node

pub = rospy.Publisher(                 # register topic
	'complex',                         # name topic
	Complex,                           # type of message
	queue_size=3                       # set queue size (similar to buffer)
)

rate = rospy.Rate(2)                   # set rate to 2 Hz

while not rospy.is_shutdown():         # loop until stopped by user
	msg = Complex()                    # declare message type
	msg.real = random()                # assign random value
	msg.imaginary = random()           # assign random value

	pub.publish(msg)                   # publish
	rate.sleep()                       # pause to keep rate