from collections import defaultdict

T = int(input())

for t in range(1, T + 1):
    N, Q = [int(i) for i in input().split()]
    bookings = [[int(i) for i in input().split()] for q in range(Q)]

    contention = defaultdict(int)
    for L, R in bookings:
        for i in range(L, R + 1):
            contention[i] += 1

    free_bookings = []

    for q in range(Q):
        max_free = 0
        max_pos = 0
        uncontended_seats = set([seat for seat in contention if contention[seat] == 1])
        for i, [L, R] in enumerate(bookings):
            seats = list(range(L, R + 1))
            num_free = len(set(seats) & uncontended_seats)
            if num_free > max_free:
                max_free = num_free
                max_pos = i
        free_bookings.append(max_free)
        if max_free == 0:
            break
        L, R = bookings.pop(i)
        for seat in range(L, R + 1):
            contention[seat] -= 1

    print("Case #{}: {}".format(t, min(free_bookings)))
