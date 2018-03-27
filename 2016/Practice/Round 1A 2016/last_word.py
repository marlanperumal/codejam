# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:07:52 2016

@author: marlan
"""

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    w = ""
    f = s[0]
    for c in s:
        if c >= f:
            w = c + w
            f = c
        else:
            w = w + c
            
    print "Case #{}: {}".format(i,w)

