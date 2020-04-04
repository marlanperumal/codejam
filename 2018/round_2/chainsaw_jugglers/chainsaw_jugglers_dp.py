# input_file = "chainsaw_jugglers.one.sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)

from collections import deque

max_B = 50
max_R = 50


def br_to_i(b, r):
    return b*(max_B + 1) + r


def i_to_br(i):
    return int(i//(max_B + 1)), i % (max_B + 1)


dp_table = {(0, 0, 0): 0}

for i in range((max_B + 1) * (max_R + 1)):
    b1, r1 = i_to_br(i)
    for b in range(max_B + 1):
        for r in range(max_R + 1):
            if i < 1:
                dp_table[(i, b, r)] = 0
            else:
                if b1 > b or r1 > r:
                    test_value = 0
                else:
                    test_value = 1 + dp_table[(i - 1, b - b1, r - r1)]
                best_value = max(dp_table[(i - 1, b, r)], test_value)
                dp_table[(i, b, r)] = best_value


def run(R, B):
    return dp_table[(br_to_i(max_B, max_R), B, R)]


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        R, B = [int(i) for i in input().split()]
        result = run(R, B)
        print("Case #{}: {}".format(t, result))