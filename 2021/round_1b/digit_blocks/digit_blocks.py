T, N, B, P = [int(i) for i in input().split()]

for t in range(1, T + 1):
    towers = [[] for n in range(N)]
    full_towers = []

    for i in range(N * B):
        d = int(input())
        if d == -1:
            exit()
        placed = False
        for j, tower in enumerate(towers):
            L = len(tower)
            if L < B - 2:
                placed = True
                tower.append(d)
                print(j + 1)
                break
            if L == B - 2 and d >= 8:
                placed = True
                tower.append(d)
                print(j + 1)
                break
            if L == B - 1 and d == 9:
                placed = True
                tower.append(d)
                print(j + 1)
                break
        if not placed:
            tower.append(d)
            if len(tower) == B:
                full_towers.append(tower)
                towers = towers[:-1]
            print(j + 1)
