T = int(input())

for t in range(1, T + 1):
    N = int(input())
    P = input()
    result = "".join(["E" if p == "S" else "S" for p in P])
    
    print("Case #{}: {}".format(t, result))