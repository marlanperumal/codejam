# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:11:27 2016

@author: marlan
"""

from math import floor, sqrt
def base_m_rep(n, m):
    return long(str(n),m)
    
def find_first_factor(n):
#    for i in xrange(2,long(floor(sqrt(n)))+1):
    for i in xrange(2,min(long(floor(sqrt(n)))+1,10000)):
        if n % i == 0:
            return i
    return None
    
def valid_jamcoin(coin):
    factor_list = []
    for m in range(2,11):
        coinbm = base_m_rep(coin,m)
        first_factor = find_first_factor(coinbm)
        if first_factor is None:
            return None
        else:
            factor_list.append(first_factor)
    return factor_list
    
def drive_coinjam():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        print "Case #{}:".format(i)
        n, j = [int(s) for s in raw_input().split(" ")]
        ncoins = 0
        nmin = 2**(n-1)+1
        nmax = 2**n
        k = nmin
        while ncoins < j and k < nmax:
            coin = bin(k)[2:]
            factor_list = valid_jamcoin(coin)
            if factor_list is not None:
                ncoins = ncoins + 1
                s = str(coin)
                for factor in factor_list:
                    s = s + " " + str(factor)
                print s
            k = k + 2
        print ncoins
    
if __name__ == '__main__':
    drive_coinjam()
    