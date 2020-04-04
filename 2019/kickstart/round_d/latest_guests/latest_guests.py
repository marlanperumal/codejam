# input_file = "latest_guests.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(N, G, M, H, Gd):
    Nh0 = [[] for n in range(N)]
    for g, h in enumerate(H):
        Nh0[h].append(g)
    Gr = [1 for g in range(G)]
    for m in range(M):
        Nh1 = [[] for n in range(N)]
        for g in range(G):
            if Gd[g] == "C":
                H[g] = (H[g] + 1) % N
            else:
                H[g] = (H[g] + N - 1) % N
            Nh1[H[g]].append(g)
        for n in range(N):
            if len(Nh1[n]) > 0:
                for g in Nh0[n]:
                    Gr[g] -= 1
                for g in Nh1[n]:
                    Gr[g] += 1
                Nh0[n] = Nh1[n]
    result = " ".join([str(gr) for gr in Gr])
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, G, M = [int(i) for i in input().split()]
        Gd = []
        H = []
        for g in range(G):
            h, gd = input().split()
            H.append(int(h) - 1)
            Gd.append(gd)
        result = run(N, G, M, H, Gd)
        print("Case #{}: {}".format(t, result))
