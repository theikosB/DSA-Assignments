"""
  Main Driver Program

  This file integrates:
    - Xoroshiro128+ random number generator
    - QuickSort sorting algorithm
"""

# Import custom PRNG
from xoroshiro128plus import Xoroshiro128Plus

# Import custom QuickSort
from quicksort import quicksort

# For randomness check
from collections import defaultdict   


def generate_random_list(prng, size):
    """
    Generate a list of random integers using a custom PRNG.

    Parameters:-
    prng : Xoroshiro128Plus
    size : Number of random integers to generate
        
    Returns:-
    List of pseudo-random integers
    """

    numbers = []
    for _ in range(size):
        numbers.append(prng.random_int(size))

    return numbers


def print_list(lst, title, limit=20):
    """
    Print a list in a readable format.

    Parameters:-
    lst : List to be printed
    title : Title message
    limit : Maximum number of elements to display
    """

    print(title)

    if len(lst) <= limit:
        print(lst)
    else:
        print(lst[:limit], "...", f"(total {len(lst)} elements)")

    print()


# Randomness Check Utilities
def frequency_distribution(numbers):
    """
    Compute frequency of each generated number
    """
    freq = defaultdict(int)
    for num in numbers:
        freq[num] += 1
    return freq

def mean_variance_of_frequencies(freq_dict):
    """
    Compute mean and variance of frequencies
    """
    freqs = list(freq_dict.values())
    n = len(freqs)

    if n == 0:
        return 0, 0

    mean = sum(freqs) / n
    var = sum((f - mean) ** 2 for f in freqs) / n

    return mean, var

def randomness_check(numbers):
    """
    Perform a simple randomness check using
    frequency mean and variance
    """

    print("\nRandomness Check:-")

    freq = frequency_distribution(numbers)

    mean, var = mean_variance_of_frequencies(freq)

    print(f"Total numbers generated : {len(numbers)}")
    print(f"Unique values           : {len(freq)}")
    print(f"Mean frequency          : {mean:.4f}")
    print(f"Variance of frequencies : {var:.4f}")

    print("\nInterpretation:")

    if var < mean:
        print("→ Distribution looks reasonably uniform.")
    else:
        print("→ Distribution shows noticeable non-uniformity/clustering.")

    print("\nSample frequencies (first 15 values):")
    for i, (k, v) in enumerate(freq.items()):
        if i >= 15:
            break
        print(f"Value {k} → {v} times")

    print()


def main():
    """
    Main execution function
    """

    # Configuration Parameters
    N = 10  # Number of random integers
    ASCENDING = True  # Sorting order (True = increasing, False = decreasing)

    # Initialize PRNG
    prng = Xoroshiro128Plus()

    # Generate Random Numbers
    random_numbers = generate_random_list(prng, N)

    # Display Before Sorting
    print_list(random_numbers, "Random Numbers (Before Sorting):")

    # Sort Using QuickSort
    quicksort(random_numbers, ascending=ASCENDING)

    # Display After Sorting
    order = "Ascending" if ASCENDING else "Descending"
    print_list(random_numbers, f"Random Numbers (After Sorting - {order} Order):")

    # Optional Randomness Check
    choice = input("Do you want to check the randomness? (y/n): ").strip().lower()

    if choice in ("y", "yes"):
        randomness_check(random_numbers)
    else:
        print("\nRandomness check skipped.\n")


if __name__ == "__main__":
    main()
