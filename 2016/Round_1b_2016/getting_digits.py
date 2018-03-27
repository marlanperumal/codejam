# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:46:58 2016

@author: marlan
"""

import collections
import copy

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
        ans = "".join(map(str, ans))
    print("Case #{}: {}".format(i, ans))
    
def main():
#    num_strings = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    num_strings = ["ZERO", "TWO", "SIX", "EIGHT", "THREE", "FOUR", "FIVE", "SEVEN", "NINE", "ONE"]
    nums = [0, 2, 6, 8, 3, 4, 5, 7, 9, 1]
    t = read_int()
    for i in range(t):
        s = read_str()
        letters = collections.defaultdict(int)
        for c in s:
            letters[c] += 1
        phone = []
        for numj, num in zip(nums, num_strings):
            num_in_phone = True
            while num_in_phone:
                letters_copy = copy.deepcopy(letters)
                for c in num:
                    if c not in letters_copy:
                        num_in_phone = False
                        break
                    elif letters_copy[c] < 1:
                        num_in_phone = False
                        break
                    else:
                        letters_copy[c] -=1 
                if num_in_phone:
                    phone.append(numj)
                    for c in num:
                        letters[c] -= 1
        phone.sort()
        write_case_ans(i+1,phone)
            
if __name__ == "__main__":
    main()