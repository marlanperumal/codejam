from collections import defaultdict
from itertools import groupby


def run(S, D, A, B):
    # This will probably require some input arguments
    M = [d + a for d, a in zip(D, A)]
    N = [d - b for d, b in zip(D, B)]
    
    Ms = set(M)
    Ns = set(N)
    run_lengths = defaultdict(set)
    
    for m in Ms:
        for n in Ns:
            sign_runs = [i if mi == m or ni == n else -1 
                     for i, [mi, ni] in enumerate(zip(M, N))]
            sign_runs =[
                list(y) for x, y in groupby(sign_runs, lambda z: z == -1) if not x
            ]
            for sign_run in sign_runs:
                run_lengths[len(sign_run)].add(sign_run[0])
    max_run_length = max(run_lengths)
    return "{} {}".format(max_run_length, len(run_lengths[max_run_length]))


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        # There will probably be some additional inputs
        S = int(input())
        D = []
        A = []
        B = []
        for s in range(S):
            d, a, b = [int(i) for i in input().split()]
            D.append(d)
            A.append(a)
            B.append(b)
        result = run(S, D, A, B)
        print("Case #{}: {}".format(t, result))