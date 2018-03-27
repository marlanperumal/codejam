# Bathroom stall theory
# - The exact stall chosen is less important than the gap in which it sits
# - The next stall chosen will always be in the largest available gap g
# - If the gap is odd, the chosen stall will be exactly in the middle
#   creating new gaps of size (g-1)/2
# - If the gap is even, the chosen stall will be one of the the two middle
#   creating new gaps of size g/2 and g/2 + 1
# - Our method will involve storing the list of available gaps, then when we
#   choose it, remove it from the list and replace it with the two new gaps
# - Since the new gaps will be guaranteed to be smaller, if there are mulitple
#   gaps of the largest size we can deal with them all simultaneously

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
