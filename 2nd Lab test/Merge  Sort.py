def merge_sort(arr):
    print(f"Splitting: {arr}")
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left and right halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f"Merging: {arr}")

# Get user input for the array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Display the unsorted array
print("Unsorted array:", arr)

# Apply Merge Sort and display each step
merge_sort(arr)

# Display the sorted array
print("Sorted array:", arr)