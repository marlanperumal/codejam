X = [
    [ 2,  1,  1,  1,  1,  1],
    [ 4,  2,  1,  1,  1,  1],
    [ 8,  2,  2,  1,  1,  1],
    [16,  4,  2,  2,  1,  1],
    [32,  4,  2,  2,  2,  1],
    [64,  8,  4,  2,  2,  2]
]

Xi = [
    [0.1, -0.1, -0.05, 0.0, 0.0, 0.025], 
    [-1.2, 1.2, 0.1, 0.0, 0.0, -0.05], 
    [-0.4, -0.6, 1.2, 0.0, 0, -0.1], 
    [1.6, -1.6, -0.8, 1.0, 0.0, -0.1], 
    [-1.6, 1.6, 0.8, -1.0, 1.0, -0.4], 
    [2.4, -0.4, -1.2, 0.0, -1.0, 0.6]
]

T, W = [int(i) for i in input().split()]

for T in range(T):
    B = []
    for w in range(1, W + 1):
        print(w, flush=True)
        B.append(int(input()))
    R = []
    for i in range(W):
        R.append(round(sum([Xi[i][k]*B[k] for k in range(W)])))
    print(" ".join(str(r) for r in R))
    result = input()
    if result == "-1":
        exit()




# R = [10, 12, 17, 0, 23, 0]

# B = [0]*6
# for i in range(6):
#     B[i] = sum([X[i][k]*R[k] for k in range(6)])

# Y = [0]*6
# for i in range(6):
#     Y[i] = round(sum([Xi[i][k]*B[k] for k in range(6)]))

# print(B)
# print(Y)