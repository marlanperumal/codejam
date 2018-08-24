T = int(input())
if T == -1:
    exit()
for t in range(1,T+1):
    N = int(input())
    if N == -1:
        exit()
    flavours = {d: 0 for d in range(N)}
    for n in range(N):
        D = [int(si) for si in input().split()]
        if D == [-1]:
            exit()
        nD = D.pop(0)
        serve = -1
        for d in D:
            if d in flavours:
                serve = d
                del flavours[d]
                break
        print(serve, flush=True)
