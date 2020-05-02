# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)
from collections import defaultdict


def run(N, D, A):
    slices = sorted(slices)
    g_min_cuts = D - 1
    for i, s in enumerate(slices):
        min_cuts = D - 1
        cuts = 0
        pieces = 1
        for j, ss in enumerate(slices[i + 1:]):
            if ss % s == 0:
                pieces += ss / s

    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, D = [int(i) for i in input().split()]
        A = [int(i) for i in input().split()]
        result = run(N, D, A)
        print("Case #{}: {}".format(t, result))
