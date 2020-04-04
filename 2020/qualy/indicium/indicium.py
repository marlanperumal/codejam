def run(N, K):
    if K % N != 0:
        return "IMPOSSIBLE", None

    i = K // N
    grid = []
    for n in range(N):
        grid.append([(j + i - n - 1) % N + 1 for j in range(N)])
    return "POSSIBLE", grid


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, K = [int(i) for i in input().split()]
        result, grid = run(N, K)
        print("Case #{}: {}".format(t, result))
        if result == "POSSIBLE":
            for row in grid:
                print(" ".join([str(i) for i in row]))
