def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found

    return -1  # Return -1 if the target is not present in the array

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
