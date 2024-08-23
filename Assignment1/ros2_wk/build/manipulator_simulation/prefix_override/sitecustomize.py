import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vardan/Introduction-to-Robotics/Assignment1/ros2_wk/install/manipulator_simulation'
