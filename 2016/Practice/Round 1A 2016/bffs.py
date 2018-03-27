# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:17:37 2016

@author: marlan
"""

class Child(object):
    def __init__(self, id, bff):
        self.id = id
        self.bff = bff
        self.loop_num = 0
        self.popped = False
        self.is_doubleton = False
        self.is_singleton = False
        self.longest_route_to = 0
        
class Kindergarten(object):
    def __init__(self):
        self.children = []
        self.bff_dict = {}
        
    def add_child(self, id, bff):
        self.children.append(Child(id,bff))
        if bff in self.bff_dict:
            self.bff_dict[bff] = self.bff_dict[bff] + 1
        else:
            self.bff_dict[bff] = 1
        if bff < id:
            if self.children[bff].bff == id:
                self.children[id].is_doubleton = True
                self.children[bff].is_doubleton = True
                
    def check_singlets(self):
        for child in self.children:
            if child.id not in self.bff_dict:
                child.is_singleton = True
        
t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    rc = [int(m) for m in raw_input().split(" ")]
    longest = 0
    longest_loop = []
    kindergarten = Kindergarten()
    
    for j, bff in enumerate(rc):
        kindergarten.add_child(j, bff-1)
    kindergarten.check_singlets()
    for child in kindergarten.children:
        if child.popped:
            pass
        else:
            curr_child = child
            loop = [curr_child.id+1]
            loop_num = 1
            curr_child.loop_num = loop_num
            next_child = kindergarten.children[child.bff]
            loop_closed = False
            while not next_child.popped and not loop_closed:
                loop_num = loop_num + 1
                if next_child.loop_num == 0:
                    curr_child = next_child
                    loop.append(curr_child.id+1)
                    next_child = kindergarten.children[curr_child.bff]
                    curr_child.loop_num = loop_num
                else:
                    loop_len = loop_num - next_child.loop_num
                    if loop_len > longest:
                        longest = loop_len
                        longest_loop = loop
                    loop_closed = True
            child.popped = True
            next_child = kindergarten.children[child.bff]
            while not next_child.popped:
                next_child.popped = True
                next_child = kindergarten.children[next_child.bff]
    
    for child in kindergarten.children:
        child.popped = False
        
    for child in kindergarten.children:
        if child.is_singleton:
            path_len = 1
            next_child = kindergarten.children[child.bff]
            while not next_child.popped:
                next_child.popped = True
                if next_child.is_doubleton:
                    if next_child.longest_route_to < path_len:
                        next_child.longest_route_to = path_len
                    break
                else:
                    path_len = path_len + 1
                    next_child = kindergarten.children[next_child.bff]
            next_child = kindergarten.children[child.bff]
            while next_child.popped:
                next_child.popped = False
                next_child = kindergarten.children[next_child.bff]
    
    path_len = 0            
    for child in kindergarten.children:
        
        if child.is_doubleton:
            bff = kindergarten.children[child.bff]
            path_len = path_len + child.longest_route_to + bff.longest_route_to + 2
    path_len = path_len / 2
    if path_len > longest:
        longest = path_len
                        
                    
                    
                    
    print "Case #{}: {}".format(i,longest)
#    print longest_loop