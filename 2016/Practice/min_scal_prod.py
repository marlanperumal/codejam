# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:25:04 2016

@author: marlan
"""

import numpy as np

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    x = np.array([int(j) for j in raw_input().split(" ")])
    y = np.array([int(j) for j in raw_input().split(" ")])
    xs = np.sort(x)
    ys = np.sort(y)[::-1]
    print "Case #{}: {}".format(i,np.inner(xs,ys))