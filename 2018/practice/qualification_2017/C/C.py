from math import floor, ceil
from collections import defaultdict

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
        n, k = read_int_list()
        gaps = defaultdict(int)
        gaps[n] += 1
        while k > 0:
            g = max(gaps.keys())
            m = gaps[g]
            g1 = (g-1)//2
            g2 = g1 if g % 2 == 1 else g1 + 1
            gaps[g1] += m
            gaps[g2] += m
            k -= m
            del gaps[g]
        write_case_ans(t, [g2, g1])

if __name__ == "__main__":
    main()
