T = int(input())
for t in range(1, T+1):
    N = int(input())
    W = [int(si) for si in input().split()]
    stack = [W[0]]
    for w in W[1:]:
        if sum(stack) <= w*6:
            stack = [w] + stack
        else:
            max_stack = max(stack)
            if w < max_stack and sum(stack) - max_stack <= w*6:
                stack.pop(stack.index(max_stack))
                stack = [w] + stack
    ans = len(stack)
    print("Case #{}: {}".format(t, ans))
