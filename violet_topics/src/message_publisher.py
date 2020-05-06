#!/usr/bin/env python
import rospy
from violet_topics.msg import Complex  # Custom message type
from random import random              # to generate rand. #s

rospy.init_node('message_publisher')   # initialize node

pub = rospy.Publisher(                 # register topic
	'complex',                          # name topic
	Complex,                            # type of message
	queue_size=3
)

rate = rospy.Rate(2)                   # set rate to 2 Hz

while not rospy.is_shutdown():
	msg = Complex()                    # declare message type
	msg.real = random()                # assign values
	msg.imaginary = random()

	pub.publish(msg)                   # publish
	rate.sleep()                       # pause to keep rate