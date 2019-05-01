def run(N, S, E, L):
    stones = {
        n: {
            "s": S[n],
            "e": E[n],
            "l": L[n]
        } for n in range(N)
    }
    energy = 0
    while stones:
        stone = max(stones, key=lambda n: 
            [stones[n]["e"] - sum([
                min(stones[i]["e"], stones[i]["l"] * stones[n]["s"])
                for i in stones 
                if i != n
            ]), stones[n]["s"], stones[n]["e"]]
        )
        energy += stones[stone]["e"]
        s = stones[stone]["s"]
        del stones[stone]
        stones_left = list(stones.keys())
        for stone in stones_left:
            stones[stone]["e"] -= stones[stone]["l"] * s
            if stones[stone]["e"] <= 0:
                del stones[stone]

    return energy


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        S, E, L = [], [], []
        for n in range(N):
            s, e, l = [int(i) for i in input().split()]
            S.append(s)
            E.append(e)
            L.append(l)
        result = run(N, S, E, L)
        print("Case #{}: {}".format(t, result))
