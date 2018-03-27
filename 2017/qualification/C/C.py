from operator import attrgetter

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

class Stall():
    def __init__(self, pos, n):
        self.pos = pos
        self.rpos = n - pos - 1
        self.occupied = False
        self.L = 0
        self.R = 0
        self.max_LR = 0
        self.min_LR = 0

    @property
    def open(self):
        return 1 if not self.occupied else 0

    def __repr__(self):
        return str(self.pos)

def main():
    t = read_int()
    for j in range(1, t+1):
        n, k = read_int_list()
        stalls = [Stall(i, n) for i in range(n)]
        # print("Num stalls:", n)
        for i in range(k):
            # print([stall.pos for stall in stalls])
            # print("Person:", i)
            # print([1 if stall.occupied else 0 for stall in stalls])
            last_left = -1
            last_right = n
            for stall in stalls:
                if not stall.occupied:
                    stall.L = stall.pos - last_left - 1
                else:
                    stall.L = 0
                    last_left = stall.pos
            for stall in reversed(stalls):
                if not stall.occupied:
                    stall.R = last_right - stall.pos - 1
                else:
                    stall.R = 0
                    last_right = stall.pos
            for stall in stalls:
                stall.min_LR = min(stall.L, stall.R)
                stall.max_LR = max(stall.L, stall.R)

            sorted_stalls = sorted(stalls, key=attrgetter('open', 'min_LR', 'max_LR', 'rpos'), reverse=True)
            selected_stall = sorted_stalls[0]
            selected_stall.occupied = True
        write_case_ans(j, [selected_stall.max_LR, selected_stall.min_LR])


if __name__ == "__main__":
    main()
