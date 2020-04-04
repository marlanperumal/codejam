prices = [1, 5, 8, 9, 10, 17, 17, 20]
# prices = [3, 5, 8, 9, 10, 17, 17, 20]
max_length = len(prices)

dp_table = {(0, 0): 0}


def cut_rod(cut_size, length):
    if (cut_size, length) in dp_table:
        return dp_table[(cut_size, length)]
    else:
        if cut_size == 0:
            dp_table[(cut_size, length)] = 0
            return 0
        elif cut_size > length:
            test_value = 0
        else:
            test_value = prices[cut_size - 1] + cut_rod(cut_size, length - cut_size)
        best_value = max(test_value, cut_rod(cut_size - 1, length))
        dp_table[(cut_size, length)] = best_value
        return best_value


print(cut_rod(8, 8))
