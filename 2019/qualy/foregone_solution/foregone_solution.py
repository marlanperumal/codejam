T = int(input())

for t in range(1, T + 1):
    N = input()
    B = int("".join(["1" if i == "4" else "0" for i in N]))
    A = int(N.replace("4", "3"))
    assert(int(N) == A + B)

    print("Case #{}: {} {}".format(t, A, B))
