from math import ceil
from bisect import bisect_left

def find_next(x, roundups):
    i = bisect_left(roundups, x)
    return roundups[i] - x if roundups[i] - x > 0 else roundups[0]


T = int(input())
for t in range(1, T+1):
    N, L = [int(si) for si in input().split()]
    C = [int(ci) for ci in input().split()]
    used = sum(C)
    leftover = N - used
    roundups = []
    total = sum([round(ci/N*100) for ci in C])
    for n in range(N+1):
        if round(n/N*100)-(n/N*100) > 0:
            roundups.append(n)
    if len(roundups) == 0:
        total = 100
    else:
        to_next = sorted([find_next(ci, roundups) for ci in C])
        while leftover >= min(to_next[0], roundups[0]):
            total += ceil(to_next[0]/N*100)
            used += to_next[0]
            leftover = N - used
            to_next.pop(0)
            to_next.append(roundups[0])
        total += round(leftover/N*100)
    print("Case #{}: {}".format(t, total))
