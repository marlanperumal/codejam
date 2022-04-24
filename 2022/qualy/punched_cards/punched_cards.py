T = int(input())

for t in range(1, T + 1):
    print(f"Case #{t}:")
    R, C = [int(i) for i in input().split()]
    for r in range(2 * R + 1):
        for c in range(2 * C + 1):
            if r < 2 and c < 2:
                print(".", end="")
            elif r % 2 == 1:
                if c % 2 == 1:
                    print(".", end="")
                else:
                    print("|", end="")
            else:
                if c % 2 == 1:
                    print("-", end="")
                else:
                    print("+", end="")
        print()