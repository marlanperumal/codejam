# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(X, Y, M):
    for i, m in enumerate(M):
        if m == "S":
            Y -= 1
        elif m == "N":
            Y += 1
        elif m == "W":
            X -= 1
        elif m == "E":
            X += 1

        if abs(X) + abs(Y) <= i + 1:
            return i + 1

    return "IMPOSSIBLE"


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        X, Y, M = [s for s in input().split()]
        X, Y = int(X), int(Y)
        result = run(X, Y, M)
        print("Case #{}: {}".format(t, result))
