def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found in the array

# Take user input for the list
user_input = input("Enter a sorted list of numbers separated by spaces: ")
my_list = [int(x) for x in user_input.split()]

# Take user input for the target value
target = int(input("Enter the target value to search for: "))

result = binary_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

