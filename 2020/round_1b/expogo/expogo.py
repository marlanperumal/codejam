from math import log2, ceil


def run(X, Y):
    min_length = abs(X) + abs(Y)
    min_moves = ceil(log2(min_length + 1))
    move = 2**(min_moves - 1)
    result = ""
    while move >= 1:
        if abs(X) > abs(Y):
            if X > 0:
                result += "E"
                X -= move
            else:
                result += "W"
                X += move
        else:
            if Y > 0:
                result += "N"
                Y -= move
            else:
                result += "S"
                Y += move
        move //= 2

    if abs(X) > 0 or abs(Y) > 0:
        return "IMPOSSIBLE"

    result = "".join([s for s in reversed(result)])
    return result


T = int(input())
for t in range(1, T + 1):
    X, Y = [int(i) for i in input().split()]
    result = run(X, Y)
    print("Case #{}: {}".format(t, result))
