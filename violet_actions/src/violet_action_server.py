#! /usr/bin/env python 
import rospy          # python client library for ROS
import time           # python timing (not normal for ROS)
import actionlib      # for actions
from violet_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback   # message types needed

def do_timer(goal):            # action function
	start_time = time.time()   # get time at start
	update_count = 0           # to count number of updates sent

	if goal.time_to_wait.to_sec() > 60.0:      # stop if input time is oover 60 seconds
		result = TimerResult()                                     # create result object
		result.time_elapsed = rospy.Duration.from_sec(
			time.time() - start_time)                              # calculate time elapsed
		result.updates_sent = update_count                         # number of updates sent
		server.set_aborted(result, "Aborted - too long to wait!")  # error message
		return

	while (time.time() - start_time) < goal.time_to_wait.to_sec():
		# go until time to wait is over

		if   server.is_preempt_requested():    # stop if preempted by user
			result = TimerResult()                                 # create result object
			result.time_elapsed = rospy.Duration.from_sec(
				time.time() - start_time)                          # calculate time elapsed
			result.updates_sent = update_count                     # number of updates sent
			server.set_preempted(result, "Timer preempted")        # error message
			return

		feedback = TimerFeedback()             # create feedback object
		feedback.time_elapsed = rospy.Duration.from_sec(
			time.time()- start_time)           # calculate time elapsed (in seconds)
		feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed # calculate time remaining (in seconds)
		server.publish_feedback(feedback)      # publish feedback
		update_count += 1                      # add one to count of updates sent
		time.sleep(1.0)                        # wait for 1 second
	result = TimerResult()                     # create result object
	result.time_elapsed = rospy.Duration.from_sec(
		time.time() - start_time)              # calculate time elapsed (in seconds)
	result.updates_sent = update_count         # final number of updates sent
	server.set_succeeded(result, "Timer completed successfully")   # success message

rospy.init_node('timer_action_server')         # initialize server node
server = actionlib.SimpleActionServer(         # register server
	'timer',                # name of server
	TimerAction,            # action message type
	do_timer,               # timer action function
	False                   # always set to False
	)                  

server.start()              # start action
rospy.spin()                # wait for requests