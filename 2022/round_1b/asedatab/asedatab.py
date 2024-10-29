N = 8

T = int(input())

for t in range(T):
    print("0" * N)
    x = int(input())
    x0 = 0
    if x == -1:
        exit()
    while x > 0:
        if x == 4 and x0 == 4:
            # print("1" * x + "0" * (N - x))
            print("10111000")
        else:
            print("1" * x + "0" * (N - x))
        x0 = x
        x = int(input())
        if x == -1:
            exit()
