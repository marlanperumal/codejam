# Tidy number theory
# - Objective is to find the highest number less than N that is tidy
# - Some values of N will already be tidy
# - Repeated digits are still tidy
# - For non-tidy numbers, we need to inspect the digits left to right
#   and follow the last tidy digit with a string of 9s
# - If the last tidy digit is 1 then we need to drop an order and just fill 9s

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
