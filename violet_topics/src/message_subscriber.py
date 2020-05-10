#!/usr/bin/env python 
import rospy                             # python client library for ROS
from violet_topics.msg import Complex    # custom message type

def callback(msg):                       # callback function
	print 'Real:', msg.real              # print real part of complex number
	print 'Imaginary:', msg.imaginary    # print imaginary part of complex number
	print                                # blank line

rospy.init_node('message_subscriber')    # initialize node

sub = rospy.Subscriber(                  # register subscriber
	'complex',                           # topic name
	Complex,                             # message type
	callback                             # callback function
)

rospy.spin()  # keep node running until shut down
