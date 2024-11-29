import heapq


def k_smallest_elements(arr, k):

    min_heap = arr[:]
    heapq.heapify(min_heap)


    smallest_elements = []
    for _ in range(k):
        smallest_elements.append(heapq.heappop(min_heap))


    smallest_elements.sort()

    return smallest_elements



arr = [3,60,32,12,4,57,18,12, 46]
k = 5
result = k_smallest_elements(arr, k)
print(result)
