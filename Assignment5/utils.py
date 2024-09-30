import numpy as np

c = lambda angle: np.round(np.cos(angle),2)
s = lambda angle: np.round(np.sin(angle),2)


def DH_matrix(theta,alpha,a,d):
    mat = []
    for i in range(len(theta)):
        mat.append([theta[i], alpha[i], a[i],d[i]])
    return np.array(mat)

def T(dh):
    theta, alpha, a, d = dh
    return np.array([
        [c(theta), -s(theta)*c(alpha),s(theta)*s(alpha), a*c(theta)],
        [s(theta), c(theta)*c(alpha), -c(theta)*s(alpha), a*s(theta)],
        [0, s(alpha), c(alpha), d],
        [0, 0, 0, 1]
    ])

def Tr(dh_params):
    T_matrices = []
    T_total = np.eye(4)
    for dh in dh_params:
        T_i = T(dh)
        T_total = T_total @ T_i
        T_matrices.append(T_total)
    return T_matrices

def Jacobian(dh_params):
    n = len(dh_params)
    T_matrices = Tr(dh_params)
    
    J = np.zeros((6, n))
    
    for i in range(n):
        T_i = T_matrices[i]
        R_i = T_i[:3, :3]
        p_i = T_i[:3, 3]
        
        if i == 0:
            z_prev = np.array([0, 0, 1])
            p_prev = np.array([0, 0, 0])
        else:
            T_prev = T_matrices[i-1]
            z_prev = T_prev[:3, 2]
            p_prev = T_prev[:3, 3]
        
        J[:3, i] = np.cross(z_prev, (p_i - p_prev))
        J[3:, i] = z_prev
    return J