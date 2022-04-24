from random import randint
T = int(input())

for t in range(T):
    N, K = [int(i) for i in input().split()]
    r, p = [int(i) for i in input().split()]
    visited = set([r])
    passages = p

    for k in range(min(K, N - 1)):
        while r in visited:
            r = randint(1, N)
        print(f"T {r}")

        r, p = [int(i) for i in input().split()]
        passages += p
        visited.add(r)

    result = round(passages / 2 * N / min(K, N))
    print(f"E {result}")
