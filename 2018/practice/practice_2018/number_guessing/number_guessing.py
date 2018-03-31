T = int(input())
for t in range(1, T+1):
    A, B = [int(si) for si in input().split()]
    N = int(input())
    correct = False
    while not correct and N > 0:
        guess = (A + B + 1)//2
        print(guess, flush=True)
        response = input()
        if response == "CORRECT":
            break
        elif response == "TOO_SMALL":
            A = guess
        elif response == "TOO_BIG":
            B = guess
        elif response == "WRONG_ANSWER":
            exit()
        N -= 1
