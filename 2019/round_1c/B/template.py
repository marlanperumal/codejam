from math import factorial
from collections import defaultdict
# from itertools import permutations
# from random import shuffle
# input_file = "sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)
# o_print = print
# o_input = input

# arrangements = list(permutations("ABCDE"))
# shuffle(arrangements)
# missing_arrangement = arrangements.pop()
# arrangements = "".join(["".join([a for a in arrangement]) for arrangement in arrangements])
# request = 0
# num_guesses = 0


# def print(v, flush=True):
#     global request
#     global num_guesses
#     # o_print("O: ", v)
#     num_guesses += 1
#     request = int(v)


# def input():
#     output = arrangements[request]
#     # o_print("I: ", output)
#     return output


def run():
    # o_print(missing_arrangement)
    members_1 = defaultdict(list)
    members_2 = defaultdict(list)
    members_3 = defaultdict(list)
    missing = []
    for i in range(factorial(5) - 1):
        print(5 * i + 1, flush=True)
        member = input()
        members_1[member].append(5 * i)
    # o_print(members_1)
    for m in members_1:
        if len(members_1[m]) < factorial(4):
            m1 = m
            missing.append(m)
            break
    # o_print("Missing: ", m1)
    for i in range(factorial(4) - 1):
        j = members_1[m1][i] + 1
        print(j + 1, flush=True)
        member = input()
        members_2[member].append(j)
    # o_print(members_2)
    for m in members_2:
        if len(members_2[m]) < factorial(3):
            m2 = m
            missing.append(m)
            break
    # o_print("Missing: ", m2)
    for i in range(factorial(3) - 1):
        j = members_2[m2][i] + 1
        print(j + 1, flush=True)
        member = input()
        members_3[member].append(j)
    # o_print(members_3)
    for m in members_3:
        if len(members_3[m]) < factorial(2):
            m3 = m
            missing.append(m)
            break
    # o_print("Missing: ", m3)
    print(members_3[m3][0] + 1 + 1)
    m5 = input()
    m4 = (set("ABCDE") - set(missing) - set([m5])).pop()
    result = "".join([m1, m2, m3, m4, m5])
    # o_print(result)
    # o_print(num_guesses)
    return result


# T, F = 1, 150
T, F = [int(i) for i in input().split()]
for t in range(1, T + 1):
    result = run()
    print(result)
    verdict = input()
    if verdict == "-1":
        exit()
