# input_file = "b.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(S):
    S = [s[1:] for s in S]
    S = sorted(S, key=lambda x: len(x), reverse=True)
    for i in range(len(S) - 1):
        if not S[i].endswith(S[i + 1]):
            result = "*"
            return result
    result = S[0]

    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        S = []
        for n in range(N):
            S.append(input())

        result = run(S)
        print("Case #{}: {}".format(t, result))
