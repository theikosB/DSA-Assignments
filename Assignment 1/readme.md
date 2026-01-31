# Random Number Generation and QuickSort (Optional Randomness Check)

## Overview
This project demonstrates:
- Custom pseudo-random number generation using **Xoroshiro128+**, developed by [Blackman&Vigna2018](https://arxiv.org/abs/1805.01407)
- Sorting numbers using **QuickSort**
- Optional randomness analysis

No built-in random generator or sorting functions are used.

---

## Project Structure

- xoroshiro128plus.py → Random number generator
- quicksort.py → QuickSort implementation
- main.py → Program driver


---

## File Details

### xoroshiro128plus.py
Implements the **Xoroshiro128+** pseudo-random number generator.

Main components:
- `Xoroshiro128Plus` – generator class
- `_rotl(x, k)` – rotates bits to mix state
- `next()` – produces next random number
- `random_int(max_value)` – returns number in `[0, max_value)`

The generator keeps an internal 128-bit state and updates it each time a number is produced.

---

### quicksort.py
Implements QuickSort in-place.

Functions:
- `swap(arr, i, j)` – swaps two elements.
- `partition(...)` – rearranges elements around a pivot.
- `quicksort(...)` – recursively sorts the array.

Supports both ascending and descending sorting.

---

### main.py
Controls program execution.

Functions:
- `generate_random_list(...)` – creates random numbers.
- `print_list(...)` – prints arrays cleanly.
- `frequency_distribution(...)` – counts occurrences of numbers.
- `mean_variance_of_frequencies(...)` – computes frequency statistics.
- `randomness_check(...)` – checks distribution uniformity.
- `main()` – runs the program flow.

Program flow:
1. Generate random numbers
2. Show unsorted list
3. Sort numbers
4. Show sorted list
5. Optionally analyze randomness

---

## Running the Program

Run:

```bash
python main.py
