# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)

from collections import defaultdict


def run(Q, M):
    mapping = defaultdict(int)

    for m in M:
        for c in m:
            mapping[c] += 1

    sorted_mapping = sorted(mapping, key=lambda x: mapping[x])

    result = sorted_mapping[0:1] + list(reversed(sorted_mapping[1:]))
    result = "".join(result)

    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        U = int(input())
        Q = []
        M = []
        for i in range(int(1e4)):
            q, m = input().split()
            Q.append(q)
            M.append(m)
        result = run(Q, M)
        print("Case #{}: {}".format(t, result))
