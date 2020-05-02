# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)
from collections import defaultdict


def run(N, D, A):
    slices = defaultdict(int)
    for a in A:
        slices[a] += 1

    slice_list = sorted(list(slices))

    max_slices = max(slices.values())

    if D == 2:
        if max_slices >= 2:
            return 0
        else:
            return 1
    elif D == 3:
        if len(slice_list) == 1 and max_slices < 3:
            return 2
        elif max_slices >= 3:
            return 0
        elif max([slices[s] for s in slice_list[:-1]]) == 2:
            return 1
        else:
            for i, s in enumerate(slice_list[:-1]):
                for ss in slice_list[i + 1:]:
                    if ss == 2 * s:
                        return 1
            return 2
    else:
        return 0


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, D = [int(i) for i in input().split()]
        A = [int(i) for i in input().split()]
        result = run(N, D, A)
        print("Case #{}: {}".format(t, result))
