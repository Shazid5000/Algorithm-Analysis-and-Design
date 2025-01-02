def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Get user input for the array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Display the unsorted array
print("Unsorted array:", arr)

# Apply Bubble Sort
bubble_sort(arr)

# Display the sorted array
print("Sorted array:", arr)
