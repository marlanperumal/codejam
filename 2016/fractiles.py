# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:48:11 2016

@author: marlan
"""

def drive_fractiles():
    t = int(raw_input())
    for i in xrange(1, t + 1):        
        k, c, s = [int(sin) for sin in raw_input().split(" ")]
        sout = ""
        for j in xrange(s):
            sout = sout + str((j+1)*k**(c-1)) + " "
        sout = sout[:-1]            
        print "Case #{}: {}".format(i, sout)
    
if __name__ == '__main__':
    drive_fractiles()