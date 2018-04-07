from math import sin, cos, sqrt, pi
s2 = sqrt(2)
p2 = pi/2
p4 = pi/4
T = int(input())
for t in range(1, T+1):
    A = float(input())
    theta = 0
    f = s2*sin(theta + p4) - A
    delta = 1
    while delta > 1e-12:
        delta = - f/(s2*cos(theta + p4))
        theta = theta + delta
        f = sqrt(2)*sin(theta + p4) - A
    x = cos(theta)/2
    y = sin(theta)/2
    print("Case #{}:".format(t))
    print(cos(theta)/2, sin(theta)/2, 0)
    print(cos(theta + p2)/2, sin(theta + p2)/2, 0)
    print(0, 0, 0.5)
