T = int(input())

for t in range(1, T + 1):
    N, K = [int(i) for i in input().split()]
    E = [int(i) for i in input().split()]
    s0 = sum(E)
    s1 = s0**2
    s2 = sum([e**2 for e in E])
    if s0 == 0 and s1 == s2:
        result = 0
    else:
        X = []
        k = 0
        while s1 != s2 and k > 0 and k < K:
            if s0 == 0:
                x = 1
            else:
                x = (s2 - s1) // (2 * s0)
            X.append(x)
            s0 += x
            s1 = s0**2
            s2 += x**2
            k += 1
    if s1 == s2 and k <= k:
        if len(X) == 0:
            result = 0
        else:
            result = " ".join([str(x) for x in X])
    else:
        result = "IMPOSSIBLE"
    print(f"Case #{t}: {result}")
