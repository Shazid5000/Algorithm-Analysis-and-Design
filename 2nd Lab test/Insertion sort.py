def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        # Display the current state of the array after each iteration
        print(f"Iteration {i}: {arr}")

# Get user input for the array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Display the unsorted array
print("Unsorted array:", arr)

# Apply Insertion Sort and display each step
insertion_sort(arr)

# Display the sorted array
print("Sorted array:", arr)