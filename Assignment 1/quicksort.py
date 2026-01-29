"""
  QuickSort Algorithm Implementation
"""


def swap(arr, i, j):
    """
    Swap two elements in a list.

    Parameters:-
    arr : The list in which elements are swapped
    i : Index of first element
    j : Index of second element
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high, ascending=True):
    """
    Partition the array (comparing with the pivot) around a pivot element.

    Parameters:-
    arr : The list being sorted
    low : Starting index of the sub-array
    high : Ending index of the sub-array
    ascending : 
        True  → sort in increasing order
        False → sort in decreasing order

    Returns:-
    Final index position of the pivot
    """

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
    """
    This function sorts the array in-place using recursion.

    Parameters:-
    arr : List of elements to be sorted
    low : Starting index of the current segment
    high : Ending index of the current segment
    ascending :
        True  → increasing order
        False → decreasing order
    """

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

