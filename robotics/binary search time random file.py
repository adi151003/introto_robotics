import random
import timeit

# Function to perform a binary search in a sorted file for a given target number and measure time
def binary_search_with_timing(filename, target):
    try:
        start_time = timeit.default_timer()  # Record the start time
        with open(filename, "r") as file:
            lines = file.readlines()
            left, right = 0, len(lines) - 1

            while left <= right:
                mid = (left + right) // 2
                current = int(lines[mid].strip())

                if current == target:
                    end_time = timeit.default_timer()  # Record the end time when the number is found
                    elapsed_time = (end_time - start_time) * 1e6  # Calculate elapsed time in microseconds
                    return mid, True, elapsed_time
                elif current < target:
                    left = mid + 1
                else:
                    right = mid - 1

            end_time = timeit.default_timer()  # Record the end time if the number is not found
            elapsed_time = (end_time - start_time) * 1e6  # Calculate elapsed time in microseconds
            return -1, False, elapsed_time
    except FileNotFoundError:
        return -1, False, None  # If file not found, return -1 and no elapsed time

# Generate a sorted list of numbers from 1 to n and write them to a file

def generate_sorted_numbers_file(filename, n):
    numbers_list = list(range(1, n + 1))
    with open(filename, "w") as file:
        for number in numbers_list:
            file.write(f"{number}\n")

# Get user input for the target number and n (maximum number)
try:
    n = int(input("Enter the maximum number (n): "))
    target_number = int(input("Enter the number you want to find: "))
    filename = "sorted_numbers.txt"

    # Generate the sorted numbers file (if not already created)
    generate_sorted_numbers_file(filename, n)

    index, found, elapsed_time = binary_search_with_timing(filename, target_number)

    if found:
        print(f"{target_number} found in the file at index {index}.")
        if elapsed_time is not None:
            print(f"Binary search took {elapsed_time:.6f} microseconds.")
    else:
        print(f"{target_number} not found in the file.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")

