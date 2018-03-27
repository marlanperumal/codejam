# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:28:25 2016

@author: marlan
"""

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
    for i in range(t):
        b, m = read_int_list()
        if m > (b-2)*(b-1)//2 + 1:
            write_case_ans(i+1,"IMPOSSIBLE")
        else:
            write_case_ans(i+1,"POSSIBLE")
            ans = [[0]*b]
            for j in range(1,b):
                ans.append([0]*b)
            for j in range(1,b):
                ans[0][j] = 1
            m -= 1
            c = b-1
            while m > 0 and c > 0:
                r = 1
                while m > 0 and r < b:
                    ans[r][c] = 1
                    m -= 1
                    r += 1
                c -= 1
            for j in range(b):
                print("".join(str(ans[j])))
            print("".join(str([0]*b)))

if __name__ == "__main__":
    main()