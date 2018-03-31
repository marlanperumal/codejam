T = int(input())
for t in range(1, T+1):
    N = int(input())
    P = [int(si) for si in input().split()]
    parties = { chr(ord("A") + i): pi for i, pi in enumerate(P) }
    evac_plan = []
    while sum(parties.values()) > 0:
        biggest_party = max(parties, key=parties.get)
        evac_step = biggest_party
        parties[biggest_party] -= 1
        senate_size = sum(parties.values())
        next_biggest_party = max(parties, key=parties.get)
        if parties[next_biggest_party] > (senate_size//2):
            evac_step += next_biggest_party
            parties[next_biggest_party] -= 1
        evac_plan.append(evac_step)
    print("Case #{}: {}".format(t, " ".join(evac_plan)))
