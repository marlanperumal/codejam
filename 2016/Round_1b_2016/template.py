# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:58:58 2016

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
    pass

if __name__ == "__main__":
    main()