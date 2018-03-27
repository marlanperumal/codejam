T = int(input())
for t in range(1, T+1):
    s, k = read_str().split()
    k = int(k)
    sb = [si == "+" for si in s]
    f = 0
    for i in range(len(sb) - k + 1):
        if not sb[i]:
            f += 1
            sb[i:i+k] = [not b for b in sb[i:i+k]]
    ans = f if all(sb) else "IMPOSSIBLE"
    print("Case #{}: {}".format(t, ans))
    
