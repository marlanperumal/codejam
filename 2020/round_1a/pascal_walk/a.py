# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def tri(x):
    return x * (x + 1) // 2


def run(N):
    if N == 1:
        print(1, 1)
    elif N == 2:
        print(1, 1)
        print(2, 1)
    elif N == 3:
        print(1, 1)
        print(2, 1)
        print(2, 2)
    elif N == 4:
        print(1, 1)
        print(2, 1)
        print(3, 2)
    else:
        print(1, 1)
        print(2, 1)
        N -= 2
        y = 2
        i = 1
        j = tri(i)
        while N > j + i:
            i += 1
            y += j
            N -= j
            print(i + 1, i - 1)
            j = tri(i)
        while N > i - 1 and i > 1:
            j = i
            y += j
            N -= j
            print(i + 1, i)
            i -= 1
        if N > 0:
            N -= 1
            y += 1
            print(i + 1, i + 1)

        while N > 0:
            i += 1
            y += 1
            N -= 1
            print(i + 1, i + 1)


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        print("Case #{}:".format(t))
        result = run(N)
