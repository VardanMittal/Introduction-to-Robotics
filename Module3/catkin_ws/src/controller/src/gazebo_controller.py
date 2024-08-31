#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def publish_joint_angles():
    rospy.init_node('gazebo_controller', anonymous=True)
    
    joint_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

    rate = rospy.Rate(10)
    
    joint_state = JointState()
    joint_state.name = ['gripper', 'joint1', 'joint2', 'joint3', 'joint4']

    joint_state.position = [0.4, 0.4, 0.35, 1.45, 1.0]

    while not rospy.is_shutdown():
        joint_state.header = Header(stamp=rospy.Time.now())
        joint_pub.publish(joint_state)
        rospy.loginfo("Published joint angles: %s", joint_state.position)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_angles()
    except rospy.ROSInterruptException:
        pass
