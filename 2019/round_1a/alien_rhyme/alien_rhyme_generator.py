from random import randint

N = 1000
wl = 50

print(1)
print(N)
for n in range(int(N)):
    print("".join([chr(randint(0, 25) + 65) for i in range(wl)]))
