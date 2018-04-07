T = int(input())
for t in range(1, T+1):
    D, P = input().split()
    D = int(D)
    p2rep = {1: 0}
    i = 0
    j = 1
    for i in range(len(P)):
        if P[i] == "S":
            p2rep[j] += 1
        elif P[i] == "C":
            j *= 2
            p2rep[j] = 0
    hacks = 0
    damage = sum([v*k for k,v in p2rep.items()])
    while damage > D:
        max_power = max(p2rep.keys())
        if max_power == 1:
            break
        if p2rep[max_power] == 0:
            del p2rep[max_power]
        else:
            p2rep[max_power] -= 1
            p2rep[max_power/2] += 1
            if p2rep[max_power] == 0:
                del p2rep[max_power]
            hacks += 1
            damage = sum([v*k for k,v in p2rep.items()])
    ans = "IMPOSSIBLE" if damage > D else hacks
    print("Case #{}: {}".format(t, ans))
