from math import sqrt

def run(cookies, p):
    # This will probably require some input arguments
    W = [cookie[0] for cookie in cookies]
    H = [cookie[1] for cookie in cookies]
    original_perimeter = sum([2*(w + h) for w, h in zip(W, H)])
    target_additional = p - original_perimeter
    upper_bound = sum([8*h for h in H])
    lower_bound = 0
    intervals = []
    previous_interval = [0, 0]
    for w, h in zip(W, H):
        new_interval = [previous_interval[0] + 2*w, previous_interval[1] + 2*sqrt(w**2 + h**2)]
        if target_additional < new_interval[0]:
            upper_bound = new_interval[0]
            break
        elif target_additional <= new_interval[1]:
            upper_bound = target_additional
            lower_bound = target_additional
            break
        else:
            lower_bound = new_interval[1]
            
        intervals.append(new_interval)
        previous_interval = new_interval
    if target_additional - lower_bound < upper_bound - target_additional:
        return original_perimeter + lower_bound
    else:
        return original_perimeter + upper_bound
    

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        # There will probably be some additional inputs
        N, P = [int(i) for i in input().split()]
        cookies = [[int(i) for i in input().split()] for n in range(N)]
        cookies = [[w, h] if w < h else [h, w] for w, h in cookies]
        result = run(cookies, P)
        print("Case #{}: {}".format(t, result))
