# from numpy import sin, cos, sqrt, pi
# s2 = sqrt(2)
# p2 = pi/2
# p4 = pi/4
# T = int(input())
# for t in range(1, T+1):
#     A = float(input())
#     theta = 0
#     f = s2*sin(theta + p4) - A
#     delta = 1
#     while delta > 1e-12:
#         delta = - f/(s2*cos(theta + p4))
#         theta = theta + delta
#         f = sqrt(2)*sin(theta + p4) - A
#     x = cos(theta)/2
#     y = sin(theta)/2
#     print("Case #{}:".format(t))
#     print(cos(theta)/2, sin(theta)/2, 0)
#     print(cos(theta + p2)/2, sin(theta + p2)/2, 0)
#     print(0, 0, 0.5)

import numpy as np
from math import sin, cos, pi, sqrt, acos

def mmult(A, B):
    N = len(A)
    I = len(A[0])
    M = len(B[0])
    ans = [[0]*M for n in range(N)]
    for n in range(N):
        for m in range(M):
            ans[n][m] = sum([A[n][i]*B[i][m] for i in range(I)])
    # print(ans)
    return ans

def transpose(A):
    ans = [list(i) for i in zip(*A)]
    # print(ans)
    return ans

def dot(A, b):
    N = len(A)
    ans = [0]*N
    for n in range(N):
        ans[n] = sum([A[n][i]*b[i] for i in range(N)])
    return ans

def one_norm(b):
    return max([abs(x) for x in b])

def rotz(x, theta):
    rot = [
        [cos(theta), -sin(theta), 0],
        [sin(theta), cos(theta), 0],
        [0, 0, 1]
    ]
    ans = transpose(mmult(rot, x))
    # print(ans)
    return ans

def rotx(x, phi):
    rot = [
        [1, 0, 0],
        [0, cos(phi), -sin(phi)],
        [0, sin(phi), cos(phi)],
    ]
    return transpose(mmult(rot, x))

def proj_area(cube, plane):
    a_vec = dot(cube, plane)
    return one_norm(a_vec)

def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(col) for col in row]))

def bisect(fun, x0, x1):
    fx0 = fun(x0)
    fx1 = fun(x1)

    while abs(fx1) > 1e-12:
        x2 = x1 - fx1*(x1 - x0)/(fx1 - fx0)
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = fun(x1)
        print(x1, fx1)
    return x1

T = int(input())
for t in range(1, T+1):
    A = float(input())
    plane = [0,1,0]
    cube = [[1,0,0],[0,1,0],[0,0,1]]
    psi = acos(sqrt(2)/sqrt(3))

    if A == 1:
        rot_cube = cube
    elif A < sqrt(2):
        theta = bisect(lambda x: proj_area(rotz(cube, x), plane) - A, 0, -pi/4)
        rot_cube = rotz(cube, theta)
    elif A == sqrt(2):
        rot_cube = rotz(cube, -pi/4)
    elif A < sqrt(3):
        cube = rotz(cube, -pi/4)
        phi = bisect(lambda x: proj_area(rotx(cube, x), plane) - A, 0, -psi)
        rot_cube = rotx(cube, phi)
    elif A == sqrt(3):
        cube = rotz(cube, -pi/4)
        rot_cube = rotx(cube, -psi)

    print("Case #{}".format(t))
    print_matrix([[col/2 for col in row] for row in rot_cube])
