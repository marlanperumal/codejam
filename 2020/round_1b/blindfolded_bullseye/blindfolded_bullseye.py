T, A, B = [int(i) for i in input().split()]
for t in range(1, T + 1):
    max_tries = 300
    tries = 0
    done = False
    for x in range(-5, 6):
        for y in range(-5, 6):
            tries += 1
            print(x, y)
            result = input()
            if result == "CENTER":
                done = True
            elif result == "WRONG":
                exit
            if done or tries >= max_tries:
                break
        if done or tries >= max_tries:
            break
