def run(N, L):
    cost = 0
    for i in range(len(L) - 1):
        sublist = L[i:]
        minl = min(sublist)
        j = sublist.index(minl)
        cost += j + 1
        L = L[:i] + list(reversed(L[i:i + j + 1])) + L[i + j + 1:]
    return cost


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    L = [int(i) for i in input().split()]

    result = run(N, L)
    print(f"Case #{t}: {result}")
