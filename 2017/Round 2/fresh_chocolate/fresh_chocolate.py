# input_file = "fresh_chocolate.sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


from collections import defaultdict


def run(N, P, G):
    choc_groups = defaultdict(int)
    for g in G:
        choc_groups[g % P] += 1
    # print(N, P, G)
    # print(choc_groups)
    if P == 2:
        result = choc_groups[0] + int(choc_groups[1] // 2) + choc_groups[1] % 2
    elif P == 3:
        result = choc_groups[0]
        result += min(choc_groups[1], choc_groups[2])
        result += int(abs(choc_groups[1] - choc_groups[2]) // 3)
        result += 0 if abs(choc_groups[1] - choc_groups[2]) % 3 == 0 else 1
    elif P == 4:
        result = choc_groups[0]
        min_13 = min(choc_groups[1], choc_groups[3])
        result += min_13
        choc_groups[1] -= min_13
        choc_groups[3] -= min_13
        result += int(choc_groups[2] // 2)
        choc_groups[2] = choc_groups[2] % 2
        if choc_groups[2] == 1 and choc_groups[1] >= 2:
            result += 1
            choc_groups[2] -= 1
            choc_groups[1] -= 2
        if choc_groups[2] == 1 and choc_groups[3] >= 2:
            result += 1
            choc_groups[2] -= 1
            choc_groups[3] -= 2
        if choc_groups[1] >= 4:
            result += int(choc_groups[1] // 4)
            choc_groups[1] = choc_groups[1] % 4
        if choc_groups[3] >= 4:
            result += int(choc_groups[3] // 4)
            choc_groups[3] = choc_groups[3] % 4
        if choc_groups[1] > 0 or choc_groups[2] > 0 or choc_groups[3] > 0:
            result += 1
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, P = [int(i) for i in input().split()]
        G = [int(i) for i in input().split()]
        result = run(N, P, G)
        print("Case #{}: {}".format(t, result))
