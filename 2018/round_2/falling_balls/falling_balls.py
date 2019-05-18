# input_file = "falling_balls.sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(C, B):
    if B[0] == 0 or B[-1] == 0:
        return []
    if B == [1] * C:
        return [[0] * C]
    row = [1] * C
    slides_list = []
    for r in B:
        slides = []
        num_right_slides = 0
        for i, [b, bi] in enumerate(zip(B, row)):
            if i < len(slides):
                if bi - 1 < b:
                    for j in range(b - bi + 1):
                        slides.append(-1)
            else:
                if bi + num_right_slides < b:
                    slides.append(0)
                    for j in range(b - bi - num_right_slides):
                        slides.append(-1)
                    num_right_slides = 0
                elif bi + num_right_slides == b:
                    slides.append(0)
                    num_right_slides = 0
                else:
                    slides.append(1)
                    num_right_slides = bi + num_right_slides - b
        for i, slide in enumerate(slides):
            if slide == 1:
                row[i] -= 1
                row[i + 1] += 1
            elif slide == -1:
                row[i] -= 1
                row[i - 1] += 1
        slides_list.append(slides)
        done = B == row
        if done:
            break
    if not done:
        return []
    slides_list.append([0] * C)
    return slides_list


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        C = int(input())
        B = [int(i) for i in input().split()]
        result = run(C, B)
        if len(result) == 0:
            print("Case #{}: {}".format(t, "IMPOSSIBLE"))
        else:
            print("Case #{}: {}".format(t, len(result)))
            for slides in result:
                for slide in slides:
                    if slide == -1:
                        print("/", end="")
                    elif slide == 0:
                        print(".", end="")
                    else:
                        print("\\", end="")
                print()
