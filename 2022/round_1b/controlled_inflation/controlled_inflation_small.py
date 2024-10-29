def go_left(pumps, loc, X1, level):
    x11 = X1[level][0]
    x12 = X1[level][1]

    if x12 <= loc:
        pumps += loc - x11
    else:
        pumps += x12 - loc + x12 - x11
    
    if level >= len(X1) - 1:
        return pumps
    
    p1 = go_left(pumps, x11, X1, level + 1)
    p2 = go_right(pumps, x11, X1, level + 1)
    return min(p1, p2)


def go_right(pumps, loc, X1, level):
    x11 = X1[level][0]
    x12 = X1[level][1]

    if x11 >= loc:
        pumps += x12 - loc
    else:
        pumps += loc - x11 + x12 - x11
    
    if level >= len(X1) - 1:
        return pumps
    
    p1 = go_left(pumps, x12, X1, level + 1)
    p2 = go_right(pumps, x12, X1, level + 1)
    return min(p1, p2)


T = int(input())

for t in range(1, T + 1):
    N, P = [int(i) for i in input().split()]
    X = [[int(i) for i in input().split()] for n in range(N)]
    X1 = [[min(x), max(x)] for x in X]

    pumps = 0
    result = go_right(pumps, 0, X1, 0)
    print(f"Case #{t}: {result}")
