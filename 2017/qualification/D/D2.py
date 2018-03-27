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
    T = read_int()
    for t in range(1, T + 1):
        N, M = read_int_list()
        starting_placements = []
        for m in range(m):
            grid = [["." for c in range(N)] for r in range(N)]
            p_grid = [["." for c in range(N)] for r in range(N)]
            c_grid = [["." for c in range(N)] for r in range(N)]
            model = read_char_list()
            model_type = model[0]
            row = model[1] - 1
            col = model[2] - 1

            if model_type = '+':
                p_grid[row][col] = '+'
                grid[row][col] = '+'
            elif model_type = 'x':
                c_grid[row][col] = 'x'
                grid[row][col] = 'x'
            elif model_type = 'o':
                p_grid[row][col] = '+'
                c_grid[row][col] = 'x'
                grid[row][col] = 'o' 
        write_case_ans(i, [2 if n == 1 else 3*n-2, len(places)])

if __name__ == "__main__":
    main()
