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
        N, P = read_int_list()
        recipe = read_int_list()
        ingredients = []
        possible_packs = {}
        for n in range(N):
            r = recipe[n]
            rl = ceil(9*r/10)
            rh = ceil(11*r/10)
            ingredient = read_int_list()
            for i in ingredient:
                il = i//rh
                ih = i//rl
                if ih > 0:
                    for p in range(il, ih+1):
                        if p not in possible_packs:
                            possible_packs[p] = [0]*N
                        possible_packs[p][n] += 1
            ingredients.append(ingredient)
        for p in possible_packs:
            pack = possible_packs[p]





if __name__ == "__main__":
    main()
