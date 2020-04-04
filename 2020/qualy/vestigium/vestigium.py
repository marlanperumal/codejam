# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(N, square):
    bad_rows = 0
    bad_cols = 0
    trace = sum(square[i][i] for i in range(N))
    for i in range(N):
        values = set()
        for j in range(N):
            n = square[i][j]
            if n in values:
                bad_rows += 1
                break
            values.add(n)
    for i in range(N):
        values = set()
        for j in range(N):
            n = square[j][i]
            if n in values:
                bad_cols += 1
                break
            values.add(n)
    return trace, bad_rows, bad_cols


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        square = [[int(j) for j in input().split()] for j in range(N)]
        k, r, c = run(N, square)
        print("Case #{}: {} {} {}".format(t, k, r, c))
