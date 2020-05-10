#! /usr/bin/env python 
import rospy          # python client library for ROS
import time           # python timing (not normal for ROS)
import actionlib      # for actions
from violet_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback   # message types needed

def the_feedback_cb(feedback):                 # callback function
	print('[Feedback] Time elapsed %f' % 
		(feedback.time_elapsed.to_sec()))      # print time elapsed (in seconds)
	print('[Feedback] Time remaining: %f' % 
		(feedback.time_remaining.to_sec()))    # print time remaining (in seconds)

rospy.init_node('timer_action_client')         # initialize client node
client = actionlib.SimpleActionClient(         # register client
	'timer',        # server name
	TimerAction     # action message type
)

client.wait_for_server()          # wait for action server
goal = TimerGoal()                # create goal object
goal.time_to_wait = rospy.Duration.from_sec(5)      # set field

# to test server abort:
# goal.time_to_wait = rospy.Duration.from_sec(500.0)    # any number over 60

client.send_goal(goal, feedback_cb=the_feedback_cb)   # send goal

# to test goal preemption by user:
# time.sleep(3.0)
# client.cancel_goal()

client.wait_for_result()          # wait for action server to finish

# print results:
print('[Result] State: %d' % (client.get_state()))              # number of final state
print('[Result] Status: %s' % (client.get_goal_status_text()))  # final status (success, failure, etc.)
if client.get_result():                                 # if results exist
	print('[Result] Time elapsed: %f' % 
		(client.get_result().time_elapsed.to_sec()))    # print time elapsed (in seconds)
	print('[Result] Updates sent: %d' % 
		(client.get_result().updates_sent))             # print number of updates sent




