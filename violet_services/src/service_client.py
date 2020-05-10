#!/usr/bin/env python
import rospy                                   # python client library for ROS
from violet_services.srv import WordCount      # needed message type
import sys                                     # python functions, methods, etc.

rospy.init_node('service_client')     # initialize client node
rospy.wait_for_service('word_count')  # wait for registration

word_counter = rospy.ServiceProxy(    # set up proxy
	'word_count',                     # service name
	WordCount                         # service type
)


valid_words = [k for k in sys.argv[1:] if '__' not in k]    # filter out non-valid strings
parsed_words = ' '.join(valid_words)                        # parse arguments (put in correct form)
word_count = word_counter(parsed_words)                     # use service to count word

print(parsed_words+' --> has '+str(word_count.count)+' words')  # print input words and count