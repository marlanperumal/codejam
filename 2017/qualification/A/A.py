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
    for i in range(1, t+1):
        s, k = input().split(" ")
        k = int(k)
        sb = [True if c == "+" else False for c in s]
        flips = 0
        for j in range(len(sb) - k + 1):
            if not sb[j]:
                sb[j:j+k] = [not c for c in sb[j:j+k]]
                flips += 1
        write_case_ans(i, flips if all(sb) else "IMPOSSIBLE")

if __name__ == "__main__":
    main()
