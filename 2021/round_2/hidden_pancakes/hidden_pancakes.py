def num_visible(stack):
    i = 1
    top = stack[0]
    for j in stack[1:]:
        if j > top:
            i += 1
            top = j
        else:
            break
    return i


def run(N, V):
    stacks = [[]]
    new_stacks = []
    for i, v in enumerate(V):
        for stack in stacks:
            new_stack = [i] + stack
            print(num_visible(new_stack), v)
            if num_visible(new_stack) == v:
                new_stacks.append(new_stack)
        stacks, new_stacks = new_stacks, []
        print(stacks, new_stacks)
    return len(new_stacks)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    V = [int(i) for i in input().split()]
    result = run(N, V)
    print(f"Case #{t}: {result}")
