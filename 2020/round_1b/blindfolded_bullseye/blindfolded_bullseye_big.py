T, A, B = [int(i) for i in input().split()]
for t in range(1, T + 1):
    max_tries = 300
    tries = 0
    done = False
    print(A, 0)
    xpos = 1 if input() == "HIT" else 0
    print(-A, 0)
    xneg = 1 if input() == "HIT" else 0
    print(0, A)
    ypos = 1 if input() == "HIT" else 0
    print(0, -A)
    yneg = 1 if input() == "HIT" else 0
    if xpos + ypos + xneg + yneg == 4:  # center
        print(0, 0)
        result = input()
        if result == "CENTER":
            continue
    elif xpos + ypos + xneg + yneg == 1:
        if xpos == 1:
            x0 = A
            x1 = 1e9
            x2 = int((x0 + x1) // 2)
            while x2 != x0 and x2 != x1:
                print(x2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    x0 = x2
                else:
                    x1 = x2
                x2 = int((x0 + x1) // 2)
            print(A - x2, 0)
        elif xneg == 1:
            x0 = -1e9
            x1 = -A
            x2 = int((x0 + x1) // 2)
            while x2 != x0 and x2 != x1:
                print(x2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    x1 = x2
                else:
                    x0 = x2
                x2 = int((x0 + x1) // 2)
            print(x2 - A, 0)
        if ypos == 1:
            y0 = A
            y1 = 1e9
            y2 = int((y0 + y1) // 2)
            while y2 != y0 and y2 != y1:
                print(y2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    y0 = y2
                else:
                    y1 = y2
                y2 = int((y0 + y1) // 2)
            print(A - y2, 0)
        elif yneg == 1:
            y0 = -1e9
            y1 = -A
            y2 = int((y0 + y1) // 2)
            while y2 != y0 and y2 != y1:
                print(y2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    y1 = y2
                else:
                    y0 = y2
                y2 = int((y0 + y1) // 2)
            print(y2 - A, 0)
        result = input()
        if result == "CENTER":
            continue
        else:
            exit
    else:
        if xpos == 1:
            x0 = A
            x1 = 1e9
            x2 = int((x0 + x1) // 2)
            while x2 != x0 and x2 != x1:
                print(x2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    x0 = x2
                else:
                    x1 = x2
                x2 = int((x0 + x1) // 2)
        else:
            x0 = 2 * A - 1e9
            x1 = A
            x2 = int((x0 + x1) // 2)
            while x2 != x0 and x2 != x1:
                print(x2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    x0 = x2
                else:
                    x1 = x2
                x2 = int((x0 + x1) // 2)
        xpos = x2
        if xneg == 1:
            x0 = -1e9
            x1 = -A
            x2 = int((x0 + x1) // 2)
            while x2 != x0 and x2 != x1:
                print(x2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    x1 = x2
                else:
                    x0 = x2
                x2 = int((x0 + x1) // 2)
        else:
            x0 = -A
            x1 = 1e9 - 2 * A
            x2 = int((x0 + x1) // 2)
            while x2 != x0 and x2 != x1:
                print(x2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    x0 = x2
                else:
                    x1 = x2
                x2 = int((x0 + x1) // 2)
        xneg = x2
        if ypos == 1:
            y0 = A
            y1 = 1e9
            y2 = int((y0 + y1) // 2)
            while y2 != y0 and y2 != y1:
                print(y2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    y0 = y2
                else:
                    y1 = y2
                y2 = int((y0 + y1) // 2)
        else:
            y0 = 2 * A - 1e9
            y1 = A
            y2 = int((y0 + y1) // 2)
            while y2 != y0 and y2 != y1:
                print(y2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    y0 = y2
                else:
                    y1 = y2
                y2 = int((y0 + y1) // 2)
        ypos = y2
        if yneg == 1:
            y0 = -1e9
            y1 = -A
            y2 = int((y0 + y1) // 2)
            while y2 != y0 and y2 != y1:
                print(y2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    y1 = y2
                else:
                    y0 = y2
                y2 = int((y0 + y1) // 2)
        else:
            y0 = -A
            y1 = 1e9 - 2 * A
            y2 = int((y0 + y1) // 2)
            while y2 != y0 and y2 != y1:
                print(y2, 0)
                hit = True if input() == "HIT" else False
                if hit:
                    y0 = y2
                else:
                    y1 = y2
                y2 = int((y0 + y1) // 2)
        yneg = y2
        print((xpos + xneg) // 2, (ypos + yneg) // 2)
        result = input()
        if result == "CENTER":
            continue
        else:
            exit

