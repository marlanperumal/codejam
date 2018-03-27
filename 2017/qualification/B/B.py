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
    t = read_int()
    for k in range(1, t+1):
        n = read_str()
        m = ""
        N = len(n)
        i = 1
        while i < N:
            if n[-i] == "0" or n[-i] < n[-i-1]:
                n = n[:-i] + "9"*(i)
                j = i + 1
                c = n[-j]
                while c == "0":
                    n = n[:-j] + "9"*(j)
                    j = j + 1
                    c = n[-j]
                n = n[:-j] + str(int(c)-1) + n[N-j+1:]
                if n[0] == "0":
                    n = n[1:]
                    N -= 1
            i += 1
        write_case_ans(k, n)


if __name__ == "__main__":
    main()
