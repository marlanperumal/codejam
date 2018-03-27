# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:13:24 2016

@author: marlan
"""

import numpy as np
import matplotlib.pyplot as plt

## raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
## This is all you need for most Google Code Jam problems.
#t = int(raw_input())  # read a line with a single integer
#for i in xrange(1, t + 1):
#  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#  print "Case #{}: {} {}".format(i, n + m, n * m)
#  # check out .format's specification for more formatting options

def count_digits(n):
    if n == 0:
        return "Insomnia"
    i = 1
    done = False
    seen_digits = {}
    while not done:
        digits = [int(k) for k in str(i*n)]        
        for digit in digits:
            if digit not in seen_digits:
                seen_digits[digit] = 10
        if len(seen_digits) == 10:
            done = True
        else:
            i = i+1
    return i*n
    
def drive_beatrix():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        print "Case #{}: {}".format(i,count_digits(n))
        
if __name__ == '__main__':
    drive_beatrix()
