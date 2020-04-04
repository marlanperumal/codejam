# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(S):
    Sb = ["("*i + str(i) + ")"*i for i in S]
    Sbs = "".join(Sb)
    while ")(" in Sbs:
        Sbs = Sbs.replace(")(", "")
    return Sbs


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        S = [int(i) for i in input()]
        result = run(S)
        print("Case #{}: {}".format(t, result))
