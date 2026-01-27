"""
  Main Driver Program

  This file integrates:
    - Xoroshiro128+ random number generator
    - QuickSort sorting algorithm
"""

# Import custom PRNG
from Xoroshiro128Plus import Xoroshiro128Plus

# Import custom QuickSort
from quicksort import quicksort


def generate_random_list(prng, size, max_value):
    """
    Generate a list of random integers using a custom PRNG.

    Parameters:-
    prng : Xoroshiro128Plus
        Instance of the custom random number generator
    size : int
        Number of random integers to generate
    max_value : int
        Upper bound for random values (exclusive)

    Returns:-
    list
        List of pseudo-random integers
    """

    numbers = []
    for _ in range(size):
        numbers.append(prng.random_int(max_value))

    return numbers


def print_list(lst, title, limit=20):
    """
    Print a list in a readable format.

    Parameters:-
    lst : list
        List to be printed
    title : str
        Title message
    limit : int
        Maximum number of elements to display
    """

    print(title)

    if len(lst) <= limit:
        print(lst)
    else:
        print(lst[:limit], "...", f"(total {len(lst)} elements)")

    print()


def main():
    """
    Main execution function.
    """

    # Configuration Parameters
    N = 1000          # Number of random integers
    MAX_VALUE = 10000 # Range: 0 to MAX_VALUE-1
    ASCENDING = True  # Sorting order (True = increasing, False = decreasing)

    # Initialize PRNG
    prng = Xoroshiro128Plus()

    # Generate Random Numbers
    random_numbers = generate_random_list(prng, N, MAX_VALUE)

    # Display Before Sorting
    print_list(random_numbers, "Random Numbers (Before Sorting):")

    # Sort Using QuickSort
    quicksort(random_numbers, ascending=ASCENDING)

    # Display After Sorting
    order = "Ascending" if ASCENDING else "Descending"
    print_list(random_numbers, f"Random Numbers (After Sorting - {order} Order):")


if __name__ == "__main__":
    main()
