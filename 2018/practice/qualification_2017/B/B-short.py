T = int(input())
for t in range(1, T+1):
    n = input()
    nl = [int(si) for si in n]
    tidy = True
    l = nl[0]
    k = 0
    for i in range(len(nl)-1):
        if not nl[i] == l:
            l = nl[i]
            k = i
        if nl[i+1] < nl[i]:
            tidy = False
            if nl[i] == 1:
                nl = [9 for j in range(len(nl)-1)]
            else:
                nl = nl[:k] + [nl[k]-1] + [9 for j in range(k+1, len(nl))]
            break
    ans = "".join([str(i) for i in nl])
    print("Case #{}: {}".format(t, ans))
