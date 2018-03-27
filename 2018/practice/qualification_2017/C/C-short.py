from collections import defaultdict
T = int(input())
for t in range(1, T+1):
    n, k = [int(n) for n in input().split(" ")]
    gaps = defaultdict(int)
    gaps[n] += 1
    while k > 0:
        g = max(gaps.keys())
        m = gaps[g]
        g1 = (g-1)//2
        g2 = g1 if g % 2 == 1 else g1 + 1
        gaps[g1] += m
        gaps[g2] += m
        k -= m
        del gaps[g]
    print("Case #{}: {} {}".format(t, g1, g2))
