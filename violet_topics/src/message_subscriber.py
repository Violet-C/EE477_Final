#!/usr/bin/env python
import rospy
from violet_topics.msg import Complex

def callback(msg):
	print 'Real:', msg.real
	print 'Imaginary:', msg.imaginary
	print                                # blank line

rospy.init_node('message_subscriber')    # initialize node

sub = rospy.Subscriber(                  # register subscriber
	'complex',                           # topic name
	Complex,                             # message type
	callback                             # callback function
)

rospy.spin()  # keeps node running until shut down
