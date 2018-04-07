def check_sort(L):
    sL1 = sorted(L[::2])
    sL2 = sorted(L[1::2])
    for i in range(len(sL2)):
        if sL1[i] > sL2[i]:
            return i*2
        elif len(sL1) > i+1 and sL2[i] > sL1[i+1]:
            return i*2 + 1
    return "OK"

T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = [int(si) for si in input().split()]
    print("Case #{}: {}".format(t, check_sort(L)))
