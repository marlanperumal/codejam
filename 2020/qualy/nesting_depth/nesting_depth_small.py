# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(S):
    str_list = []
    substring = S[0]
    for c in S[1:]:
        if c != substring[0]:
            str_list.append(substring)
            substring = c
        else:
            substring += c
    str_list.append(substring)
    result = "".join([
        ss if ss[0] == "0" else "({})".format(ss) if ss[0] == "1" else ""
        for ss in str_list
    ])
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        S = input()
        result = run(S)
        print("Case #{}: {}".format(t, result))
