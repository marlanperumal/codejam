T = int(input())
for t in range(1, T+1):
    N, L = [int(si) for si in input().split()]
    words = []
    for n in range(N):
        words.append(input())
    tiles = {l: {} for l in range(L)}
    for word in words:
        for l in range(L):
            if word[l] in tiles[l]:
                tiles[l][word[l]] += 1
            else:
                tiles[l][word[l]] = 1
    ans = "-"
    potentials = list(tiles[L-1].keys())
    for l in reversed(range(L-1)):
        new_potentials = []
        for tile in tiles[l]:
            new_potentials.extend([tile + potential for potential in potentials])
        potentials = new_potentials
    for potential in potentials:
        if potential not in words:
            ans = potential
            break
    print("Case #{}: {}".format(t, ans))
