N = 100

fib_memo = {1: 1, 2: 1}


def fib(i):
    if i in fib_memo:
        return fib_memo[i]
    else:
        fib_i = fib(i-1) + fib(i-2)
        fib_memo[i] = fib_i
        return fib_i


for i in range(1, N + 1):
    print(fib(i))
