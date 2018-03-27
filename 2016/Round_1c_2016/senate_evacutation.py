# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:22:52 2016

@author: marlan
"""

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
        ans = " ".join(map(str, ans))
    print("Case #{}: {}".format(i, ans))
    
def main():
    t = read_int()
    for i in range(t):
        n = read_int()
        p_list = read_int_list()
        parties = [chr(c+ ord("A")) for c in range(n)]
        s_heap = [[party, senators] for party, senators in zip(p_list,parties)]
        s_heap.sort(reverse=True)
        done = False
        h_id = 0
        ans_str = ""
        while not done:
            if len(s_heap) == 2:
                if s_heap[0][0] > s_heap[1][0]:
                    ans_str += s_heap[0][1] + " "
                    s_heap[0][0] -= 1
                else:
                    ans_str += s_heap[0][1] + s_heap[1][1] + " "
                    s_heap[0][0] -= 1
                    s_heap[1][0] -= 1
                if s_heap[0][0] == 0:
                    done = True
            else:
                while h_id < len(s_heap) - 1 and s_heap[h_id][0] == s_heap[h_id+1][0]:
                    h_id += 1
                j = 0
                while j < h_id + 1 and len(s_heap) > 2:
                    ans_str += s_heap[j][1] + " "
                    s_heap[j][0] -= 1
                    if s_heap[j][0] == 0:
                        s_heap.pop(j)
                        h_id -= 1
                    else:
                        j += 1
        write_case_ans(i+1, ans_str[:-1])
        

if __name__ == "__main__":
    main()