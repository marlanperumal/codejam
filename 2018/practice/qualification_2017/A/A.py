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
    print("Case #{i}: {ans}".format(i=i, ans=ans), end='\n')

def main():
    T = read_int()
    for t in range(1, T+1):
        s, k = read_str().split()
        k = int(k)
        sb = [si == "+" for si in s]
        f = 0
        for i in range(len(sb) - k + 1):
            if not sb[i]:
                f += 1
                sb[i:i+k] = [not b for b in sb[i:i+k]]
        write_case_ans(t, f if all(sb) else "IMPOSSIBLE")

if __name__ == "__main__":
    main()
