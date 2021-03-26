from math import factorial


def run(N, C):
    if C < N - 1:
        return "IMPOSSIBLE"
    if C >= N * (N + 1) / 2:
        return "IMPOSSIBLE"

    R = [1] * (N - 1)
    C -= N - 1
    for i, c in enumerate(range(N - 1, 0, -1)):
        r = min(C, c)
        C -= r
        R[i] += r
        if C == 0:
            break

    L = list(range(1, N + 1))
    for k, r in enumerate(reversed(R)):
        i = N - k - 2
        j = r - 1
        L = L[:i] + list(reversed(L[i:i + j + 1])) + L[i + j + 1:]

    return " ".join([str(l) for l in L])


T = int(input())

for t in range(1, T + 1):
    N, C = [int(i) for i in input().split()]

    result = run(N, C)
    print(f"Case #{t}: {result}")
