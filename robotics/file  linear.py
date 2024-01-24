# Function to perform a linear search in a file for a given target number
def linear_search_with_index(filename, target):
    try:
        with open(filename, "r") as file:
            for index, line in enumerate(file):
                if int(line.strip()) == target:
                    return index, True
        return -1, False
    except FileNotFoundError:
        return -1, False

# Get user input for the target number
try:
    target_number = int(input("Enter the number you want to find: "))
    filename = "sorted_numbers.txt"  # Replace with the actual file path

    index, found = linear_search_with_index(filename, target_number)

    if found:
        print(f"{target_number} found in the file at index {index}.")
    else:
        print(f"{target_number} not found in the file.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
