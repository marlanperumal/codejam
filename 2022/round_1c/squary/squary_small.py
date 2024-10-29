T = int(input())

for t in range(1, T + 1):
    N, K = [int(i) for i in input().split()]
    E = [int(i) for i in input().split()]
    s0 = sum(E)
    s1 = s0**2
    s2 = sum([e**2 for e in E])
    if s0 == 0:
        if s2 - s1 != 0:
            result = "IMPOSSIBLE"
        else:
            result = 0
    else:
        x = (s2 - s1) // (2 * s0)
        if x * (2 * s0) == (s2 - s1):
            result = int(x)
        else:
            result = "IMPOSSIBLE"
    print(f"Case #{t}: {result}")