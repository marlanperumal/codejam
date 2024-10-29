from collections import deque

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    D = [int(i) for i in input().split()]
    dq = deque(D)
    max_d = 0
    paying = 0
    while dq:
        if dq[0] < dq[-1]:
            p = dq.popleft()
        else:
            p = dq.pop()
        if p >= max_d:
            max_d = p
            paying += 1
    print(f"Case #{t}: {paying}")
