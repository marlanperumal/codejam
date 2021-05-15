T, N = [int(i) for i in input().split()]

for t in range(1, T + 1):
    for n in range(1, N):
        print(f"M {n} {N}")
        m = int(input())
        if m == -1:
            exit()
        if m > n:
            print(f"S {n} {m}")
            _ = int(input())
            if _ == -1:
                exit()
    print("D")
    _ = int(input())
    if _ == -1:
        exit()
