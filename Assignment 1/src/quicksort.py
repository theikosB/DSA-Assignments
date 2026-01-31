def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high, ascending=True):
    # Choose pivot (here we use the last element)
    pivot = arr[high]

    # i marks the boundary of smaller elements
    i = low - 1

    # Traverse through sub-array
    for j in range(low, high):
        if ascending:
            condition = arr[j] < pivot
        else:
            condition = arr[j] > pivot

        if condition:
            i += 1
            swap(arr, i, j)

    # Place pivot in correct position
    swap(arr, i + 1, high)

    return i + 1


def quicksort(arr, low=0, high=None, ascending=True):
    # Initialize high index on first call
    if high is None:
        high = len(arr) - 1

    # Base condition: stop recursion
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high, ascending)

        # Recursively sort left part
        quicksort(arr, low, pivot_index - 1, ascending)

        # Recursively sort right part
        quicksort(arr, pivot_index + 1, high, ascending)

