# %%
from itertools import permutations

# %%
ticks_per_rev = int(1e9 * 60 * 60 * 12)
ticks_per_hour = ticks_per_rev / 12
ticks_per_min = ticks_per_rev / 60
ticks_per_sec = ticks_per_rev / 60


# %%
def run(A, B, C):
    for h, m, s in permutations([A, B, C]):
        if m / 12 == h % ticks_per_hour and s / 60 == m % ticks_per_min:
            hh = int(h // ticks_per_hour)
            mm = int(m // ticks_per_min)
            ss = int(s // ticks_per_sec)
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
