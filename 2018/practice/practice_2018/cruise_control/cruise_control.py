T = int(input())
for t in range(1, T+1):
    D, N = [int(si) for si in input().split()]
    longest_time = 0
    for n in range(N):
        Ki, Si = [int(si) for si in input().split()]
        time = (D-Ki)/Si
        if time > longest_time:
            longest_time = time
    speed = D/longest_time
    print("Case #{}: {}".format(t, speed))
