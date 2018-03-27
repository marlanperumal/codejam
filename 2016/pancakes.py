# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:10:01 2016

@author: marlan
"""

def count_flips(p):
    flips = 0
    curr_p = p[0]
    for i in xrange(1,len(p)):
        if curr_p != p[i]:
            flips = flips + 1
            curr_p = p[i]
    if curr_p == "-":
        flips = flips + 1
    return flips
    
def drive_pancakes():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        p = raw_input()
        print "Case #{}: {}".format(i,count_flips(p))
        
if __name__ == '__main__':
    drive_pancakes()