def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Display the unsorted part of the array
        print(f"Pass {i+1}:")
        print("Unsorted array:", arr[i:])
        
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Display the swapping process
        print(f"Swapping {arr[i]} and {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Display the sorted part of the array
        print("Sorted array:", arr[:i+1])
        print()

# Get user input for the array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Apply Selection Sort
selection_sort(arr)

# Display the final sorted array
print("Sorted array:", arr)