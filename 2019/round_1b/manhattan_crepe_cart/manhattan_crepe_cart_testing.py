from random import randint

T = 10
Q = 10
P = 500
print(T)
for t in range(T):
    p = randint(1, P)
    X = randint(0, Q)
    Y = randint(0, Q)
    directions = ["N", "S", "E", "W"]
    print(p, Q)
    for i in range(p):
        x, y = randint(0, Q), randint(0, Q)
        d = directions[randint(0, 3)]
        while (x == 0 and d == "W") or (y == 0 and d == "S")\
                or (x == Q and d == "E") or (y == Q and d == "S"):
            d = directions[randint(0, 3)]
        print("{} {} {}".format(x, y, d))
