# %%
from itertools import permutations

# %%
ticks_per_rev = int(1e9 * 60 * 60 * 12)
ticks_per_hour = ticks_per_rev / 12
ticks_per_min = ticks_per_rev / 60
ticks_per_sec = ticks_per_rev / 60


# %%
def run(A, B, C):
    # offset = min(A, B, C)
    # A, B, C = A - offset, B - offset, C - offset
    for h, m, s in permutations([A, B, C]):
        h, m, s = h - s, m - s, s - s
        for i in range(60):
            offset = i * ticks_per_sec
            if ((m - offset) % ticks_per_rev) / 12 == (h - offset) % ticks_per_hour and ((s - offset) % ticks_per_rev) / 60 == (m - offset) % ticks_per_min:
                hh = int((h - offset) // ticks_per_hour) % 12
                mm = int((m - offset) // ticks_per_min) % 60
                ss = int((s - offset) // ticks_per_sec) % 60
                nn = 0
                return [hh, mm, ss, nn]
    return [None, None, None, None]


# %%
T = int(input())

# %%
for t in range(1, T + 1):
    A, B, C = [int(i) for i in input().split()]
    h, m, s, n = run(A, B, C)
    print(f"Case #{t}: {h} {m} {s} {n}")
