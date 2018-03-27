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
        D, N = read_int_list()
        slowest_time = 0
        for n in range(N):
            Ki, Si = read_int_list()
            time = (D - Ki)/Si
            if time > slowest_time:
                slowest_time = time
        write_case_ans(t, D/slowest_time)


if __name__ == "__main__":
    main()
