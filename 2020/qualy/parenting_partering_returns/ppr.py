# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(N, SE):
    SEI = sorted(SE)
    current = 0
    s0, e0, i0 = SEI[0]
    schedule = [0]
    tasks = [[[s0, e0]], []]
    for s, e, i in SEI[1:]:
        if s < e0:
            other_tasks = tasks[1 - current]
            if not other_tasks or s >= other_tasks[-1][1]:
                current = 1 - current
            else:
                return "IMPOSSIBLE"
        schedule.append(current)
        tasks[current].append([s, e])
        s0, e0, i0 = s, e, i
    sortable_schedule = [[sei[-1], j] for sei, j in zip(SEI, schedule)]
    sorted_schedule = sorted(sortable_schedule)
    parents = "CJ"
    result = "".join([parents[i[1]] for i in sorted_schedule])
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        SEI = [[int(i) for i in input().split(" ")] + [n] for n in range(N)]
        result = run(N, SEI)
        print("Case #{}: {}".format(t, result))
