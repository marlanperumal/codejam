values = [60, 100, 120]
weights = [10, 20, 30]

W = 50

dp_table = {(0, 0): 0}


def pack(num_items, max_weight):
    print(num_items, max_weight)
    if (num_items, max_weight) in dp_table:
        return dp_table[(num_items, max_weight)]
    else:
        if max_weight <= 0 or num_items == 0:
            dp_table[(num_items, max_weight)] = 0
            return 0
        elif weights[num_items - 1] > W:
            test_value = 0
        else:
            test_value = values[num_items - 1] + pack(num_items - 1, max_weight - weights[num_items - 1])
        best_value = max(test_value, pack(num_items - 1, max_weight))
        dp_table[(num_items, max_weight)] = best_value
        return best_value


print(pack(3, 50))
