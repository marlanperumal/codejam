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
        print("Case #{}:".format(t))
        R, C = read_int_list()
        grid = []
        partitions = []

        partition = []
        for r in range(R):
            row = read_str()
            grid.append(row)
            partition.append(row)
            if len(row.strip("?")) > 0:
                partitions.append(partition)
                partition = []
        if partition != []:
            partitions[-1].extend(partition)


        partition_letters = []

        for rp, row_partition in enumerate(partitions):
            num_rows = len(row_partition)
            for row in row_partition:
                if len(row.strip("?")) > 0:
                    bottow_row = row
                    break
            col_partition = []
            l = 0
            letters = []
            for letter in bottow_row:
                l += 1
                if letter != "?":
                    col_partition.append(letter * l)
                    l = 0
                    letters.append(letter)
            if l > 0:
                col_partition[-1] = col_partition[-1] + letters[-1]*l
            partitions[rp] = [col_partition]*num_rows

        # print(partitions)

        for row_partition in partitions:
            for row in row_partition:
                for col in row:
                    print(col, end="")
                print()


if __name__ == "__main__":
    main()
