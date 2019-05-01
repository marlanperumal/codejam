from collections import defaultdict


def run(N, Q, letters, L, R):
    num_palindromes = 0
    for q in range(Q):
        P = letters[L[q] - 1:R[q]]
        letter_counts = defaultdict(int)
        for p in P:
            letter_counts[p] += 1
        num_odd = 0
        for l in letter_counts:
            i = letter_counts[l]
            if i % 2 == 1:
                num_odd += 1
            if num_odd > 1:
                break
        if num_odd in [0, 1]:
            num_palindromes += 1
    return num_palindromes


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, Q = [int(i) for i in input().split()]
        letters = input()
        L = []
        R = []
        for q in range(Q):
            l, r = [int(i) for i in input().split()]
            L.append(l)
            R.append(r)
        result = run(N, Q, letters, L, R)
        print("Case #{}: {}".format(t, result))
