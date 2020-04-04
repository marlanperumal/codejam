input_file = "sample.in"


def input_from_file(filename):
    for line in open(filename):
        yield line.strip()


file_input = input_from_file(input_file)


def input():
    return next(file_input)


def run(N, C, J, M):
    order_1 = sorted(M)
    order_2 = sorted(M, key=lambda m: [m[1], m[0]])
    if order_1 == order_2:
        result = 1
    else:
        result = 2

    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        C = []
        J = []
        M = []
        for n in range(N):
            m = [int(i) for i in input().split()]
            M.append(m)
            C.append(m[0])
            J.append(m[1])
        result = run(N, C, J, M)
        print("Case #{}: {}".format(t, result))
