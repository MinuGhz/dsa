def find_pair_sorted(arr, k):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == k:
            return (arr[left], arr[right])
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return None


def find_pair_unsorted(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == k:
            return (arr[left], arr[right])
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return None


sorted_array = [1, 2, 3, 4, 5, 6]
unsorted_array = [4,2,6,1,7]
k = 9
result_sorted = find_pair_sorted(sorted_array, k)
print(result_sorted)
result_unsorted = find_pair_unsorted(unsorted_array, k)
print(result_unsorted)
