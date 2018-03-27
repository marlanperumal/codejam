def read_int():
    return int(input())

def read_int_list():
    return [int(n) for n in input().split(" ")]

def read_str():
    return input()

def read_char_list():
    return [c for c in input().split(" ")]

def write_case_ans(i,ans):
    if isinstance(ans,list):
        ans = " ".join(map(str, ans))
    print("Case #{}: {}".format(i, ans))

def main():
    t = read_int()
    for i in range(1, t+1):
        n, m = read_int_list()
        stage = [["." for c in range(n)] for r in range(n)]
        places = []
        has_o = False
        has_x = False
        has_p = False
        o_pos = -1
        x_pos = -1
        for j in range(m):
            model = read_char_list()
            model_type = model[0]
            row = int(model[1]) - 1
            col = int(model[2]) - 1
            stage[row][col] = model_type

            if model_type == "o":
                has_o = True
                o_pos = col
            elif model_type == "x":
                has_x = True
                x_pos = col
            else:
                has_p = True

        # for r in range(n):
        #     print(stage[r])

        if has_x:
            places.append(["o", 1, col + 1])
            stage[0][col] = "o"
            has_o = True
            o_pos = col
        if not has_o:
            places.append(["o", 1, 1])
            stage[0][0] = "o"
            o_pos = 0
        for c in range(n):
            if stage[0][c] == ".":
                stage[0][c] = "+"
                places.append(["+", 1, c + 1])

        for c in range(o_pos + 1, n):
            stage[c - o_pos][c] = "x"
            places.append(["x", c - o_pos + 1, c + 1])
        for c in range(o_pos):
            stage[n - c - 1][c] = "x"
            places.append(["x", n - c, c + 1])
        for c in range(1, n-1):
            stage[n-1][c] = "+"
            places.append(["+", n, c + 1])


        for r in range(n):
            print(stage[r])

        write_case_ans(i, [2 if n == 1 else 3*n-2, len(places)])
        # for place in places:
        #     print(" ".join(map(str, place)))

if __name__ == "__main__":
    main()
