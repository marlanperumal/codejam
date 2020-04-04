# input_file = "x_or_what.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


from functools import reduce


def xor_sum(L):
    return reduce(lambda x, y: x ^ y, L)


def bit_even(n):
    return sum([int(i) for i in bin(n)[2:]]) % 2 == 0


def check_interval(A, N):
    for n in reversed(range(1, N + 1)):
        for m in range(N + 1 - n):
            subinterval = A[m:m+n]
            if bit_even(xor_sum(subinterval)):
                return n
    return 0


def run(N, Q, A, P, V):
    result = []
    for p, v in zip(P, V):
        A[p] = v
        result.append(check_interval(A, N))
    return " ".join([str(r) for r in result])


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, Q = [int(i) for i in input().split()]
        A = [int(i) for i in input().split()]
        P = []
        V = []
        for q in range(Q):
            p, v = [int(i) for i in input().split()]
            P.append(p)
            V.append(v)
        result = run(N, Q, A, P, V)
        print("Case #{}: {}".format(t, result))
