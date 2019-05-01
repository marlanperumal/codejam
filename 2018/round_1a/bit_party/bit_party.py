input_file = "bit_party.sample.in"


def input_from_file(filename):
    for line in open(filename):
        yield line.strip()


file_input = input_from_file(input_file)


def input():
    return next(file_input)


def run(R, B, C, M, S, P):
    print(R, B, C)
    U = [0] * C
    c = min(range(C), key=lambda i: (S[i] + P[i], S[i]))
    B -= 1
    U[c] += 1
    print(1, U)
    while B > 0:
        min_cost = 10**9 * 10**9 + 10**9
        best_cashier = 0
        for c in range(C):
            if M[c] > U[c]:
                cost = S[c] * (U[c] + 1) + P[c]
                if (cost < min_cost) or (cost == min_cost and S[c] < S[best_cashier]):
                    min_cost = cost
                    best_cashier = c

        U[best_cashier] += 1
        B -= 1
        print(2, U)
    print(3, U)

    total_cost = max([S[c]*U[c] + P[c] for c in range(C)])

    return total_cost


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        R, B, C = [int(i) for i in input().split()]
        M = []
        S = []
        P = []
        for c in range(C):
            m, s, p = [int(i) for i in input().split()]
            M.append(m)
            S.append(s)
            P.append(p)
        result = run(R, B, C, M, S, P)
        print("Case #{}: {}".format(t, result))
