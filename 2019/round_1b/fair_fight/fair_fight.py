input_file = "fair_fight.sample.in"


def input_from_file(filename):
    for line in open(filename):
        yield line.strip()


file_input = input_from_file(input_file)


def input():
    return next(file_input)


def run(N, K, C, D):
    fair_fights = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            c_max = max(C[i:j])
            d_max = max(D[i:j])
            if abs(c_max - d_max) <= K:
                fair_fights += 1
    return fair_fights


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, K = [int(i) for i in input().split()]
        C = [int(i) for i in input().split()]
        D = [int(i) for i in input().split()]
        result = run(N, K, C, D)
        print("Case #{}: {}".format(t, result))
