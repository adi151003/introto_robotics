# Function to perform linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Get user input for the list of numbers
input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

# Get the target number to search for
target = int(input("Enter the number to search for: "))

# Perform the linear search
result = linear_search(numbers, target)

# Display the result
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")
