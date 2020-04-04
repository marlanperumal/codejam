from itertools import permutations

traces = {}
for N in range(2, 6):
    traces[N] = {}
    row = list(range(N))
    perms = [p for p in permutations(row, N)]
    base_grid = []
    for n in range(N):
        base_grid.append([(j - n) % N for j in range(N)])

    for p1 in perms:
        p2 = row
        for p3 in perms:
            grid = [[base_grid[i][j] for i in p1] for j in p2]
            trace = sum([p3[grid[i][i]] for i in range(N)]) + N
            if trace not in traces[N]:
                traces[N][trace] = [
                    [p3[grid[i][j]] + 1 for i in range(N)]
                    for j in range(N)
                ]


def run(N, K):
    if K not in traces[N]:
        return "IMPOSSIBLE", None
    else:
        return "POSSIBLE", traces[N][K]


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, K = [int(i) for i in input().split()]
        result, grid = run(N, K)
        print("Case #{}: {}".format(t, result))
        if result == "POSSIBLE":
            for row in grid:
                print(" ".join([str(i) for i in row]))
