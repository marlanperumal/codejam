from random import choice, randint
T = 10

print(T)
for t in range(T):
    A = 255
    print(A)
    for a in range(A):
        num_moves = randint(1, 5)
        print("".join([choice("RPS") for i in range(num_moves)]))

