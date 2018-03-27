from heapq import heappush, heappop

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
    for j in range(1, t+1):
        n, k = read_int_list()
        stall_sets = []
        heappush(stall_sets, -n)
        for i in range(k):
            stall_set = -heappop(stall_sets)
            stall_set -= 1
            l = stall_set // 2
            r = l + stall_set % 2
            if r > 0:
                heappush(stall_sets,-r)
            if l > 0:
                heappush(stall_sets,-l)
        write_case_ans(j, [r, l])


if __name__ == "__main__":
    main()
