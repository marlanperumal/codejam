def read_int():
    return int(input())

def read_int_list():
    return [int(n) for n in input().split(" ")]

def read_str():
    return input()

def read_char_list():
    return [c for c in input().split(" ")]

def write_case_ans(i,ans):
    if isinstance(ans,list):
        ans = " ".join(map(str, ans))
    print("Case #{}: {}".format(i, ans))

def main():
    T = read_int()
    for t in range(1, T+1):
        n = read_str()
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
        write_case_ans(t, "".join([str(i) for i in nl]))

if __name__ == "__main__":
    main()
