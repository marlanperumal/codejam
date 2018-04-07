import numpy as np

def rotz(x, theta):
    rot = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return rot.dot(x).T

def rotx(x, phi):
    rot = np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi), np.cos(phi)],
    ])
    return rot.dot(x).T

def proj_area(cube, plane):
    a_vec = cube.dot(plane)
    return np.linalg.norm(a_vec, ord=1)

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
    return x1

T = int(input())
for t in range(1, T+1):
    A = float(input())
    plane = np.array([0,1,0])
    cube = np.array([[1,0,0],[0,1,0],[0,0,1]])
    psi = np.arccos(np.sqrt(2)/np.sqrt(3))

    if A == 1:
        rot_cube = cube
    elif A < np.sqrt(2):
        theta = bisect(lambda x: proj_area(rotz(cube, x), plane) - A, 0, -np.pi/4)
        rot_cube = rotz(cube, theta)
    elif A == np.sqrt(2):
        rot_cube = rotz(cube, -np.pi/4)
    elif A < np.sqrt(3):
        cube = rotz(cube, -np.pi/4)
        phi = bisect(lambda x: proj_area(rotx(cube, x), plane) - A, 0, -psi)
        rot_cube = rotx(cube, phi)
    elif A == np.sqrt(3):
        cube = rotz(cube, -np.pi/4)
        rot_cube = rotx(cube, -psi)

    print("Case #{}".format(t))
    print_matrix(rot_cube/2)