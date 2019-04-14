from functools import reduce
from sys import stdout


num_holes = 18
D = [4, 3, 5, 7, 11, 13, 17]
M = reduce(lambda x, y: x*y, D, 1)
B = [int(M/d) for d in D]
A = []
for d, b in zip(D, B):
    for a in range(1, d):
        if a*b % d == 1:
            A.append(a)
            break

T, N, Mi = [int(i) for i in input().split()]

for t in range(1, T + 1):
    Y = []
    for d in D:
        print(" ".join([str(d)]*num_holes))
        stdout.flush()
        response = input()
        if response == "-1":
            exit()
        W = [int(i) for i in response.split()]
        y = sum(W) % d
        Y.append(y)
    x = sum([a*b*y for a, b, y in zip(A, B, Y)])
    print(x % M)
    stdout.flush()
    correct = int(input())
    if correct == -1:
        exit()
