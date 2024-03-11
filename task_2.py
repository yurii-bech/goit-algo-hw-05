def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if right >= 0 and right < len(arr) - 1:
        return iterations, arr[right + 1]
    elif right == len(arr) - 1:
        return iterations, arr[right]
    else:
        return iterations, None

arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

def bound(arr, target):
    iterations, upper_bound = binary_search(arr, target)
    return iterations, upper_bound

print(bound(arr, 3.5))
print(bound(arr, 6.0))