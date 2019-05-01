def transmute(i, R1, R2, G, Ts):
    r1 = R1[i]
    r2 = R2[i]
    if r1 in Ts or r2 in Ts:
        return None

    while G[r1] == 0 or G[r2] == 0:

        if G[r1] == 0:
            Ts.add(r1)
            transmute_result = transmute(r1, R1, R2, G, Ts)
            if transmute_result is None:
                return None
            else:
                Ts.remove(r1)
        if G[r2] == 0:
            Ts.add(r2)
            transmute_result = transmute(r2, R1, R2, G, Ts)
            if transmute_result is None:
                return None
            else:
                Ts.remove(r2)
    
    G[r1] -= 1
    G[r2] -= 1
    G[i] += 1
    return 1


def run(M, R1, R2, G):
    R1 = [r - 1 for r in R1]
    R2 = [r - 1 for r in R2]
    Ts = {0}
    while True:
        transmute_result = transmute(0, R1, R2, G, Ts)
        if transmute_result is None:
            break
    result = G[0]
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        M = int(input())
        R1, R2 = [], []
        for m in range(M):
            r1, r2 = [int(i) for i in input().split()]
            R1.append(r1)
            R2.append(r2)
        G = [int(i) for i in input().split()]
        result = run(M, R1, R2, G)
        print("Case #{}: {}".format(t, result))
