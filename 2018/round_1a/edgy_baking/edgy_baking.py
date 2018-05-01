from math import sqrt

T = int(input())
for t in range(1,T+1):
    N, P = [int(si) for si in input().split()]
    P2 = P/2
    cookies = []
    for n in range(N):
        wi, hi = [int(si) for si in input().split()]
        cookies.append([wi, hi])
    cookie_perimeters = [cookie[0]+cookie[1] for cookie in cookies]
    cookie_min_extras = [min(cookie[0],cookie[1]) for cookie in cookies]
    cookie_max_extras = [sqrt(cookie[0]**2  + cookie[1]**2) for cookie in cookies]

    if sum(cookie_perimeters) > P2:
        ans = sum(cookie_perimeters)*2
    elif sum(cookie_perimeters) + sum(cookie_max_extras) < P2:
        ans = 2*(sum(cookie_perimeters) + sum(cookie_max_extras))
    elif (P-sum(cookie_perimeters))/N >= sum(cookie_min_extras)/N and (P-sum(cookie_perimeters))/N <= sum(cookie_max_extras)/N:
        ans = 2*P
    else:
        closest = P - sum(cookie_perimeters)
        curr_P = sum(cookie_perimeters)
        for n in range(n):
            curr_P += cookie_min_extras[n]
            if abs(P - curr_P) < closest:
                closest = abs(P - curr_P)
            if curr_P > P:
                break
            if curr_P + cookie_max_extras[n] - cookie_min_extras[n] > P:
                closest = P
                break
            curr_P += cookie_max_extras[n] - cookie_min_extras[n]
            if abs(P - curr_P) < closest:
                closest = abs(P - curr_P)
        ans = closest*2


    print("Case #{}: {}".format(t, ans))
