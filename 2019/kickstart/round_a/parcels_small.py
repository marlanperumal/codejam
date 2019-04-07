from itertools import chain

def flatten(grid):
    return list(chain.from_iterable(grid))

def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

T = int(input())

for t in range(1, T + 1):
    R, C  = [int(i) for i in input().split()]
    grid = [[int(j) for j in input()] for i in range(R)]
    min_grid = [[R + C for j in range(C)] for i in range(R)]

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                new_grid = [[manhattan([i, j], [i2, j2]) for j2 in range(C)] for i2 in range(R)]
                for i2 in range(R):
                    for j2 in range(C):
                        if new_grid[i2][j2] < min_grid[i2][j2]:
                            min_grid[i2][j2] = new_grid[i2][j2]

    max_distance = max(flatten(min_grid))

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                new_min_grid = [[0 for j in range(C)] for i in range(R)]
                new_grid = [[manhattan([i, j], [i2, j2]) for j2 in range(C)] for i2 in range(R)]
                for i2 in range(R):
                    for j2 in range(C):
                        new_min_grid[i2][j2] = min((new_grid[i2][j2], min_grid[i2][j2]))
                new_max_distance = max(flatten(new_min_grid))
                max_distance = min(max_distance, new_max_distance)

    print("Case #{}: {}".format(t, max_distance))