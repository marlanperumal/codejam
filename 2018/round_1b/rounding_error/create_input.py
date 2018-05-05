from random import randint
from collections import defaultdict
T = 100
max_N = 25
print(T)
for t in range(T):
    N = randint(2, max_N)
    R = randint(1, N)
    C = defaultdict(int)
    for r in range(R):
        C[randint(0, N)] += 1
    L = len(C)
    print(N, L)
    print(" ".join([str(ci) for ci in C.values()]))
