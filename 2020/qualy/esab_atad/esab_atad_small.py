T, B = [int(i) for i in input().split()]

for t in range(T):
    result = []
    for i in range(1, B + 1):
        print(i)
        j = input()
        result.append(j)

    print("".join(result))
    response = input()
    if response == "N":
        break
