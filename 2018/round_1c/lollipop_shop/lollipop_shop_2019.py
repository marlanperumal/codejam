from sys import stdout
from collections import defaultdict

T = int(input())

for t in range(1, T + 1):
    response = input()
    if response == "-1":
        exit()
    N = int(response)
    
    available = set(list(range(N)))
    preferences = defaultdict(int)
    for n in range(N):
        response = input()
        if response == "-1":
            exit()
        D = [int(i) for i in response.split()]
        if D[0] == 0:
            print("-1")
            stdout.flush()
        else:
            D = D[1:]
            served = False
            for d in D:
                if not served and d not in preferences and d in available:
                    served = True
                    available.remove(d)
                    print(d)
                    stdout.flush()
                preferences[d] += 1
            if not served:
                possible = set(D) & available
                if len(possible) > 0:
                    d = min(possible, key=lambda x: preferences[x])
                    served = True
                    available.remove(d)
                    print(d)
                    stdout.flush()
                else:
                    print("-1")
                    stdout.flush()
