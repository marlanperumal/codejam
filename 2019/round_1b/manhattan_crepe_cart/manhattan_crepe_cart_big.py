# input_file = "manhattan_crepe_cart.sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(P, Q, X, Y, D):
    # grid = [[0]*(Q + 1) for q in range(Q + 1)]
    Xs = sorted([[x, -1 if d == "W" else 1] for x, d in zip(X, D) if d in ["E", "W"]])
    Ys = sorted([[y, -1 if d == "S" else 1] for y, d in zip(Y, D) if d in ["N", "S"]])

    Xs = [[0, 0]] + Xs
    Xs = sorted(Xs + [[x + 1, 0] for x, d in Xs if x + 1 < Q])
    if Xs[-1][0] != Q:
        Xs = Xs + [[Q, 0]]

    Xi = [[0, 0]]
    for i in range(1, len(Xs)):
        Xi.append([Xs[i][0], Xi[i-1][1] + Xs[i-1][1]])
    
    Ys = [[0, 0]] + Ys
    Ys = sorted(Ys + [[y + 1, 0] for y, d in Ys if y + 1 < Q])
    if Ys[-1][0] != Q:
        Ys = Ys + [[Q, 0]]

    Yi = [[0, 0]]
    for i in range(1, len(Ys)):
        Yi.append([Ys[i][0], Yi[i-1][1] + Ys[i-1][1]])

    Xd = {}
    Yd = {}
    for x, i in Xi:
        Xd[x] = i
    for y, i in Yi:
        Yd[y] = i

    return "{} {}".format(max(Xd, key=lambda x: [Xd[x], -x]), max(Yd, key=lambda y: [Yd[y], -y]))


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        P, Q = [int(i) for i in input().split()]
        X = []
        Y = []
        D = []
        for p in range(P):
            x, y, d = [i for i in input().split()]
            X.append(int(x))
            Y.append(int(y))
            D.append(d)
        result = run(P, Q, X, Y, D)
        print("Case #{}: {}".format(t, result))
