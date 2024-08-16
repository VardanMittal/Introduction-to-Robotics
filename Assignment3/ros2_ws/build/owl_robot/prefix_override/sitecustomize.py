import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vardan/Introduction-to-Robotics/Assignment3/ros2_ws/install/owl_robot'
