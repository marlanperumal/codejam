import operator

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
    for t in range(1, T+1):
        N, R, O, Y, G, B, V = read_int_list()
        if B > Y + R or Y > R + B or R > B + Y:
            write_case_ans(t, "IMPOSSIBLE")
        else:
            ponies = {"B": B, "Y": Y, "R": R}
            sorted_ponies = sorted(ponies, key=ponies.get, reverse=True)
            most_ponies = sorted_ponies[0]
            stables = [most_ponies]*ponies[most_ponies]
            stable = 0
            for pony in sorted_ponies[1:]:
                for p in range(ponies[pony]):
                    stables[stable] = stables[stable] + pony
                    stable += 1
                    if stable >= ponies[most_ponies]:
                        stable = 0
            write_case_ans(t, "".join(stables))



            # blues = ["B"]*B
            # yellows = ["Y"]*Y
            # reds = ["R"]*R

        # write_case_ans(t, N)


if __name__ == "__main__":
    main()
