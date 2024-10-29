T = int(input())

for t in range(1, T + 1):
    N, P = [int(i) for i in input().split()]
    X = [[int(i) for i in input().split()] for n in range(N)]
    X1 = [[min(x), max(x)] for x in X]

    pumps = 0
    lx = 0
    rx = 0
    lp = 0
    rp = 0

    for x in X1:
        if x[0] >= rx:
            rx1 = x[1] - rx
        else:
            rx1 = rx - x[0] + x[1] - x[0]
        if x[1] <= lx:
            lx1 = lx - x[0]
        else:
            lx1 = x[1] - lx + x[1] - x[0]
        if x[0] >= lx:
            rx2 = x[1] - lx
        else:
            rx2 = lx - x[0] + x[1] - x[0]
        if x[1] <= rx:
            lx2 = rx - x[0]
        else:
            lx2 = x[1] - rx + x[1] - x[0]
        lp, rp = min(lp + lx1, rp + lx2), min(rp + rx1, lp + rx2)
        lx = x[0]
        rx = x[1]
    result = min(lp, rp)
    print(f"Case #{t}: {result}")
