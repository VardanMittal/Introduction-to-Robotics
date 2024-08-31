#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import math

def publish_joint_angles():
    # Initialize the ROS node
    rospy.init_node('gazebo_controller', anonymous=True)
    
    # Create a publisher for the /joint_states topic
    joint_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    
    # Set the rate at which to publish
    rate = rospy.Rate(10)  # 10 Hz
    
    # Initialize the JointState message
    joint_state = JointState()
    joint_state.header = Header()
    joint_state.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4']
    joint_state.position = [0.0, 0.0, 0.0, 0.0]

    while not rospy.is_shutdown():
        # Update the joint angles here
        joint_state.header.stamp = rospy.Time.now()
        joint_state.position[0] = math.sin(rospy.get_time())  # Example of dynamic angle for joint_1
        joint_state.position[1] = math.sin(rospy.get_time() + 1.0)  # Example for joint_2
        joint_state.position[2] = math.sin(rospy.get_time() + 2.0)  # Example for joint_3
        
        # Publish the joint states
        joint_pub.publish(joint_state)
        
        # Sleep to maintain the desired rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_angles()
    except rospy.ROSInterruptException:
        pass
