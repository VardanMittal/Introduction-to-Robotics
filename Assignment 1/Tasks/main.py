import numpy as np
import matplotlib.pyplot as plt

def invKinematicSolver(x,y):
    """This function solves inverse kinematics for 2R manipulator
    Keyword arguments:
    x,y : coordinates of end effector
    Return: returns a list of 2 possible combinations of joint angles
    """
    l1 = 4
    l2 = 3.5
    if x > 7.5 or y > 7.5:
        return
    val = np.arccos(
            (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
    thetas = [val, -val]
    joint_angles = []
    for theta in thetas:
        q1 = np.arctan2(x, y) - np.arctan2(l2*np.sin(theta), (l1 + l2*np.cos(theta)))
        q2 = theta + q1
        joint_angles.append((q1,q2))
    return joint_angles

