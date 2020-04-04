# prices = [1, 5, 8, 9, 10, 17, 17, 20]
prices = [3, 5, 8, 9, 10, 17, 17, 20]
max_length = len(prices)

dp_table = [[0] * (max_length + 1)]

for cut_size in range(1, max_length + 1):
    row = []
    dp_table.append(row)
    for length in range(max_length + 1):
        if cut_size > length:
            test_value = 0
        else:
            test_value = prices[cut_size - 1] + dp_table[cut_size][length - cut_size]
        row.append(max(test_value, dp_table[cut_size - 1][length]))

print(dp_table)
