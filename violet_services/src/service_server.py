#!/usr/bin/env python
import rospy                                                    # python client library for ROS                   
from violet_services.srv import WordCount, WordCountResponse    # message types needed

def count_words(request):              # function to serve
	return len(request.words.split())  # number of words

rospy.init_node('service_server')      # initialize server node

service = rospy.Service(  # register service
	'word_count',         # service name
	WordCount,            # service type
	count_words           # function service provides
)

rospy.spin()              # wait for requests