import numpy as np
import matplotlib.pyplot as plt
def fwdKinematicsSolver(q1,q2, l1,l2):
    x = l1 * np.cos(q1) + l2 * np.cos(q2)
    y = l1 * np.sin(q1) + l2 * np.sin(q2)

    return (x,y)

def invKinematicsSolver(x,y, l1, l2):
    """This function solves inverse kinematics for 2R manipulator
    Keyword arguments:
    x,y : coordinates of end effector
    Return: returns a list of 2 possible combinations of joint angles
    """
    D = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    
    D = np.clip(D, -1.0, 1.0)  # Clamping D to be within [-1, 1]
    val = np.arccos(D)
    # print(val)
    thetas = [val, -val]
    joint_angles = []
    for theta in thetas:
        q1 = np.arctan2(y, x) - np.arctan2(l2*np.sin(theta), (l1 + l2*np.cos(theta)))
        q2 = theta + q1
        joint_angles.append((q1,q2))
    return joint_angles[0]

def trajectory(x,y):
    ee_traj = []
    for x_target,y_target in zip(x,y):
        solution = invKinematicsSolver(x_target, y_target, 4.0, 3.0)
        # print(solution)
        """We have two sets of variables -ve theta and +ve theta as the path traced using both of them going to overlap we are only considering +ve theta results..."""
        q1 = solution[0]
        q2 = solution[1]
        x_ee, y_ee = fwdKinematicsSolver(q1,q2, 4.0, 3.0)

        ee_traj.append([x_ee, y_ee])

    ee_traj = np.array(ee_traj)
    return ee_traj

def plot_traj(x,y, ee_traj):
    plt.figure()
    plt.plot(x, y, 'r--', label='Desired trajectory')
    plt.plot(ee_traj[:,0], ee_traj[:,1], 'g-', label='traced trajectory', alpha=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Trajactory Plotting')
    plt.show()