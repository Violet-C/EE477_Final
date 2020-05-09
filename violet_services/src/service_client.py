#!/usr/bin/env python
import rospy
from violet_services.srv import WordCount
import sys

rospy.init_node('service_client')
rospy.wait_for_service('word_count')  # wait for registration

word_counter = rospy.ServiceProxy(    # set up proxy
	'word_count',                     # service name
	WordCount                         # service type
)


valid_words = [k for k in sys.argv[1:] if '__' not in k]
parsed_words = ' '.join(valid_words)        # parse arguments
word_count = word_counter(parsed_words)      # use service

print(parsed_words+' --> has '+str(word_count.count)+' words')