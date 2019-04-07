def get_nearest_even(Ns):
    N = int(Ns)
    l = len(Ns)
    has_odds = False
    for i, c in enumerate(Ns):
        if int(c) % 2 == 1:
            has_odds = True
            break

    if not has_odds:
        result = N
    elif l - i == 1:
        result = N - 1
    else:
        lower_even = int(Ns[:i] + ("" if Ns[i] == "1" else str(int(Ns[i]) - 1)) + "".join(["8"]*(l-i-1)))
        if c == "9":
            result = lower_even
        else:
            upper_even = int(Ns[:i] + str(int(c) + 1)) * pow(10, l-i-1)
            result = lower_even if min(N - lower_even, upper_even - N) == N - lower_even else upper_even
    return result

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        Ns = input()
        nearest_even = get_nearest_even(Ns)
        result = abs(int(Ns) - nearest_even)
        print("Case #{t}: {result}".format(t=t, result=result))