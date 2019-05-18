from collections import deque
input_file = "chainsaw_jugglers.one.sample.in"


def input_from_file(filename):
    for line in open(filename):
        yield line.strip()


file_input = input_from_file(input_file)


def input():
    return next(file_input)


def run(R, B):
    total_jugglers = 0
    chainsaws = 1
    combinations = deque([(i, chainsaws - i) for i in range(chainsaws + 1)])
    while R + B >= chainsaws:
        print(combinations)
        if len(combinations) == 0:
            chainsaws += 1
            combinations = deque([(i, chainsaws - i) for i in range(chainsaws + 1) if R >= i and B >= chainsaws - i])
        else:
            if R > B:
                combo = combinations.pop()
            else:
                combo = combinations.popleft()
            if R >= combo[0] and B >= combo[1]:
                print(combo)
                R -= combo[0]
                B -= combo[1]
                total_jugglers += 1
    return total_jugglers


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        R, B = [int(i) for i in input().split()]
        result = run(R, B)
        print("Case #{}: {}".format(t, result))
