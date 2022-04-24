T = int(input())

for t in range(1, T + 1):
    N = int(input())
    S = [int(i) for i in input().split()]
    i = 0
    for s in sorted(S):
        if s >= i + 1:
            i += 1
    print(f"Case #{t}: {i}")