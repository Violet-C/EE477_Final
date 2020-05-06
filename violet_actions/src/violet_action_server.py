#! /usr/bin/env python 
import rospy
import time           # python timing (not normal for ROS)
import actionlib      # for actions
from violet_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback

def do_timer(goal):   # action function
	start_time = time.time()
	update_count = 0

	if goal.time_to_wait.to_sec() > 60.0:      # stops after 60 seconds 
		result = TimerResult()
		result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
		result.updates_sent = update_count
		server.set_aborted(result, "Aborted - too long to wait!")
		return

	while (time.time() - start_time) < goal.time_to_wait.to_sec():
		# goes until time to wait is over

		if   server.is_preempt_requested():    # stops if preempted by user
			result = TimerResult()
			result.time_elapsed = rospy.Duration.from_sec(
				time.time() - start_time)
			result.updates_sent = update_count
			server.set_preempted(result, "Timer preempted")
			return

		feedback = TimerFeedback()
		feedback.time_elapsed = rospy.Duration.from_sec(time.time()- start_time)
		feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed
		server.publish_feedback(feedback)
		update_count += 1
		time.sleep(1.0)
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
	result.updates_sent = update_count
	server.set_succeeded(result, "Timer completed successfully")

rospy.init_node('timer_action_server')         # initialize server node
server = actionlib.SimpleActionServer(         # register server
	'timer',                # name of server
	TimerAction,            # action message type
	do_timer,               # timer action function
	False                   # always set to False
	)                  

server.start()
rospy.spin()