#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random
import math
from itertools import combinations

limit = 10000

def can_add(p, template):
  if template[0] == -1:
    if p == template[1]:
      return True, template
    elif p[0] == template[1][0]:
      return True, (0, template[1][0])
    elif p[1] == template[1][1]:
      return True, (1, template[1][1])
    else:
      return True, (2, template[1], p)
  elif template[0] == 0:
    if p[0] == template[1]:
      return True, (0, template[1])
    else:
      return True, (3, template[1], p[1])
  elif template[0] == 1:
    if p[1] == template[1]:
      return True, (1, template[1])
    else:
      return True, (3, p[0], template[1])
  elif template[0] == 2:
    if p == template[1] or p == template[2]:
      return True, template
    elif p[0] == template[1][0] or p[1] == template[2][1]:
      return True, (3, template[1][0], template[2][1])
    elif p[0] == template[2][0] or p[1] == template[1][1]:
      return True, (3, template[2][0], template[1][1])
    else:
      return False, None
  elif template[0] == 3:
    if p[0] == template[1] or p[1] == template[2]:
      return True, template
  
  return False, None
  

def solve(n, s):

  sp = []
  #print s
  for d, a, b in s:
    p = (d + a, d -b)
    if len(sp) == 0 or p != sp[-1][1]:
      sp.append([p, 1])
    else:
      sp[1][1] += 1

  #print sp
  
 
  longest = 0
  count = 0
  index = 0
  start = index
  template = -1, sp[start][0]
  length = sp[start][1]
  while index < len(sp):
    if length > longest:
      longest = length
      count = 1
    elif length == longest:
      count += 1
   
    if index == len(sp) -1: break

    index += 1
    r, t = can_add(sp[index][0], template)
    if r:
      template = t
      length += sp[index][1]

    else:
      #backtracking
      template = -1, sp[index][0]
      length = sp[index][1]
      start = index
      while start > 0:
        rp, tp = can_add(sp[start - 1][0], template)
        if not rp: 
          break
        length += sp[start - 1][1]
        start -= 1
        template = tp

  return longest, count

count = None
n = None
tests = None
counter = 0

for line in sys.stdin:
  #print line
  if not count:
    count = int(line.strip())
  elif n is None:
    #print line
    n = int(line.strip())
    tests = []
  else:
    row = [int(x) for x in line.strip().split()]
    tests.append(row)
    if len(tests) == n:
      counter += 1
      s = solve(n, tests)
      print "Case #%d: %d %d" % (counter, s[0], s[1])
      n = None


if count != counter:
  print "Wrong number of test cases"
  sys.exit(0)

