import heapq


def run(N, W):
    heap = []
    heapq.heappush(heap, -W[0])
    for w in W[1:]:
        sum_heap = sum(heap)
        if -sum_heap <= w*6:
            heapq.heappush(heap, -w)
        else:
            new_heap = []
            for i in range(len(heap)):
                s = heapq.heappop(heap)
                if s - sum_heap <= w*6 and w < -s:
                    heapq.heappush(heap, -w)
                    break
                else:
                    heapq.heappush(new_heap, s)
            heap = list(heapq.merge(heap, new_heap))
    result = len(heap)
    print(heap)
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        W = [int(i) for i in input().split()]
        result = run(N, W)
        print("Case #{}: {}".format(t, result))
