def run(N, Q, letters, L, R):
    num_palindromes = 0
    alphabet = set(letters)
    letter_counts = {
        letter: [0] for letter in alphabet
    }
    for letter in letters:
        for a in alphabet:
            if letter == a:
                letter_counts[a].append(letter_counts[a][-1] + 1)
            else:
                letter_counts[a].append(letter_counts[a][-1])
    for q in range(Q):
        l, r = L[q] - 1, R[q]
        P = [letter_counts[a][r] - letter_counts[a][l] for a in alphabet]
        num_odd = 0
        for p in P:
            if p % 2 == 1:
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
