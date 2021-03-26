def run(X, Y, S):
    S = S.replace("?", "")
    if len(S) <= 1:
        return 0

    current_letter = S[0]
    x = 0
    y = 0
    for s in S[1:]:
        if s != current_letter:
            if s == "J":
                x += 1
            elif s == "C":
                y += 1
            current_letter = s

    return x * X + y * Y


T = int(input())

for t in range(1, T + 1):
    X, Y, S = input().split()
    X, Y = int(X), int(Y)
    result = run(X, Y, S)
    print(f"Case #{t}: {result}")
