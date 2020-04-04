input_file = "sample.in"


def input_from_file(filename):
    for line in open(filename):
        yield line.strip()


file_input = input_from_file(input_file)


def input():
    return next(file_input)


def run():

    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        result = run()
        print("Case #{}: {}".format(t, result))
