input_file = "manhattan_crepe_cart.sample.in"


def input_from_file(filename):
    for line in open(filename):
        yield line.strip()


file_input = input_from_file(input_file)


def input():
    return next(file_input)


def run(P, Q, X, Y, D):
    grid = [[0]*(Q + 1) for q in range(Q + 1)]

    for p, [x, y, d] in enumerate(zip(X, Y, D)):
        if d == "N":
            for j in range(y + 1, Q + 1):
                for i in range(Q + 1):
                    grid[i][j] += 1 
        elif d == "S":
            for j in range(y):
                for i in range(Q + 1):
                    grid[i][j] += 1 
        if d == "E":
            for i in range(x + 1, Q + 1):
                for j in range(Q + 1):
                    grid[i][j] += 1 
        if d == "W":
            for i in range(x):
                for j in range(Q + 1):
                    grid[i][j] += 1

    location = max([(grid[i][j], -i, -j) for i in range(Q + 1) for j in range(Q + 1)])
    result = "{} {}".format(-location[1], -location[2])
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        P, Q = [int(i) for i in input().split()]
        X = []
        Y = []
        D = []
        for p in range(P):
            x, y, d = [i for i in input().split()]
            X.append(int(x))
            Y.append(int(y))
            D.append(d)
        result = run(P, Q, X, Y, D)
        print("Case #{}: {}".format(t, result))
