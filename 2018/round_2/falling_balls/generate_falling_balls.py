n = 4
for i1 in range(n + 1):
    for i2 in range(n - i1 + 1):
        for i3 in range(n - i1 - i2 + 1):
            i4 = n - i1 - i2 - i3
            print(n)
            print(i1, i2, i3, i4)