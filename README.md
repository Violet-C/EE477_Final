# EE477_Final
This is the final project for ME477 at Saint Martin's University.  All .py files are modeled after the corresponding files in the [robotics_book_code](https://github.com/ricopicone/robotics-book-code) repository by ricopicone.

## Requirements

This repository was created for use with ROS Melodic Morenia and Ubuntu 18.04.4 (Bionic Beaver).

## Installation and configuration

1. After installing ROS and creating a workspace, fork the repository [EE477_Final](https://github.com/Violet-C/EE477_Final) on Github.

2. Clone the repository using the following command:
```bash
git clone https://github.com/Violet-C/EE477_Final
```
3. Build the workspace using:
```bash
catkin_make
```
4. Source the workspace using:
```bash
source devel/setup.bash
```
5. Update using `git` as desired.



# ROS package: |violet_topics|

This package has two pairs of a publisher node and a subscriber node.  One uses a custom message type to generate random complex numbers and print their real and imaginary parts to the screen.  The other prints out consecutive integers starting at 1.  Both will continue to run until ended by the user ('CTRL'+'C').

## Getting started

The nodes which produce random complex numbers can be started individually using:
```bash
roscore
```

```bash
rosrun violet_topics message_publisher.py
```

```bash
rosrun violet_topics message_subscriber.py
```

or by using the included launch file:
```bash
roslaunch violet_topics violet_message.launch
```

Similarly, the nodes which produce consecutive integers can be started individually using:
```bash
roscore
```

```bash
rosrun violet_topics topic_publisher.py
```

```bash
rosrun violet_topics topic_subscriber.py
```

or by using the included launch file:
```bash
roslaunch violet_topics violet_topic.launch
```

## Usage

Both pairs of nodes can be run at the same time.  The message publisher and subscriber use the topic 'complex', and the topic publisher and subscriber use the topic 'counter'.



# ROS package: |violet_services|

This package uses a server node and a client node to count the number of words in an input phrase, and prints this number to the screen in the form 'This is an input of 7 words --> has 7 words'.


## Getting started

The word counter can be started either by starting each node manually:

```bash
roscore
```

```bash
rosrun violet_services service_server.py
```

```bash
rosrun violet_services service_client.py This is an input of 7 words
```

or by using the included launch file:
```bash
roslaunch violet_services violet_service.launch words:="This is an input of 7 words"

```

## Usage

Any words may be used as input for the lauch command, but must always be entered in the form:

```bash
rosrun violet_services service_client.py Input words
```
or
```bash
roslaunch violet_services violet_service.launch words:="Input words"

```



# ROS package: |violet_actions|

This package uses a server node and client node to set a timer for up to 60 seconds.  Each second, the time elapsed and time remaining are printed to the screen.  After the timer finishes, it prints its exit status.  The timer will be exited with an error message if a timer over 60 seconds is requested or if the timer is preempted by the user before it finishes.  Commented code is included in  `violet_action_client.py` to test both of these cases.

## Getting started

The timer can be started either by starting each node manually:

```bash
roscore
```

```bash
rosrun violet_actions violet_action_server.py
```

```bash
rosrun violet_actions violet_action_client.py
```

or by using the included launch file:
```bash
roslaunch violet_actions violet_action.launch
```

## Usage

The timer duration in seconds is set in in `violet_action_client.py` using:
```bash
goal.time_to_wait = rospy.Duration.from_sec(5) 
```
 The example above sets the timer for 5 seconds, and this command can be modified to set a timer for up to 60 seconds.

The timer can be preempted by the user with: 
```bash
client.cancel_goal()
```
which is included as a commented line in `violet_action_client.py`.