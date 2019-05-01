from random import uniform, random
T = 1
N = 200
print(T)
for t in range(1, T + 1):
    print(N)
    popularity = [uniform(0.005, 0.1) for n in range(N)]
    for n in range(N):
        D = [i for i in range(N) if random() < popularity[i]]
        D = [len(D)] + D
        print(" ".join([str(d) for d in D]))
    print(1)