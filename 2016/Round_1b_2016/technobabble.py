# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:07:35 2016

@author: marlan
"""
import collections

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
        topics = []
        for j in range(n):
            topics.append(read_str())
        print("***")
        split_topics = [words.split(" ") for words in topics]
        first_words = [words[0] for words in split_topics]
        second_words = [words[1] for words in split_topics]
        first_word_dict = collections.defaultdict(int)
        second_word_dict = collections.defaultdict(int)
        repeat_first_words = collections.defaultdict(int)
        repeat_second_words = collections.defaultdict(int)
        unique_first_words = collections.defaultdict(int)
        unique_second_words = collections.defaultdict(int)
        repeat_topics = 0
        for first_word, second_word in zip(first_words, second_words):
            first_word_dict[first_word] += 1
            second_word_dict[second_word] += 1
        for first_word, second_word in zip(first_words, second_words):
            if first_word_dict[first_word] > 1 and second_word_dict[second_word] > 1:
                repeat_first_words[first_word] += 1
                repeat_second_words[second_word] += 1
                first_word_dict[first_word] -= 1
                second_word_dict[second_word] -= 1
                repeat_topics += 1
            elif first_word_dict[first_word] > 1:
                unique_first_words[first_word] += 1
            elif second_word_dict[second_word] > 1:
                unique_second_words[second_word] += 1
        repeat_topics += len(repeat_first_words.keys())
        repeat_topics += len(repeat_second_words.keys())
        repeat_topics -= len(unique_first_words.keys())
        repeat_topics -= len(unique_second_words.keys())
        write_case_ans(i+1,repeat_topics)
            

if __name__ == "__main__":
    main()