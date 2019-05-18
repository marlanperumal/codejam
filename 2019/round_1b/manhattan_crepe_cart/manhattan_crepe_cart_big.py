# input_file = "manhattan_crepe_cart.sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(P, Q, X, Y, D):
    # grid = [[0]*(Q + 1) for q in range(Q + 1)]
    Xs = sorted([[x, -1 if d == "W" else 1, 0, 0, 0] for x, d in zip(X, D) if d in ["E", "W"]])
    Ys = sorted([[y, -1 if d == "S" else 1, 0, 0, 0] for y, d in zip(Y, D) if d in ["N", "S"]])

    Xs = sorted(Xs + [[x[0] + 1, 0, 0, 0, 0] for x in Xs if x[0] + 1 <= Q])
    Xs = [[0, 0, 0, 0, 0]] + Xs

    for i, xs in enumerate(Xs[1:]):
        xs[2] = Xs[i][2] + max(Xs[i][1], 0)

    for i, xs in enumerate(reversed(Xs[:len(Xs)-1])):
        j = len(Xs) - i - 1
        xs[3] = Xs[j][3] - min(Xs[j][1], 0)

    for xs in Xs:
        xs[4] = xs[2] + xs[3]

    Ys = sorted(Ys + [[y[0] + 1, 0, 0, 0, 0] for y in Ys if y[0] + 1 <= Q])
    Ys = [[0, 0, 0, 0, 0]] + Ys

    for i, ys in enumerate(Ys[1:]):
        ys[2] = Ys[i][2] + max(Ys[i][1], 0)

    for i, ys in enumerate(reversed(Ys[:len(Ys)-1])):
        j = len(Ys) - i - 1
        ys[3] = Ys[j][3] - min(Ys[j][1], 0)

    for ys in Ys:
        ys[4] = ys[2] + ys[3]
    if t == 5:
        print(sorted(Xs, key=lambda x: [-x[4], x[0]]))
        print(sorted(Ys, key=lambda y: [-y[4], y[0]]))
    return "{} {}".format(
        max(Xs, key=lambda x: [x[4], -x[0]])[0], 
        max(Ys, key=lambda y: [y[4], -y[0]])[0]
    )


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
