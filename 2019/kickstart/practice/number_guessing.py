T = int(input())

error = False
for t in range(1, T + 1):
    A, B = [int(i) for i in input().split()]
    N = int(input())
    done = False
    for i in range(N):
        guess = (A + B + 1) // 2
        print(guess)
        response = input()
        if response == "TOO_BIG":
            B = guess
        elif response == "TOO_SMALL":
            A = guess
        elif response == "CORRECT":
            done = True
            break
        else:
            error = True
            break
    if not done or error:
        break