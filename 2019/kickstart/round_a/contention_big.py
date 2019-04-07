from itertools import chain
from collections import defaultdict

def flatten(grid):
    return list(chain.from_iterable(grid))

T = int(input())

for t in range(1, T + 1):
    N, Q = [int(i) for i in input().split()]
    bookings = [[int(i) for i in input().split()] for q in range(Q)]
    breakpoints = sorted(list(set(flatten(bookings))))
    intervals = [(breakpoints[i], breakpoints[i+1] - 1) for i in range(len(breakpoints) - 1)] + [(breakpoints[-1], breakpoints[-1])]

    contention = defaultdict(int)
    for L, R in bookings:
        for L1, R1 in intervals:
            if L1 >= L and R1 <= R:
                contention[(L1, R1)] += 1
    free_bookings = []

    for q in range(Q):
        max_free = 0
        max_pos = 0
        uncontended_intervals = set([interval for interval in contention if contention[interval] == 1])
        for i, [L, R] in enumerate(bookings):
            num_free = 0
            for L1, R1 in uncontended_intervals:
                if L1 >= L and R1 <= R:
                    num_free += R1 - L1 + 1
            if num_free > max_free:
                max_free = num_free
                max_pos = i
        free_bookings.append(max_free)
        if max_free == 0:
            break
        L, R = bookings.pop(i)
        for L1, R1 in intervals:
            if L1 >= L and R1 <= R:
                contention[(L1, R1)] -= 1

    print("Case #{}: {}".format(t, min(free_bookings)))
