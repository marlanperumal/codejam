# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:17:37 2016

@author: marlan
"""

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    height_dict = {}
    for j in xrange(2*n-1):
        rc = [int(m) for m in raw_input().split(" ")]
        for p in rc:
            if p in height_dict:
                height_dict[p] = height_dict[p] + 1
            else:
                height_dict[p] = 1
    ml = []
    for p, np in height_dict.items():
        if np % 2 != 0:
            ml.append(p)
    ml.sort()
    mls = str(ml[0])
    for p in ml[1:]:
        mls = mls + " " + str(p)
    print "Case #{}: {}".format(i,mls)