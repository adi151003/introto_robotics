import timeit

import random

# Get user input for n (the maximum number)
try:
    n = int(input("Enter the maximum number (n): "))
    filename = "output.txt"  # File to store the randomized numbers

    # Generate a list of numbers from 1 to n
    numbers_list = list(range(1, n + 1))

    # Shuffle the list to randomize the order
    random.shuffle(numbers_list)

    # Write the randomized numbers to the file
    with open(filename, "w") as file:
        for number in numbers_list:
            file.write(f"{number}\n")

    print(f"Randomized numbers from 1 to {n} have been written to {filename}.")
except ValueError:
    print("Invalid input. Please enter a valid number for n.")


# Function to perform a linear search in a file for a given target number and measure time
def linear_search_with_timing(filename, target):
    try:
        start_time = timeit.default_timer()  # Record the start time
        with open(filename, "r") as file:
            for index, line in enumerate(file):
                if int(line.strip()) == target:
                    end_time = timeit.default_timer()  # Record the end time when the number is found
                    elapsed_time = (end_time - start_time) * 1e6  # Calculate elapsed time in microseconds
                    return index, True, elapsed_time
        return -1, False, None  # If not found, return -1 and no elapsed time
    except FileNotFoundError:
        return -1, False, None  # If file not found, return -1 and no elapsed time

# Get user input for the target number
try:
    target_number = int(input("Enter the number you want to find: "))
    filename = "output.txt"  # Replace with the actual file path

    index, found, elapsed_time = linear_search_with_timing(filename, target_number)

    if found:
        print(f"{target_number} found in the file at index {index}.")
        if elapsed_time is not None:
            print(f"Search took {elapsed_time:.6f} microseconds.")
    else:
        print(f"{target_number} not found in the file.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
